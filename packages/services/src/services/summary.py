from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Protocol

from openai import AzureOpenAI

logger = logging.getLogger(__name__)


@dataclass
class SummaryResult:
    """Result of generating a summary."""

    success: bool
    summary: str | None = None
    error: str | None = None


class SummaryService(Protocol):
    """Protocol for AI summary generation services."""

    def generate_quarterly_summary(self, report) -> SummaryResult: ...


class AzureOpenAISummaryService:
    """Azure OpenAI-based summary generation service."""

    endpoint: str
    api_key: str
    deployment: str

    def __init__(
        self,
        endpoint: str | None = None,
        api_key: str | None = None,
        deployment: str | None = None,
        api_version: str = "2024-02-15-preview",
    ) -> None:
        _endpoint = endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
        _api_key = api_key or os.getenv("AZURE_OPENAI_API_KEY")
        _deployment = deployment or os.getenv("AZURE_OPENAI_DEPLOYMENT")

        if not _endpoint:
            raise ValueError("endpoint or AZURE_OPENAI_ENDPOINT must be provided")
        if not _api_key:
            raise ValueError("api_key or AZURE_OPENAI_API_KEY must be provided")
        if not _deployment:
            raise ValueError("deployment or AZURE_OPENAI_DEPLOYMENT must be provided")

        self.endpoint = _endpoint
        self.api_key = _api_key
        self.deployment = _deployment

        self._client = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.api_key,
            api_version=api_version,
        )

    def generate_quarterly_summary(self, report) -> SummaryResult:
        """Generate a summary for a quarterly report.

        Args:
            report: QuarterlyReport object with filing details.

        Returns:
            SummaryResult with the generated summary or error.
        """
        report_text = self._format_quarterly_report(report)

        try:
            response = self._client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant that summarizes FEC quarterly "
                            "campaign finance reports. Provide a clear, concise summary "
                            "that highlights key financial information including total "
                            "receipts, disbursements, and cash on hand. "
                            "Keep the tone professional and factual."
                        ),
                    },
                    {
                        "role": "user",
                        "content": f"Please summarize this quarterly FEC filing:\n\n{report_text}",
                    },
                ],
                max_tokens=1000,
                temperature=0.3,
            )

            summary = response.choices[0].message.content
            if not summary:
                return SummaryResult(success=False, error="Empty response from model")

            logger.info(f"Generated summary for {report.committee_name}")
            return SummaryResult(success=True, summary=summary)

        except Exception as e:
            logger.error(f"Failed to generate quarterly summary: {e}")
            return SummaryResult(success=False, error=str(e))

    def _format_quarterly_report(self, report) -> str:
        """Format a QuarterlyReport into readable text for summarization."""
        lines = [
            f"Candidate: {report.candidate_name}",
            f"Committee: {report.committee_name}",
            f"Report Type: {report.report_type}",
            f"Form Type: {report.form_type}",
            f"Coverage Period: {report.coverage_start_date} to {report.coverage_end_date}",
            f"Filing Date: {report.receipt_date}",
        ]

        if report.total_receipts is not None:
            lines.append(f"Total Receipts: ${report.total_receipts:,.2f}")
        if report.total_disbursements is not None:
            lines.append(f"Total Disbursements: ${report.total_disbursements:,.2f}")
        if report.cash_on_hand is not None:
            lines.append(f"Cash on Hand: ${report.cash_on_hand:,.2f}")

        return "\n".join(lines)
