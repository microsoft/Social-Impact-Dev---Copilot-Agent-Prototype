"""AI-powered analysis from extracted data.

Analyzers perform Phase 2 analysis: taking pre-computed statistics and
generating human-readable insights using LLM.
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from openai import AzureOpenAI

from .prompts import (
    MAXED_DONORS_SYSTEM_PROMPT,
    MAXED_DONORS_USER_TEMPLATE,
    SUMMARY_SYSTEM_PROMPT,
    SUMMARY_USER_TEMPLATE,
)

if TYPE_CHECKING:
    from fec_api_client import Filings

    from .extractors import ExtractionResult

logger = logging.getLogger(__name__)


@dataclass
class AnalysisResult:
    """Result of AI-powered analysis."""

    feature: str
    data: dict
    stats: dict
    narrative: str
    cached: bool = False


class BaseAnalyzer(Protocol):
    """Protocol for AI-powered analyzers."""

    feature_name: str

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Analyze extracted data and generate narrative.

        Args:
            extraction: Pre-computed extraction result.
            report: Report metadata.

        Returns:
            AnalysisResult with data, stats, and AI-generated narrative.
        """
        ...


class MaxedDonorsAnalyzer:
    """Analyzer for maxed-out donors ($3,500 limit)."""

    feature_name = "maxed_donors"

    def __init__(
        self,
        endpoint: str | None = None,
        api_key: str | None = None,
        deployment: str | None = None,
        api_version: str = "2024-02-15-preview",
    ) -> None:
        """Initialize analyzer with Azure OpenAI credentials.

        Args:
            endpoint: Azure OpenAI endpoint (or AZURE_OPENAI_ENDPOINT env var).
            api_key: Azure OpenAI API key (or AZURE_OPENAI_API_KEY env var).
            deployment: Azure OpenAI deployment name (or AZURE_OPENAI_DEPLOYMENT env var).
            api_version: Azure OpenAI API version.
        """
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

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Analyze maxed donors and generate narrative.

        Args:
            extraction: Extraction result from MaxedDonorsExtractor.
            report: Report metadata.

        Returns:
            AnalysisResult with analysis data and AI narrative.
        """
        from ..reports import get_display_name

        stats = extraction.stats
        data = extraction.data

        # Format report period
        period = f"{report.coverage_start_date} to {report.coverage_end_date}"
        committee_name = get_display_name(report)

        # Format top employers list
        employers_list = self._format_top_list(data.get("top_employers", []))

        # Format top occupations list
        occupations_list = self._format_top_list(data.get("top_occupations", []))

        # Format top states list
        states_list = self._format_top_list(data.get("top_states", []))

        # Skip AI call if no maxed donors
        if stats.get("count", 0) == 0:
            return AnalysisResult(
                feature=self.feature_name,
                data=data,
                stats=stats,
                narrative="No donors reached the $3,500 contribution limit during this period.",
            )

        # Generate narrative using AI
        user_message = MAXED_DONORS_USER_TEMPLATE.format(
            committee_name=committee_name,
            report_period=period,
            count=stats.get("count", 0),
            total=stats.get("total", 0),
            pct=stats.get("pct_of_individual", 0),
            employers_list=employers_list,
            occupations_list=occupations_list,
            states_list=states_list,
        )

        try:
            response = self._client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": MAXED_DONORS_SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=300,
                temperature=0.3,
            )

            narrative = response.choices[0].message.content or ""
            logger.info(f"Generated maxed donors analysis for {committee_name}")

        except Exception as e:
            logger.error(f"Failed to generate maxed donors analysis: {e}")
            # Fallback narrative
            narrative = self._generate_fallback_narrative(stats, data)

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative.strip(),
        )

    def _format_top_list(self, items: list[tuple[str, int]], max_items: int = 5) -> str:
        """Format a list of (name, count) tuples for display."""
        if not items:
            return "- None reported"

        lines = []
        for name, count in items[:max_items]:
            lines.append(f"- {name}: {count} donor(s)")
        return "\n".join(lines)

    def _generate_fallback_narrative(self, stats: dict, data: dict) -> str:
        """Generate a simple fallback narrative without AI."""
        count = stats.get("count", 0)
        total = stats.get("total", 0)
        pct = stats.get("pct_of_individual", 0)

        top_employers = data.get("top_employers", [])
        employer_text = ""
        if top_employers:
            top_employer = top_employers[0][0]
            employer_text = f" The most common employer among maxed donors is {top_employer}."

        return (
            f"{count} donors reached the $3,500 contribution limit, "
            f"contributing ${total:,.2f} ({pct:.1f}% of individual contributions).{employer_text}"
        )


@dataclass
class SummaryResult:
    """Result of generating a summary."""

    summary: str
    cached: bool = False


class SummaryAnalyzer:
    """Analyzer for generating report summaries."""

    feature_name = "summary"

    def __init__(
        self,
        endpoint: str | None = None,
        api_key: str | None = None,
        deployment: str | None = None,
        api_version: str = "2024-02-15-preview",
    ) -> None:
        """Initialize analyzer with Azure OpenAI credentials.

        Args:
            endpoint: Azure OpenAI endpoint (or AZURE_OPENAI_ENDPOINT env var).
            api_key: Azure OpenAI API key (or AZURE_OPENAI_API_KEY env var).
            deployment: Azure OpenAI deployment name (or AZURE_OPENAI_DEPLOYMENT env var).
            api_version: Azure OpenAI API version.
        """
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

    def analyze(self, report: Filings) -> SummaryResult:
        """Generate a summary for a report.

        Args:
            report: Report (Filings) object with filing details.

        Returns:
            SummaryResult with the generated summary.
        """
        from ..reports import get_display_name

        display_name = get_display_name(report)
        user_message = SUMMARY_USER_TEMPLATE.format(
            display_name=display_name,
            committee_name=report.committee_name,
            report_type=report.report_type,
            form_type=report.form_type,
            coverage_start=report.coverage_start_date,
            coverage_end=report.coverage_end_date,
            receipt_date=report.receipt_date,
            financials=self._format_financials(report),
        )

        try:
            response = self._client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": SUMMARY_SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=1000,
                temperature=0.3,
            )

            summary = response.choices[0].message.content
            if not summary:
                return SummaryResult(
                    summary=f"New report filed by {display_name}. (AI summary unavailable)"
                )

            logger.info(f"Generated summary for {report.committee_name}")
            return SummaryResult(summary=summary)

        except Exception as e:
            logger.error(f"Failed to generate summary: {e}")
            return SummaryResult(
                summary=f"New report filed by {display_name}. (AI summary unavailable)"
            )

    def _format_financials(self, report: Filings) -> str:
        """Format financial data for the prompt."""
        lines = []
        if report.total_receipts is not None:
            lines.append(f"Total Receipts: ${report.total_receipts:,.2f}")
        if report.total_disbursements is not None:
            lines.append(f"Total Disbursements: ${report.total_disbursements:,.2f}")
        if report.cash_on_hand_end_period is not None:
            lines.append(f"Cash on Hand: ${report.cash_on_hand_end_period:,.2f}")
        return "\n".join(lines)
