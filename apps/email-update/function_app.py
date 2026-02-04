import json
import logging
import os

import azure.functions as func
from services import (
    AzureBlobStorageService,
    AzureEmailService,
    AzureOpenAISummaryService,
    BlobStorageService,
    EmailService,
    SummaryService,
)

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# Blob storage settings
BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")

# Azure OpenAI settings
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# Email settings
EMAIL_CONNECTION_STRING = os.getenv("EMAIL_CONNECTION_STRING")
EMAIL_SENDER_ADDRESS = os.getenv("EMAIL_SENDER_ADDRESS")
EMAIL_RECIPIENT_LIST = os.getenv("EMAIL_RECIPIENT_LIST", "")


@app.blob_trigger(
    arg_name="manifest",
    path="manifests/{name}.json",
    connection="BLOB_CONNECTION_STRING",
)
def process_manifest(manifest: func.InputStream) -> None:
    """Blob trigger that processes manifest files and sends email summaries.

    Triggered when a new manifest file is uploaded to the manifests container.
    Generates an AI summary of the filings and sends an email notification.
    """
    blob_name = manifest.name
    if not blob_name:
        logger.error("Manifest name is empty")
        return
    logger.info(f"Processing manifest: {blob_name}")

    # Initialize services
    blob_service: BlobStorageService = AzureBlobStorageService(
        account_url=BLOB_ACCOUNT_URL,
        container_name=BLOB_CONTAINER_NAME,
    )
    summary_service: SummaryService = AzureOpenAISummaryService(
        endpoint=AZURE_OPENAI_ENDPOINT,
        api_key=AZURE_OPENAI_API_KEY,
        deployment=AZURE_OPENAI_DEPLOYMENT,
    )
    email_service: EmailService = AzureEmailService(
        connection_string=EMAIL_CONNECTION_STRING,
        sender_address=EMAIL_SENDER_ADDRESS,
    )

    # Check if already processed via metadata
    if blob_service.is_processed(blob_name):
        logger.info(f"Manifest already processed: {blob_name}")
        return

    # Read manifest content
    manifest_content = manifest.read()
    if not manifest_content:
        logger.error(f"Empty manifest file: {blob_name}")
        return

    try:
        manifest_data = json.loads(manifest_content.decode("utf-8"))
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in manifest {blob_name}: {e}")
        return

    filings = manifest_data.get("filings", [])
    if not filings:
        logger.info(f"No filings in manifest: {blob_name}")
        blob_service.mark_as_processed(blob_name)
        return

    # Generate AI summary
    summary_result = summary_service.generate_summary(filings)
    fallback_summary = f"New FEC filings received: {len(filings)} file(s) are available for review."
    summary_text = summary_result.summary or fallback_summary

    # Build file URLs
    file_urls = blob_service.build_file_urls(filings)

    # Send email notification
    recipients = email_service.parse_recipient_list(EMAIL_RECIPIENT_LIST)
    email_service.send_summary_email(
        recipients=recipients,
        filings=filings,
        summary=summary_text,
        file_urls=file_urls,
    )

    # Mark manifest as processed
    blob_service.mark_as_processed(blob_name)
    logger.info(f"Successfully processed manifest: {blob_name}")
