"""AI-powered analysis from extracted data.

Analyzers perform Phase 2 analysis: taking pre-computed statistics and
generating human-readable insights using LLM.

Standard Statistics (minimal/no AI):
- A. MaxedDonorsAnalyzer
- B & E. GeographyAnalyzer (formats stats, no AI)
- C. DonorSizeAnalyzer (formats stats, no AI)
- D. FundingSourceAnalyzer (formats stats, no AI)
- F. ExpenditureAnalyzer (formats stats, no AI)

Detailed AI Analysis:
- IndustryAnalyzer (AI-powered)
- GroupedDonationsAnalyzer (AI-powered)
- SummaryAnalyzer (AI-powered, compiled last with all data)
"""

from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from openai import AzureOpenAI

from .prompts import (
    GROUPED_DONATIONS_SYSTEM_PROMPT,
    GROUPED_DONATIONS_USER_TEMPLATE,
    INDUSTRY_SYSTEM_PROMPT,
    INDUSTRY_USER_TEMPLATE,
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
        """Analyze extracted data and generate narrative."""
        ...


def _get_openai_client(
    endpoint: str | None = None,
    api_key: str | None = None,
    api_version: str = "2024-02-15-preview",
) -> tuple[AzureOpenAI, str]:
    """Get Azure OpenAI client and deployment name.

    Returns:
        Tuple of (client, deployment_name).

    Raises:
        ValueError: If credentials are not provided.
    """
    _endpoint = endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
    _api_key = api_key or os.getenv("AZURE_OPENAI_API_KEY")
    _deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT")

    if not _endpoint:
        raise ValueError("endpoint or AZURE_OPENAI_ENDPOINT must be provided")
    if not _api_key:
        raise ValueError("api_key or AZURE_OPENAI_API_KEY must be provided")
    if not _deployment:
        raise ValueError("AZURE_OPENAI_DEPLOYMENT must be provided")

    client = AzureOpenAI(
        azure_endpoint=_endpoint,
        api_key=_api_key,
        api_version=api_version,
    )
    return client, _deployment


# =============================================================================
# Standard Statistics Analyzers (minimal/no AI)
# =============================================================================


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
        """Analyze maxed donors and generate narrative."""
        from ..reports import get_display_name

        stats = extraction.stats
        data = extraction.data

        period = f"{report.coverage_start_date} to {report.coverage_end_date}"
        committee_name = get_display_name(report)

        employers_list = self._format_top_list(data.get("top_employers", []))
        occupations_list = self._format_top_list(data.get("top_occupations", []))
        states_list = self._format_top_list(data.get("top_states", []))

        if stats.get("count", 0) == 0:
            return AnalysisResult(
                feature=self.feature_name,
                data=data,
                stats=stats,
                narrative="No donors reached the $3,500 contribution limit.",
            )

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
            narrative = self._generate_fallback_narrative(stats, data)

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative.strip(),
        )

    def _format_top_list(self, items: list[tuple[str, int]], max_items: int = 5) -> str:
        if not items:
            return "- None reported"
        lines = [f"- {name}: {count} donor(s)" for name, count in items[:max_items]]
        return "\n".join(lines)

    def _generate_fallback_narrative(self, stats: dict, data: dict) -> str:
        count = stats.get("count", 0)
        total = stats.get("total", 0)
        pct = stats.get("pct_of_individual", 0)

        top_employers = data.get("top_employers", [])
        employer_text = ""
        if top_employers:
            employer_text = (
                f" The most common employer among maxed donors is {top_employers[0][0]}."
            )

        return (
            f"{count} donors reached the $3,500 contribution limit, "
            f"contributing ${total:,.2f} ({pct:.1f}% of individual contributions)."
            f"{employer_text}"
        )


class GeographyAnalyzer:
    """Analyzer for geographic breakdown (no AI - just formats stats)."""

    feature_name = "geography"

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Format geographic statistics into a narrative."""
        stats = extraction.stats
        data = extraction.data

        candidate_state = data.get("candidate_state", "Unknown")
        in_state_pct = stats.get("in_state_pct", 0)
        out_state_pct = stats.get("out_state_pct", 0)

        top_states = data.get("top_states", [])[:5]
        top_states_str = ", ".join(f"{s['state']} (${s['total']:,.0f})" for s in top_states)

        if candidate_state and candidate_state != "Unknown":
            narrative = (
                f"Geographic breakdown: {in_state_pct:.1f}% in-state ({candidate_state}) "
                f"vs {out_state_pct:.1f}% out-of-state. "
                f"Top contributing states: {top_states_str}."
            )
        else:
            narrative = f"Top contributing states: {top_states_str}."

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative,
        )


class DonorSizeAnalyzer:
    """Analyzer for small vs large donor breakdown (no AI - just formats stats)."""

    feature_name = "donor_size"

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Format donor size statistics into a narrative."""
        stats = extraction.stats
        data = extraction.data

        threshold = data.get("threshold", 25)
        small_count = stats.get("small_count", 0)
        small_pct = stats.get("small_pct", 0)
        big_count = stats.get("big_count", 0)
        big_pct = stats.get("big_pct", 0)

        narrative = (
            f"Donor composition: {small_count:,} small donors (${threshold} or less) "
            f"account for {small_pct:.1f}% of contributions, while {big_count:,} "
            f"larger donors account for {big_pct:.1f}%."
        )

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative,
        )


class FundingSourceAnalyzer:
    """Analyzer for funding source breakdown (no AI - just formats stats)."""

    feature_name = "funding_sources"

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Format funding source statistics into a narrative."""
        stats = extraction.stats
        data = extraction.data

        parts = []
        if stats.get("individuals_pct", 0) > 0:
            parts.append(f"{stats['individuals_pct']:.1f}% individuals")
        if stats.get("pacs_pct", 0) > 0:
            parts.append(f"{stats['pacs_pct']:.1f}% PACs")
        if stats.get("parties_pct", 0) > 0:
            parts.append(f"{stats['parties_pct']:.1f}% parties")
        if stats.get("transfers_pct", 0) > 0:
            parts.append(f"{stats['transfers_pct']:.1f}% transfers")
        if stats.get("loans_pct", 0) > 0:
            parts.append(f"{stats['loans_pct']:.1f}% loans")

        if parts:
            narrative = f"Funding sources: {', '.join(parts)}."
        else:
            narrative = "No funding sources identified."

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative,
        )


class ExpenditureAnalyzer:
    """Analyzer for interesting expenditures (no AI - just formats stats)."""

    feature_name = "expenditures"

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Format expenditure statistics into a narrative."""
        stats = extraction.stats
        data = extraction.data

        flagged_count = stats.get("flagged_count", 0)
        flagged_total = stats.get("flagged_total", 0)
        total_expenditures = stats.get("total_expenditures", 0)

        if flagged_count == 0:
            narrative = "No expenditures flagged for review."
        else:
            flagged = data.get("flagged_expenditures", [])[:5]
            top_items = ", ".join(f"{e['payee']} (${e['amount']:,.0f})" for e in flagged)
            narrative = (
                f"{flagged_count} expenditures flagged (${flagged_total:,.2f} of "
                f"${total_expenditures:,.2f} total). Top items: {top_items}."
            )

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative,
        )


# =============================================================================
# Detailed AI Analysis
# =============================================================================


class IndustryAnalyzer:
    """Analyzer for employer/industry patterns (AI-powered)."""

    feature_name = "industry"

    def __init__(self) -> None:
        self._client: AzureOpenAI | None = None
        self._deployment: str | None = None

    def _ensure_client(self) -> None:
        """Lazy-load OpenAI client."""
        if self._client is None:
            self._client, self._deployment = _get_openai_client()

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Analyze employer/industry patterns."""
        from ..reports import get_display_name

        stats = extraction.stats
        data = extraction.data

        period = f"{report.coverage_start_date} to {report.coverage_end_date}"
        committee_name = get_display_name(report)

        top_employers = data.get("top_employers", [])[:10]
        employers_list = (
            "\n".join(
                f"- {e['employer']}: ${e['total']:,.2f} from {e['count']} donor(s)"
                for e in top_employers
            )
            or "- None reported"
        )

        multi_donor = data.get("multi_donor_employers", [])[:10]
        multi_list = (
            "\n".join(
                f"- {e['employer']}: {e['count']} donors, ${e['total']:,.2f}" for e in multi_donor
            )
            or "- None"
        )

        top_occs = data.get("top_occupations", [])[:10]
        occupations_list = (
            "\n".join(
                f"- {o['occupation']}: ${o['total']:,.2f} from {o['count']} donor(s)"
                for o in top_occs
            )
            or "- None reported"
        )

        # Skip AI if no meaningful data
        if stats.get("unique_employers", 0) == 0:
            return AnalysisResult(
                feature=self.feature_name,
                data=data,
                stats=stats,
                narrative="No employer data available for analysis.",
            )

        self._ensure_client()
        assert self._client is not None
        assert self._deployment is not None

        user_message = INDUSTRY_USER_TEMPLATE.format(
            committee_name=committee_name,
            report_period=period,
            employers_list=employers_list,
            multi_donor_employers=multi_list,
            occupations_list=occupations_list,
            unique_employers=stats.get("unique_employers", 0),
            multi_donor_count=stats.get("multi_donor_employer_count", 0),
        )

        try:
            response = self._client.chat.completions.create(
                model=self._deployment,
                messages=[
                    {"role": "system", "content": INDUSTRY_SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=300,
                temperature=0.3,
            )
            narrative = response.choices[0].message.content or ""
            logger.info(f"Generated industry analysis for {committee_name}")
        except Exception as e:
            logger.error(f"Failed to generate industry analysis: {e}")
            narrative = self._generate_fallback(stats, data)

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative.strip(),
        )

    def _generate_fallback(self, stats: dict, data: dict) -> str:
        top_employers = data.get("top_employers", [])[:3]
        if top_employers:
            names = ", ".join(e["employer"] for e in top_employers)
            return f"Top employers: {names}."
        return "Employer data available but AI analysis unavailable."


class GroupedDonationsAnalyzer:
    """Analyzer for grouped donations / fundraiser detection (AI-powered)."""

    feature_name = "grouped_donations"

    def __init__(self) -> None:
        self._client: AzureOpenAI | None = None
        self._deployment: str | None = None

    def _ensure_client(self) -> None:
        """Lazy-load OpenAI client."""
        if self._client is None:
            self._client, self._deployment = _get_openai_client()

    def analyze(
        self,
        extraction: ExtractionResult,
        report: Filings,
    ) -> AnalysisResult:
        """Analyze donation patterns for potential fundraising events."""
        from ..reports import get_display_name

        stats = extraction.stats
        data = extraction.data

        period = f"{report.coverage_start_date} to {report.coverage_end_date}"
        committee_name = get_display_name(report)

        sig_dates = data.get("significant_dates", [])[:5]
        dates_list = (
            "\n".join(
                f"- {d['date']}: {d['count']} donations, ${d['total']:,.2f}" for d in sig_dates
            )
            or "- None"
        )

        loc_events = data.get("potential_events", [])[:5]
        location_list = (
            "\n".join(
                f"- {e['location']} on {e['date']}: {e['count']} donations, ${e['total']:,.2f}"
                for e in loc_events
            )
            or "- None"
        )

        emp_events = data.get("employer_events", [])[:5]
        employer_list = (
            "\n".join(
                f"- {e['employer']} on {e['date']}: {e['count']} donations, ${e['total']:,.2f}"
                for e in emp_events
            )
            or "- None"
        )

        # Skip AI if no patterns detected
        no_patterns = (
            stats.get("significant_date_count", 0) == 0
            and stats.get("potential_event_count", 0) == 0
            and stats.get("employer_event_count", 0) == 0
        )
        if no_patterns:
            return AnalysisResult(
                feature=self.feature_name,
                data=data,
                stats=stats,
                narrative="No significant donation clustering patterns detected.",
            )

        self._ensure_client()
        assert self._client is not None
        assert self._deployment is not None

        user_message = GROUPED_DONATIONS_USER_TEMPLATE.format(
            committee_name=committee_name,
            report_period=period,
            significant_dates=dates_list,
            location_events=location_list,
            employer_events=employer_list,
            total_contributions=stats.get("total_contributions", 0),
            significant_date_count=stats.get("significant_date_count", 0),
            potential_event_count=stats.get("potential_event_count", 0),
            employer_event_count=stats.get("employer_event_count", 0),
        )

        try:
            response = self._client.chat.completions.create(
                model=self._deployment,
                messages=[
                    {"role": "system", "content": GROUPED_DONATIONS_SYSTEM_PROMPT},
                    {"role": "user", "content": user_message},
                ],
                max_tokens=300,
                temperature=0.3,
            )
            narrative = response.choices[0].message.content or ""
            logger.info(f"Generated grouped donations analysis for {committee_name}")
        except Exception as e:
            logger.error(f"Failed to generate grouped donations analysis: {e}")
            narrative = self._generate_fallback(stats, data)

        return AnalysisResult(
            feature=self.feature_name,
            data=data,
            stats=stats,
            narrative=narrative.strip(),
        )

    def _generate_fallback(self, stats: dict, data: dict) -> str:
        parts = []
        if stats.get("significant_date_count", 0) > 0:
            parts.append(f"{stats['significant_date_count']} dates with significant activity")
        if stats.get("potential_event_count", 0) > 0:
            parts.append(f"{stats['potential_event_count']} potential location events")
        if parts:
            return f"Detected: {', '.join(parts)}."
        return "Donation pattern data available but AI analysis unavailable."


# =============================================================================
# Summary Analyzer (compiled last with all data)
# =============================================================================


@dataclass
class SummaryResult:
    """Result of generating a summary."""

    summary: str
    cached: bool = False


class SummaryAnalyzer:
    """Analyzer for generating report summaries (compiled last with all data)."""

    feature_name = "summary"

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

    def analyze(
        self,
        report: Filings,
        analysis_stats: str = "",
    ) -> SummaryResult:
        """Generate a summary for a report, optionally including analysis stats.

        Args:
            report: Report (Filings) object with filing details.
            analysis_stats: Pre-formatted string of analysis statistics.

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
            analysis_stats=analysis_stats or "No additional analysis available.",
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
        lines = []
        if report.total_receipts is not None:
            lines.append(f"Total Receipts: ${report.total_receipts:,.2f}")
        if report.total_disbursements is not None:
            lines.append(f"Total Disbursements: ${report.total_disbursements:,.2f}")
        if report.cash_on_hand_end_period is not None:
            lines.append(f"Cash on Hand: ${report.cash_on_hand_end_period:,.2f}")
        return "\n".join(lines) if lines else "Financial data not available."
