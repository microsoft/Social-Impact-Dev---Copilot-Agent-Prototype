import logging
import os

import azure.functions as func
from services import (
    AzureBlobStorageService,
    AzureEmailService,
    AzureOpenAISummaryService,
    EmailService,
    Filings,
    SummaryService,
    build_report_preview_html,
    get_display_name,
    parse_comma_list,
)

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# Email settings
EMAIL_RECIPIENT_LIST = os.getenv("EMAIL_RECIPIENT_LIST", "")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")


@app.blob_trigger(
    arg_name="report_blob",
    path="fec-filings/{committee_id}/{year_quarter}/report.json",
    connection="BLOB_CONNECTION_STRING",
)
def process_new_report(report_blob: func.InputStream) -> None:
    """Blob trigger that sends email when a new report is synced."""
    blob_name = report_blob.name
    if not blob_name:
        logger.error("Report blob name is empty")
        return

    # Extract committee_id from path (e.g., "fec-filings/C00718866/2024-Q1/report.json")
    parts = blob_name.split("/")
    committee_id = parts[1] if len(parts) > 1 else "unknown"
    logger.info(f"Processing new report for committee: {committee_id}")

    # Read report content
    report_content = report_blob.read()
    if not report_content:
        logger.error(f"Empty report file: {blob_name}")
        return

    try:
        report = Filings.from_json(report_content.decode("utf-8"))
    except Exception as e:
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

    # Generate AI summary
    summary_result = summary_service.generate_summary(report)
    fallback = f"New report filed by {get_display_name(report)}."
    summary_text = summary_result.summary or fallback

    # Send email
    email_result = email_service.send_report_email(
        recipients=recipients,
        report=report,
        summary=summary_text,
    )

    if email_result.success:
        logger.info(f"Email sent for {report.committee_name}: {email_result.message_id}")
    else:
        logger.error(f"Failed to send email for {report.committee_name}: {email_result.error}")


@app.route(route="preview/{committee_id}", methods=["GET"], auth_level=func.AuthLevel.ANONYMOUS)
def preview_summary(req: func.HttpRequest) -> func.HttpResponse:
    """GET /api/preview/{committee_id} - Preview email summary as HTML."""
    committee_id = req.route_params.get("committee_id")
    if not committee_id:
        return func.HttpResponse("Missing committee_id", status_code=400)

    # Initialize storage service
    blob_service = AzureBlobStorageService(container_name=BLOB_CONTAINER_NAME)

    # Find the latest report for this committee
    try:
        blobs = blob_service.list_blobs(prefix=f"{committee_id}/")
        report_blobs = [b for b in blobs if b.endswith("/report.json")]
        if not report_blobs:
            return func.HttpResponse(
                f"No reports found for committee {committee_id}", status_code=404
            )

        # Get the most recent (last alphabetically = most recent year-quarter)
        latest_blob = sorted(report_blobs)[-1]
        report_content = blob_service.download_bytes(latest_blob)
        if not report_content:
            return func.HttpResponse("Failed to read report", status_code=500)

        report = Filings.from_json(report_content.decode("utf-8"))
    except Exception as e:
        logger.error(f"Failed to read report for {committee_id}: {e}")
        return func.HttpResponse(f"Error reading report: {e}", status_code=500)

    # Generate AI summary
    try:
        summary_service: SummaryService = AzureOpenAISummaryService()
        summary_result = summary_service.generate_summary(report)
        summary_text = summary_result.summary or f"New report filed by {get_display_name(report)}."
    except Exception as e:
        logger.warning(f"AI summary failed, using fallback: {e}")
        summary_text = f"New report filed by {get_display_name(report)}. (AI summary unavailable)"

    # Build HTML preview
    html_content = build_report_preview_html(report, summary_text)

    return func.HttpResponse(html_content, mimetype="text/html", status_code=200)
