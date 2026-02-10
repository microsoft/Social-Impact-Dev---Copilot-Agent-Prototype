import json
import logging
import os

import azure.functions as func
from services import (
    AzureEmailService,
    AzureOpenAISummaryService,
    CandidateReport,
    EmailService,
    SummaryService,
    parse_comma_list,
)

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# Email settings
EMAIL_RECIPIENT_LIST = os.getenv("EMAIL_RECIPIENT_LIST", "")


@app.blob_trigger(
    arg_name="report_blob",
    path="fec-filings/reports/{committee_id}.json",
    connection="BLOB_CONNECTION_STRING",
)
def process_new_report(report_blob: func.InputStream) -> None:
    """Blob trigger that sends email when a new committee report is synced."""
    blob_name = report_blob.name
    if not blob_name:
        logger.error("Report blob name is empty")
        return

    # Extract committee_id from path (e.g., "fec-filings/reports/C00718866.json")
    committee_id = blob_name.split("/")[-1].replace(".json", "")
    logger.info(f"Processing new report for committee: {committee_id}")

    # Read report content
    report_content = report_blob.read()
    if not report_content:
        logger.error(f"Empty report file: {blob_name}")
        return

    try:
        report_data = json.loads(report_content.decode("utf-8"))
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in report {blob_name}: {e}")
        return

    # Parse recipients
    recipients = parse_comma_list(EMAIL_RECIPIENT_LIST)
    if not recipients:
        logger.warning("No recipients configured, skipping email")
        return

    # Initialize services
    summary_service: SummaryService = AzureOpenAISummaryService()
    email_service: EmailService = AzureEmailService()

    # Create CandidateReport from filing data
    report = CandidateReport.from_filing(report_data, committee_id)

    # Generate AI summary
    summary_result = summary_service.generate_candidate_summary(report)
    fallback = f"New quarterly report filed by {report.committee_name}."
    summary_text = summary_result.summary or fallback

    # Send email
    email_result = email_service.send_candidate_report_email(
        recipients=recipients,
        report=report,
        summary=summary_text,
    )

    if email_result.success:
        logger.info(f"Email sent for {report.committee_name}: {email_result.message_id}")
    else:
        logger.error(f"Failed to send email for {report.committee_name}: {email_result.error}")
