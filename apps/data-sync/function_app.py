import logging
import os

import azure.functions as func
from fec_api_client import FecApiClient
from services import AzureBlobStorageService, BlobStorageService, SyncService

app = func.FunctionApp()
logger = logging.getLogger(__name__)

# FEC API settings
FEC_API_KEY = os.getenv("FEC_API_KEY")

# Blob storage settings
BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")


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
    sync_service = SyncService(
        fec_client=fec_client,
        blob_service=blob_service,
    )

    results = sync_service.sync()
    synced = sum(1 for v in results.values() if v is not None)
    logger.info(f"Synced {synced}/{len(results)} candidates")
