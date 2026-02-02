import logging
import os

import azure.functions as func
from fec_api_client import FecApiClient
from services import AzureBlobStorageService, FileSyncService

app = func.FunctionApp()
logger = logging.getLogger(__name__)


@app.timer_trigger(schedule="0 0 6 * * *", arg_name="timer", run_on_startup=False)
def check_for_updates(timer: func.TimerRequest) -> None:
    """Timer trigger that runs daily at 6 AM UTC to sync FEC filings."""
    if timer.past_due:
        logger.warning("Timer is running late")

    fec_api_key = os.environ.get("FEC_API_KEY")
    if not fec_api_key:
        raise ValueError("FEC_API_KEY is required")

    sync_service = FileSyncService(
        fec_client=FecApiClient(auth_token=fec_api_key),
        blob_service=AzureBlobStorageService(),
    )

    result = sync_service.sync()
    logger.info(f"Synced {result.filings_processed} filings, {result.files_uploaded} files")
