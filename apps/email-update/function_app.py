import json
import logging
import os

import azure.functions as func
from services import (
    AzureBlobStorageService,
    AzureEmailService,
    AzureOpenAISummaryService,
    CandidateReportService,
)

app = func.FunctionApp()
logger = logging.getLogger(__name__)

BLOB_ACCOUNT_URL = os.getenv("BLOB_ACCOUNT_URL")
BLOB_CONTAINER_NAME = os.getenv("BLOB_CONTAINER_NAME", "fec-filings")


def get_candidate_ids() -> list[str]:
    value = os.getenv("FEC_CANDIDATE_IDS", "")
    return [v.strip() for v in value.split(",") if v.strip()]


def get_recipients() -> list[str]:
    value = os.getenv("EMAIL_RECIPIENT_LIST", "")
    return [v.strip() for v in value.split(",") if v.strip()]


def create_report_service() -> CandidateReportService:
    blob_service = AzureBlobStorageService(
        account_url=BLOB_ACCOUNT_URL,
        container_name=BLOB_CONTAINER_NAME,
    )
    return CandidateReportService(
        blob_service=blob_service,
        summary_service=AzureOpenAISummaryService(),
        email_service=AzureEmailService(),
    )


@app.timer_trigger(schedule="0 0 8 15 1,4,7,10 *", arg_name="timer", run_on_startup=False)
def scheduled_report_check(timer: func.TimerRequest) -> None:
    """Runs on 15th of Jan/Apr/Jul/Oct at 8 AM UTC (FEC quarterly deadlines)."""
    if timer.past_due:
        logger.warning("Timer is running late")

    service = create_report_service()
    result = service.process_candidates(get_candidate_ids(), get_recipients())
    logger.info(f"Scheduled run complete: {result}")


@app.route(route="check-reports", methods=["POST"], auth_level=func.AuthLevel.FUNCTION)
def manual_report_check(req: func.HttpRequest) -> func.HttpResponse:
    """POST /api/check-reports - Manual trigger for testing."""
    service = create_report_service()
    result = service.process_candidates(get_candidate_ids(), get_recipients())

    return func.HttpResponse(
        json.dumps(
            {
                "candidates_processed": result.candidates_processed,
                "emails_sent": result.emails_sent,
                "errors": result.errors,
            }
        ),
        mimetype="application/json",
        status_code=200,
    )
