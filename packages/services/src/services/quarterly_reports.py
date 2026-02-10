from __future__ import annotations

import json
import logging
from dataclasses import dataclass

from .email import EmailService
from .storage import BlobStorageService
from .summary import SummaryService

logger = logging.getLogger(__name__)


@dataclass
class QuarterlyReport:
    """A committee's quarterly campaign finance report (FEC Form 3)."""

    committee_id: str
    candidate_name: str
    committee_name: str
    report_type: str
    coverage_start_date: str
    coverage_end_date: str
    receipt_date: str
    filing_id: str
    form_type: str
    csv_url: str | None
    pdf_url: str | None
    total_receipts: float | None = None
    total_disbursements: float | None = None
    cash_on_hand: float | None = None

    @classmethod
    def from_filing(cls, filing: dict, committee_id: str) -> QuarterlyReport:
        """Create from FEC filing data."""
        return cls(
            committee_id=committee_id,
            candidate_name=filing.get("candidate_name") or "Unknown",
            committee_name=filing.get("committee_name") or "Unknown",
            report_type=filing.get("report_type", ""),
            coverage_start_date=filing.get("coverage_start_date", ""),
            coverage_end_date=filing.get("coverage_end_date", ""),
            receipt_date=filing.get("receipt_date", ""),
            filing_id=str(filing.get("file_number", "")),
            form_type=filing.get("form_type", ""),
            csv_url=filing.get("csv_url"),
            pdf_url=filing.get("pdf_url"),
            total_receipts=filing.get("total_receipts"),
            total_disbursements=filing.get("total_disbursements"),
            cash_on_hand=filing.get("cash_on_hand_end_period"),
        )


@dataclass
class ProcessingResult:
    """Result of processing quarterly reports."""

    committees_processed: int
    emails_sent: int
    errors: list[str]


class QuarterlyReportService:
    """Service for reading and processing quarterly reports from blob storage."""

    def __init__(
        self,
        blob_service: BlobStorageService,
        summary_service: SummaryService,
        email_service: EmailService,
    ) -> None:
        self.blob_service = blob_service
        self.summary_service = summary_service
        self.email_service = email_service

    def process_committees(
        self,
        committee_ids: list[str],
        recipients: list[str],
    ) -> ProcessingResult:
        """Read reports from storage, summarize, and send emails.

        Args:
            committee_ids: List of committee IDs to process
            recipients: Email addresses to send reports to

        Returns:
            ProcessingResult with summary of operations
        """
        result = ProcessingResult(committees_processed=0, emails_sent=0, errors=[])

        for committee_id in committee_ids:
            try:
                self._process_single_committee(committee_id, recipients, result)
            except Exception as e:
                logger.error(f"Error processing {committee_id}: {e}")
                result.errors.append(f"{committee_id}: {e}")

        logger.info(f"Processing complete: {result}")
        return result

    def _process_single_committee(
        self,
        committee_id: str,
        recipients: list[str],
        result: ProcessingResult,
    ) -> None:
        """Process a single committee's report from storage."""
        logger.info(f"Processing committee: {committee_id}")

        report = self._read_report_from_storage(committee_id)
        if not report:
            logger.warning(f"No report found in storage for {committee_id}")
            result.errors.append(f"No report in storage for {committee_id}")
            return

        result.committees_processed += 1

        summary = self._generate_summary(report)
        email_result = self.email_service.send_quarterly_report_email(
            recipients=recipients,
            report=report,
            summary=summary,
        )

        if email_result.success:
            logger.info(f"Email sent for {report.committee_name}")
            result.emails_sent += 1
        else:
            result.errors.append(f"Email failed for {committee_id}: {email_result.error}")

    def _read_report_from_storage(self, committee_id: str) -> QuarterlyReport | None:
        """Read a committee's report from blob storage."""
        blob_path = f"reports/{committee_id}.json"

        try:
            data = self.blob_service.download_bytes(blob_path)
            if not data:
                return None

            filing = json.loads(data)
            return QuarterlyReport.from_filing(filing, committee_id)

        except Exception as e:
            logger.error(f"Failed to read report for {committee_id}: {e}")
            return None

    def _generate_summary(self, report: QuarterlyReport) -> str:
        """Generate AI summary for a report, with fallback."""
        summary_result = self.summary_service.generate_quarterly_summary(report)
        if summary_result.success and summary_result.summary:
            return summary_result.summary
        return f"{report.report_type} report filed on {report.receipt_date}."
