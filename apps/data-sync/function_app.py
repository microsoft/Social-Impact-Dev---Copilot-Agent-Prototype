import json
import logging
import os
from typing import cast, get_args

import azure.functions as func
from fec_api_client import FecApiClient, ReportTypeCode
from services import AzureBlobStorageService, BlobStorageService, SyncService, parse_comma_list

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# FEC API settings
FEC_API_KEY: str | None = os.getenv("FEC_API_KEY")
FEC_CANDIDATE_IDS: list[str] = parse_comma_list(os.getenv("FEC_CANDIDATE_IDS", ""))
DEFAULT_REPORT_TYPES: list[ReportTypeCode] = ["Q1", "Q2", "Q3", "YE"]
_env_report_types = parse_comma_list(os.getenv("FEC_REPORT_TYPES", ""))
FEC_REPORT_TYPES: list[ReportTypeCode] = cast(
    list[ReportTypeCode],
    [t for t in (_env_report_types or DEFAULT_REPORT_TYPES) if t in get_args(ReportTypeCode)],
)

BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")


def create_sync_service() -> SyncService:
    """Create and configure the SyncService."""
    if not FEC_API_KEY:
        raise ValueError("FEC_API_KEY is required")

    if not FEC_CANDIDATE_IDS:
        raise ValueError("FEC_CANDIDATE_IDS is required")

    fec_client = FecApiClient(auth_token=FEC_API_KEY)
    blob_service: BlobStorageService = AzureBlobStorageService(
        account_url=BLOB_ACCOUNT_URL,
        container_name=BLOB_CONTAINER_NAME,
    )

    return SyncService(
        fec_client=fec_client,
        blob_service=blob_service,
        candidate_ids=FEC_CANDIDATE_IDS,
        report_types=cast(list[str], FEC_REPORT_TYPES),
    )


@app.timer_trigger(schedule="0 0 6 * * *", arg_name="timer", run_on_startup=False)
def scheduled_sync(timer: func.TimerRequest) -> None:
    """Timer trigger that runs daily at 6 AM UTC to sync FEC filings."""
    if timer.past_due:
        logger.warning("Timer is running late")

    try:
        sync_service = create_sync_service()
        reports = sync_service.sync_candidate_reports()
        synced_count = len([r for r in reports.values() if r])
        logger.info(f"Scheduled sync complete: {synced_count} candidates synced")
    except ValueError as e:
        logger.warning(f"Sync skipped: {e}")


@app.route(route="sync", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def manual_sync(req: func.HttpRequest) -> func.HttpResponse:
    """POST /api/sync - Manual trigger for testing."""
    try:
        sync_service = create_sync_service()
        reports = sync_service.sync_candidate_reports()

        return func.HttpResponse(
            json.dumps(
                {
                    "synced": {k: v is not None for k, v in reports.items()},
                    "total_synced": len([r for r in reports.values() if r]),
                }
            ),
            mimetype="application/json",
            status_code=200,
        )
    except ValueError as e:
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            mimetype="application/json",
            status_code=400,
        )
