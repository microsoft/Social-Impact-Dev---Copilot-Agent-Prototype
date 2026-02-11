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
BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL", "")


def _get_filename_from_url(url: str) -> str:
    """Extract the filename from a URL."""
    return url.rstrip("/").split("/")[-1]


def _build_blob_url(base_path: str, filename: str) -> str:
    """Build a blob URL for a file."""
    return f"{BLOB_ACCOUNT_URL.rstrip('/')}/{BLOB_CONTAINER_NAME}/{base_path}/{filename}"


def _build_download_url(req: func.HttpRequest, base_path: str, filename: str) -> str:
    """Build a download URL through the function app."""
    url = req.url
    api_index = url.find("/api/")
    if api_index >= 0:
        base_url = url[:api_index]
    else:
        base_url = url.rsplit("/", 1)[0]
    return f"{base_url}/api/download/{base_path}/{filename}"


def _get_or_create_summary(
    blob_service: AzureBlobStorageService,
    base_path: str,
    report: Filings,
) -> str:
    """Get cached summary from blob storage, or generate and cache a new one.

    Summaries are stored at {base_path}/summary.txt to avoid repeated AI calls.
    """
    summary_blob_path = f"{base_path}/summary.txt"

    # Try to get cached summary
    try:
        cached = blob_service.download_bytes(summary_blob_path)
        if cached:
            logger.info(f"Using cached summary: {summary_blob_path}")
            return cached.decode("utf-8")
    except Exception as e:
        logger.debug(f"No cached summary found: {e}")

    # Generate new summary
    fallback = f"New report filed by {get_display_name(report)}."
    try:
        summary_service: SummaryService = AzureOpenAISummaryService()
        summary_result = summary_service.generate_summary(report)
        summary_text = summary_result.summary or fallback
    except Exception as e:
        logger.warning(f"AI summary failed, using fallback: {e}")
        return f"{fallback} (AI summary unavailable)"

    # Cache the summary
    try:
        blob_service.upload_bytes(
            summary_blob_path,
            summary_text.encode("utf-8"),
            content_type="text/plain",
        )
        logger.info(f"Cached summary: {summary_blob_path}")
    except Exception as e:
        logger.warning(f"Failed to cache summary: {e}")

    return summary_text


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

    # Extract base path (e.g., "C00718866/2024-Q1" from "fec-filings/C00718866/2024-Q1/report.json")
    parts = blob_name.split("/")
    committee_id = parts[1] if len(parts) > 1 else "unknown"
    base_path = "/".join(parts[1:3]) if len(parts) > 2 else ""
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

    # Build URLs - originals from FEC, processed from our blob storage
    formatted_csv_url = None
    xlsx_url = None
    if BLOB_ACCOUNT_URL and base_path and report.csv_url:
        csv_filename = _get_filename_from_url(report.csv_url)
        base_name = csv_filename.rsplit(".", 1)[0]
        formatted_csv_url = _build_blob_url(base_path, f"{base_name}.csv")
        xlsx_url = _build_blob_url(base_path, f"{base_name}.xlsx")

    # Initialize services
    blob_service = AzureBlobStorageService(container_name=BLOB_CONTAINER_NAME)
    email_service: EmailService = AzureEmailService()

    # Get or create cached summary
    summary_text = _get_or_create_summary(blob_service, base_path, report)

    # Send email
    email_result = email_service.send_report_email(
        recipients=recipients,
        report=report,
        summary=summary_text,
        formatted_csv_url=formatted_csv_url,
        xlsx_url=xlsx_url,
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
        # Extract base path (e.g., "C00718866/2024-Q1" from "C00718866/2024-Q1/report.json")
        base_path = "/".join(latest_blob.split("/")[:-1])

        report_content = blob_service.download_bytes(latest_blob)
        if not report_content:
            return func.HttpResponse("Failed to read report", status_code=500)

        report = Filings.from_json(report_content.decode("utf-8"))
    except Exception as e:
        logger.error(f"Failed to read report for {committee_id}: {e}")
        return func.HttpResponse(f"Error reading report: {e}", status_code=500)

    # Build URLs for processed files (formatted CSV and XLSX)
    formatted_csv_url = None
    xlsx_url = None
    if base_path and report.csv_url:
        csv_filename = _get_filename_from_url(report.csv_url)
        base_name = csv_filename.rsplit(".", 1)[0]
        formatted_csv_url = _build_download_url(req, base_path, f"{base_name}.csv")
        xlsx_url = _build_download_url(req, base_path, f"{base_name}.xlsx")

    # Get or create cached summary
    summary_text = _get_or_create_summary(blob_service, base_path, report)

    # Build HTML preview
    html_content = build_report_preview_html(
        report, summary_text, formatted_csv_url=formatted_csv_url, xlsx_url=xlsx_url
    )

    return func.HttpResponse(html_content, mimetype="text/html", status_code=200)


@app.route(
    route="send-test-email/{committee_id}",
    methods=["POST"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def send_test_email(req: func.HttpRequest) -> func.HttpResponse:
    """POST /api/send-test-email/{committee_id} - Manually trigger email for testing."""
    import json

    committee_id = req.route_params.get("committee_id")
    if not committee_id:
        return func.HttpResponse("Missing committee_id", status_code=400)

    # Parse optional recipients from request body
    recipients = None
    try:
        body = req.get_json()
        if body and "recipients" in body:
            recipients = body["recipients"]
    except ValueError:
        pass

    # Fall back to configured recipients
    if not recipients:
        recipients = parse_comma_list(EMAIL_RECIPIENT_LIST)

    if not recipients:
        return func.HttpResponse(
            "No recipients provided in request body or EMAIL_RECIPIENT_LIST",
            status_code=400,
        )

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

        latest_blob = sorted(report_blobs)[-1]
        base_path = "/".join(latest_blob.split("/")[:-1])

        report_content = blob_service.download_bytes(latest_blob)
        if not report_content:
            return func.HttpResponse("Failed to read report", status_code=500)

        report = Filings.from_json(report_content.decode("utf-8"))
    except Exception as e:
        logger.error(f"Failed to read report for {committee_id}: {e}")
        return func.HttpResponse(f"Error reading report: {e}", status_code=500)

    # Build URLs for processed files
    formatted_csv_url = None
    xlsx_url = None
    if BLOB_ACCOUNT_URL and base_path and report.csv_url:
        csv_filename = _get_filename_from_url(report.csv_url)
        base_name = csv_filename.rsplit(".", 1)[0]
        formatted_csv_url = _build_blob_url(base_path, f"{base_name}.csv")
        xlsx_url = _build_blob_url(base_path, f"{base_name}.xlsx")

    # Get or create cached summary
    summary_text = _get_or_create_summary(blob_service, base_path, report)

    # Send email
    try:
        email_service: EmailService = AzureEmailService()
        email_result = email_service.send_report_email(
            recipients=recipients,
            report=report,
            summary=summary_text,
            formatted_csv_url=formatted_csv_url,
            xlsx_url=xlsx_url,
        )

        if email_result.success:
            return func.HttpResponse(
                json.dumps(
                    {
                        "success": True,
                        "message_id": email_result.message_id,
                        "committee_name": report.committee_name,
                        "recipients": recipients,
                    }
                ),
                mimetype="application/json",
                status_code=200,
            )
        else:
            return func.HttpResponse(
                json.dumps({"success": False, "error": email_result.error}),
                mimetype="application/json",
                status_code=500,
            )
    except Exception as e:
        logger.error(f"Failed to send test email: {e}")
        return func.HttpResponse(
            json.dumps({"success": False, "error": str(e)}),
            mimetype="application/json",
            status_code=500,
        )


@app.route(
    route="download/{committee_id}/{year_quarter}/{filename}",
    methods=["GET"],
    auth_level=func.AuthLevel.ANONYMOUS,
)
def download_file(req: func.HttpRequest) -> func.HttpResponse:
    """Download file from blob storage.

    GET /api/download/{committee_id}/{year_quarter}/{filename}
    """
    committee_id = req.route_params.get("committee_id")
    year_quarter = req.route_params.get("year_quarter")
    filename = req.route_params.get("filename")

    if not committee_id or not year_quarter or not filename:
        return func.HttpResponse("Missing path parameters", status_code=400)

    blob_path = f"{committee_id}/{year_quarter}/{filename}"

    # Initialize storage service
    blob_service = AzureBlobStorageService(container_name=BLOB_CONTAINER_NAME)

    try:
        content = blob_service.download_bytes(blob_path)
        if not content:
            return func.HttpResponse(f"File not found: {blob_path}", status_code=404)

        # Determine content type based on extension
        content_type = "application/octet-stream"
        if filename.endswith(".csv"):
            content_type = "text/csv"
        elif filename.endswith(".xlsx"):
            content_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        elif filename.endswith(".pdf"):
            content_type = "application/pdf"
        elif filename.endswith(".json"):
            content_type = "application/json"

        return func.HttpResponse(
            content,
            mimetype=content_type,
            headers={"Content-Disposition": f'attachment; filename="{filename}"'},
            status_code=200,
        )
    except Exception as e:
        logger.error(f"Failed to download {blob_path}: {e}")
        return func.HttpResponse(f"Error downloading file: {e}", status_code=500)
