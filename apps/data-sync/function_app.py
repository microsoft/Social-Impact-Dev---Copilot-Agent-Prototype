import logging
import os

import azure.functions as func
from fec_api_client import FecApiClient
from services import AzureBlobStorageService, BlobStorageService, SyncService

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# FEC API settings
FEC_API_KEY = os.getenv("FEC_API_KEY")
FEC_CANDIDATE_IDS = os.getenv("FEC_CANDIDATE_IDS", "")
FEC_REPORT_TYPES = os.getenv("FEC_REPORT_TYPES", "")

# Blob storage settings
BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")


def parse_comma_list(value: str) -> list[str] | None:
    """Parse comma-separated string into list, or None if empty."""
    if not value:
        return None
    return [v.strip() for v in value.split(",") if v.strip()]


@app.timer_trigger(schedule="0 0 6 * * *", arg_name="timer", run_on_startup=False)
def check_for_updates(timer: func.TimerRequest) -> None:
    """Timer trigger that runs daily at 6 AM UTC to sync FEC filings."""
    if timer.past_due:
        logger.warning("Timer is running late")

    if not FEC_API_KEY:
        raise ValueError("FEC_API_KEY is required")

    # Initialize services
    fec_client = FecApiClient(auth_token=FEC_API_KEY)
    blob_service: BlobStorageService = AzureBlobStorageService(
        account_url=BLOB_ACCOUNT_URL,
        container_name=BLOB_CONTAINER_NAME,
    )
    candidate_ids = parse_comma_list(FEC_CANDIDATE_IDS)
    if not candidate_ids:
        logger.warning("No candidate IDs configured, nothing to sync")
        return

    sync_service = SyncService(
        fec_client=fec_client,
        blob_service=blob_service,
        candidate_ids=candidate_ids,
        report_types=parse_comma_list(FEC_REPORT_TYPES),
    )

    reports = sync_service.sync_candidate_reports()
    logger.info(f"Synced reports for {len([r for r in reports.values() if r])} candidates")
