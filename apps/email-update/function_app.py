import json
import logging
import os

import azure.functions as func
from services import (
    AzureBlobStorageService,
    AzureEmailService,
    AzureOpenAISummaryService,
    EmailService,
    QuarterlyReport,
    SummaryService,
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
    """Blob trigger that sends email when a new quarterly report is synced."""
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

    # Create QuarterlyReport from filing data
    report = QuarterlyReport.from_filing(report_data, committee_id)

    # Generate AI summary
    summary_result = summary_service.generate_quarterly_summary(report)
    fallback = f"New quarterly report filed by {report.committee_name}."
    summary_text = summary_result.summary or fallback

    # Send email
    email_result = email_service.send_quarterly_report_email(
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

        report_data = json.loads(report_content.decode("utf-8"))
    except Exception as e:
        logger.error(f"Failed to read report for {committee_id}: {e}")
        return func.HttpResponse(f"Error reading report: {e}", status_code=500)

    # Create QuarterlyReport
    report = QuarterlyReport.from_filing(report_data, committee_id)

    # Generate AI summary
    try:
        summary_service: SummaryService = AzureOpenAISummaryService()
        summary_result = summary_service.generate_quarterly_summary(report)
        summary_text = (
            summary_result.summary or f"New quarterly report filed by {report.committee_name}."
        )
    except Exception as e:
        logger.warning(f"AI summary failed, using fallback: {e}")
        summary_text = (
            f"New quarterly report filed by {report.committee_name}. (AI summary unavailable)"
        )

    # Build HTML preview
    html_content = _build_preview_html(report, summary_text)

    return func.HttpResponse(html_content, mimetype="text/html", status_code=200)


def _build_preview_html(report: QuarterlyReport, summary: str) -> str:
    """Build HTML preview for quarterly report email."""
    financials = ""
    if report.total_receipts is not None:
        financials += f"<li><strong>Total Receipts:</strong> ${report.total_receipts:,.2f}</li>"
    if report.total_disbursements is not None:
        financials += (
            f"<li><strong>Total Disbursements:</strong> ${report.total_disbursements:,.2f}</li>"
        )
    if report.cash_on_hand is not None:
        financials += f"<li><strong>Cash on Hand:</strong> ${report.cash_on_hand:,.2f}</li>"

    links = ""
    if report.pdf_url:
        links += f'<a href="{report.pdf_url}" style="color: #0066cc;">View PDF</a>'
    if report.csv_url:
        if links:
            links += " | "
        links += f'<a href="{report.csv_url}" style="color: #0066cc;">Download CSV</a>'

    period = f"{report.coverage_start_date} to {report.coverage_end_date}"
    # noqa: E501 - HTML template with inline styles
    return f"""<!DOCTYPE html>
<html>
<head>
    <title>FEC Report Preview: {report.committee_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333;
               max-width: 800px; margin: 40px auto; padding: 20px; }}
        .header {{ background: #1a1a1a; color: white; padding: 20px; border-radius: 5px; }}
        .info-box {{ background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .summary-box {{ background: #e8f4f8; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .footer {{ font-size: 12px; color: #666; border-top: 1px solid #ddd;
                   padding-top: 20px; margin-top: 30px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{report.candidate_name} - {report.report_type} Report</h1>
        <p>Preview of email notification</p>
    </div>
    <div class="info-box">
        <p><strong>Committee:</strong> {report.committee_name}</p>
        <p><strong>Period:</strong> {period}</p>
        <p><strong>Filed:</strong> {report.receipt_date}</p>
    </div>
    {"<h3>Financial Summary</h3><ul>" + financials + "</ul>" if financials else ""}
    <h3>AI Summary</h3>
    <div class="summary-box">
        <p>{summary}</p>
    </div>
    {f"<p>{links}</p>" if links else ""}
    <div class="footer">
        <p>This is a preview of the automated notification from the FEC Filing Monitor.</p>
    </div>
</body>
</html>"""
