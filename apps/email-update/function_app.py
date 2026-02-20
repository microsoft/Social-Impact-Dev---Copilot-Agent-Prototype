import gc
import logging
import os

import azure.functions as func
from services import (
    AnalysisService,
    AzureBlobStorageService,
    AzureEmailService,
    EmailService,
    Filings,
    FullAnalysisResult,
    OpenAIAnalysisService,
    build_report_preview_html,
    parse_comma_list,
    parse_fec_csv,
)

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# Email settings
EMAIL_RECIPIENT_LIST = os.getenv("EMAIL_RECIPIENT_LIST", "")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")
BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL", "")

# Use EventGrid in Azure (Flex Consumption requires it), regular polling locally
IS_AZURE = bool(os.getenv("WEBSITE_SITE_NAME"))
BLOB_TRIGGER_SOURCE = (
    func.BlobSource.EVENT_GRID if IS_AZURE else func.BlobSource.LOGS_AND_CONTAINER_SCAN
)


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


def _run_analysis(
    blob_service: AzureBlobStorageService,
    base_path: str,
    report: Filings,
) -> FullAnalysisResult | None:
    """Run full analysis with caching.

    Downloads CSV, parses it, and runs all extractors and analyzers.

    Returns:
        FullAnalysisResult with all analysis features, or None if failed.
    """
    analysis_service: AnalysisService = OpenAIAnalysisService(blob_service=blob_service)

    # Download the CSV to parse for analysis
    csv_blob_path = None
    try:
        blobs = blob_service.list_blobs(prefix=f"{base_path}/")
        csv_blobs = [b for b in blobs if b.endswith(".csv") and not b.endswith("report.csv")]
        if not csv_blobs:
            # Try without the filtering
            csv_blobs = [b for b in blobs if b.endswith(".csv")]
        if csv_blobs:
            csv_blob_path = csv_blobs[0]
    except Exception as e:
        logger.warning(f"Failed to find CSV blob: {e}")
        return None

    if not csv_blob_path:
        logger.warning(f"No CSV file found in {base_path}")
        return None

    try:
        csv_content = blob_service.download_bytes(csv_blob_path)
        if not csv_content:
            logger.warning(f"Empty CSV file: {csv_blob_path}")
            return None

        # Parse CSV
        parsed = parse_fec_csv(csv_content)

        # Run full analysis with caching
        result = analysis_service.run_full_analysis(parsed, report, base_path)

        # Release CSV content from memory
        del csv_content
        del parsed
        gc.collect()

        return result

    except Exception as e:
        logger.warning(f"Failed to run analysis: {e}")
        return None


@app.blob_trigger(
    arg_name="report_blob",
    path="fec-filings/{committee_id}/{year_quarter}/report.json",
    connection="BLOB_CONNECTION_STRING",
    source=BLOB_TRIGGER_SOURCE,
)
def process_new_report(report_blob: func.InputStream) -> None:
    """Blob trigger that sends email when a new report is synced."""
    blob_name = report_blob.name
    if not blob_name:
        logger.error("Report blob name is empty")
        return

    # Extract base path (e.g., "C00718866/2024-Q1")
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

    # Run full analysis
    analysis = _run_analysis(blob_service, base_path, report)
    summary_text = (
        analysis.summary
        if analysis and analysis.summary
        else f"New report filed by {report.committee_name}."
    )

    # Send email
    email_result = email_service.send_report_email(
        recipients=recipients,
        report=report,
        summary=summary_text,
        formatted_csv_url=formatted_csv_url,
        xlsx_url=xlsx_url,
        analysis=analysis,
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

    # Run full analysis
    analysis = _run_analysis(blob_service, base_path, report)
    summary_text = (
        analysis.summary
        if analysis and analysis.summary
        else f"New report filed by {report.committee_name}."
    )

    # Build HTML preview
    html_content = build_report_preview_html(
        report,
        summary_text,
        formatted_csv_url=formatted_csv_url,
        xlsx_url=xlsx_url,
        analysis=analysis,
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

    # Run full analysis
    analysis = _run_analysis(blob_service, base_path, report)
    summary_text = (
        analysis.summary
        if analysis and analysis.summary
        else f"New report filed by {report.committee_name}."
    )

    # Send email
    try:
        email_service: EmailService = AzureEmailService()
        email_result = email_service.send_report_email(
            recipients=recipients,
            report=report,
            summary=summary_text,
            formatted_csv_url=formatted_csv_url,
            xlsx_url=xlsx_url,
            analysis=analysis,
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
