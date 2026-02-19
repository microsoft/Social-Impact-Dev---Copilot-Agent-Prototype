"""Analysis service orchestrator.

Coordinates extraction and analysis, handles caching.
Runs all extractors first (Python data extraction), then AI interpretation,
with summary compiled last using all extracted data.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Protocol

from .analyzers import (
    AnalysisResult,
    DonorSizeAnalyzer,
    ExpenditureAnalyzer,
    FundingSourceAnalyzer,
    GeographyAnalyzer,
    GroupedDonationsAnalyzer,
    IndustryAnalyzer,
    MaxOutDonorsAnalyzer,
    SummaryAnalyzer,
)
from .extractors import (
    DonorSizeExtractor,
    ExpenditureExtractor,
    FundingSourceExtractor,
    GeographyExtractor,
    GroupedDonationsExtractor,
    IndustryExtractor,
    MaxOutDonorsExtractor,
)

if TYPE_CHECKING:
    from fec_api_client import CommitteeDetail, Filings

    from ..report.format import ParsedQuarterlyCSV
    from ..storage import BlobStorageService

logger = logging.getLogger(__name__)


@dataclass
class FullAnalysisResult:
    """Result containing all analysis features."""

    summary: str | None = None
    max_out_donors: AnalysisResult | None = None
    geography: AnalysisResult | None = None
    donor_size: AnalysisResult | None = None
    funding_sources: AnalysisResult | None = None
    expenditures: AnalysisResult | None = None
    industry: AnalysisResult | None = None
    grouped_donations: AnalysisResult | None = None

    # All extracted stats for summary compilation
    all_stats: dict = field(default_factory=dict)

    def get_combined_narrative(self) -> str:
        """Get combined narrative from all analyses."""
        narratives = []
        if self.summary:
            narratives.append(self.summary)
        if self.max_out_donors and self.max_out_donors.narrative:
            narratives.append(f"**Max Out Donors:** {self.max_out_donors.narrative}")
        if self.geography and self.geography.narrative:
            narratives.append(f"**Geography:** {self.geography.narrative}")
        if self.donor_size and self.donor_size.narrative:
            narratives.append(f"**Donor Size:** {self.donor_size.narrative}")
        if self.funding_sources and self.funding_sources.narrative:
            narratives.append(f"**Funding Sources:** {self.funding_sources.narrative}")
        if self.expenditures and self.expenditures.narrative:
            narratives.append(f"**Expenditures:** {self.expenditures.narrative}")
        if self.industry and self.industry.narrative:
            narratives.append(f"**Industry Analysis:** {self.industry.narrative}")
        if self.grouped_donations and self.grouped_donations.narrative:
            narratives.append(f"**Grouped Donations:** {self.grouped_donations.narrative}")
        return "\n\n".join(narratives)

    def get_stats_summary(self) -> dict:
        """Get a summary of all statistics for the email template."""
        stats = {}
        if self.max_out_donors:
            stats["max_out_donors"] = self.max_out_donors.stats
        if self.geography:
            stats["geography"] = self.geography.stats
        if self.donor_size:
            stats["donor_size"] = self.donor_size.stats
        if self.funding_sources:
            stats["funding_sources"] = self.funding_sources.stats
        if self.expenditures:
            stats["expenditures"] = self.expenditures.stats
        if self.industry:
            stats["industry"] = self.industry.stats
        if self.grouped_donations:
            stats["grouped_donations"] = self.grouped_donations.stats
        return stats


class AnalysisService(Protocol):
    """Protocol for analysis services."""

    def generate_summary(
        self,
        report: Filings,
        base_path: str | None = None,
        analysis_stats: str = "",
    ) -> str:
        """Generate summary for a report.

        Args:
            report: Report metadata.
            base_path: Optional blob path for caching.
            analysis_stats: Pre-formatted analysis statistics for the summary.

        Returns:
            Summary text.
        """
        ...

    def analyze_max_out_donors(
        self,
        parsed: ParsedQuarterlyCSV,
        report: Filings,
        base_path: str | None = None,
    ) -> AnalysisResult:
        """Analyze max out donors."""
        ...

    def run_full_analysis(
        self,
        parsed: ParsedQuarterlyCSV,
        report: Filings,
        base_path: str | None = None,
    ) -> FullAnalysisResult:
        """Run all available analyses.

        Args:
            parsed: Parsed FEC file.
            report: Report metadata.
            base_path: Optional blob path for caching.

        Returns:
            FullAnalysisResult with all analyses.
        """
        ...


class OpenAIAnalysisService:
    """OpenAI-powered analysis service with caching.

    Runs all extractors (Python data extraction) first, then AI interpretation.
    Summary is compiled last with all extracted statistics.
    """

    def __init__(
        self,
        blob_service: BlobStorageService | None = None,
    ) -> None:
        """Initialize analysis service.

        Args:
            blob_service: Optional blob storage service for caching.
        """
        self.blob_service = blob_service

        # Extractors (no AI)
        self._max_out_donors_extractor = MaxOutDonorsExtractor()
        self._geography_extractor = GeographyExtractor()
        self._donor_size_extractor = DonorSizeExtractor()
        self._funding_source_extractor = FundingSourceExtractor()
        self._expenditure_extractor = ExpenditureExtractor()
        self._industry_extractor = IndustryExtractor()
        self._grouped_donations_extractor = GroupedDonationsExtractor()

        # Analyzers (lazy-loaded to defer credential validation)
        self._max_out_donors_analyzer: MaxOutDonorsAnalyzer | None = None
        self._geography_analyzer: GeographyAnalyzer | None = None
        self._donor_size_analyzer: DonorSizeAnalyzer | None = None
        self._funding_source_analyzer: FundingSourceAnalyzer | None = None
        self._expenditure_analyzer: ExpenditureAnalyzer | None = None
        self._industry_analyzer: IndustryAnalyzer | None = None
        self._grouped_donations_analyzer: GroupedDonationsAnalyzer | None = None
        self._summary_analyzer: SummaryAnalyzer | None = None

    # Lazy-load analyzers
    def _get_max_out_donors_analyzer(self) -> MaxOutDonorsAnalyzer:
        if self._max_out_donors_analyzer is None:
            self._max_out_donors_analyzer = MaxOutDonorsAnalyzer()
        return self._max_out_donors_analyzer

    def _get_geography_analyzer(self) -> GeographyAnalyzer:
        if self._geography_analyzer is None:
            self._geography_analyzer = GeographyAnalyzer()
        return self._geography_analyzer

    def _get_donor_size_analyzer(self) -> DonorSizeAnalyzer:
        if self._donor_size_analyzer is None:
            self._donor_size_analyzer = DonorSizeAnalyzer()
        return self._donor_size_analyzer

    def _get_funding_source_analyzer(self) -> FundingSourceAnalyzer:
        if self._funding_source_analyzer is None:
            self._funding_source_analyzer = FundingSourceAnalyzer()
        return self._funding_source_analyzer

    def _get_expenditure_analyzer(self) -> ExpenditureAnalyzer:
        if self._expenditure_analyzer is None:
            self._expenditure_analyzer = ExpenditureAnalyzer()
        return self._expenditure_analyzer

    def _get_industry_analyzer(self) -> IndustryAnalyzer:
        if self._industry_analyzer is None:
            self._industry_analyzer = IndustryAnalyzer()
        return self._industry_analyzer

    def _get_grouped_donations_analyzer(self) -> GroupedDonationsAnalyzer:
        if self._grouped_donations_analyzer is None:
            self._grouped_donations_analyzer = GroupedDonationsAnalyzer()
        return self._grouped_donations_analyzer

    def _get_summary_analyzer(self) -> SummaryAnalyzer:
        if self._summary_analyzer is None:
            self._summary_analyzer = SummaryAnalyzer()
        return self._summary_analyzer

    def generate_summary(
        self,
        report: Filings,
        base_path: str | None = None,
        analysis_stats: str = "",
    ) -> str:
        """Generate AI summary for a report with caching.

        Args:
            report: Report metadata.
            base_path: Optional blob path for caching.
            analysis_stats: Pre-formatted analysis statistics.

        Returns:
            Summary text.
        """
        cache_path = f"{base_path}/summary.txt" if base_path else None
        fallback = f"New report filed by {report.committee_name}."

        # Try to get cached result
        if cache_path and self.blob_service:
            try:
                cached = self.blob_service.download_bytes(cache_path)
                if cached:
                    logger.info(f"Using cached summary: {cache_path}")
                    return cached.decode("utf-8")
            except Exception as e:
                logger.debug(f"No cached summary found: {e}")

        # Generate summary with AI
        try:
            analyzer = self._get_summary_analyzer()
            result = analyzer.analyze(report, analysis_stats=analysis_stats)
            summary_text = result.summary
        except Exception as e:
            logger.warning(f"AI summary failed, using fallback: {e}")
            return f"{fallback} (AI summary unavailable)"

        # Cache result
        if cache_path and self.blob_service:
            try:
                self.blob_service.upload_bytes(
                    cache_path,
                    summary_text.encode("utf-8"),
                    content_type="text/plain",
                )
                logger.info(f"Cached summary: {cache_path}")
            except Exception as e:
                logger.warning(f"Failed to cache summary: {e}")

        return summary_text

    def analyze_max_out_donors(
        self,
        parsed: ParsedQuarterlyCSV,
        report: Filings,
        base_path: str | None = None,
    ) -> AnalysisResult:
        """Analyze max out donors with caching."""
        cache_path = f"{base_path}/analysis/max_out_donors.json" if base_path else None

        if cache_path and self.blob_service:
            cached = self._get_cached_analysis(cache_path)
            if cached:
                logger.info(f"Using cached max out donors analysis: {cache_path}")
                return cached

        extraction = self._max_out_donors_extractor.extract(parsed, report)
        analyzer = self._get_max_out_donors_analyzer()
        result = analyzer.analyze(extraction, report)

        if cache_path and self.blob_service:
            self._cache_analysis(cache_path, result)

        return result

    def _get_committee(self, committee_id: str) -> CommitteeDetail | None:
        """Load committee details from blob storage."""
        if not self.blob_service:
            return None

        from fec_api_client import CommitteeDetail

        blob_path = f"{committee_id}/committee.json"
        try:
            cached = self.blob_service.download_bytes(blob_path)
            if cached:
                return CommitteeDetail.from_json(cached.decode("utf-8"))
        except Exception as e:
            logger.debug(f"No cached committee found at {blob_path}: {e}")

        return None

    def run_full_analysis(
        self,
        parsed: ParsedQuarterlyCSV,
        report: Filings,
        base_path: str | None = None,
    ) -> FullAnalysisResult:
        """Run all available analyses.

        Order:
        1. Extract all data (Python, no AI)
        2. Run standard stat analyzers (minimal/no AI)
        3. Run detailed AI analyzers (industry, grouped donations)
        4. Compile summary last with all extracted statistics
        """
        if not report.state and report.committee_id:
            committee = self._get_committee(report.committee_id)
            if committee and committee.state:
                report.state = committee.state

        # Phase 1: Extract all data (no AI)
        logger.info("Phase 1: Extracting data...")
        max_out_extraction = self._max_out_donors_extractor.extract(parsed, report)
        geography_extraction = self._geography_extractor.extract(parsed, report)
        donor_size_extraction = self._donor_size_extractor.extract(parsed, report)
        funding_extraction = self._funding_source_extractor.extract(parsed, report)
        expenditure_extraction = self._expenditure_extractor.extract(parsed, report)
        industry_extraction = self._industry_extractor.extract(parsed, report)
        grouped_extraction = self._grouped_donations_extractor.extract(parsed, report)

        # Phase 2a: Standard stat analyzers (minimal/no AI)
        logger.info("Phase 2a: Running standard analyzers...")
        max_out_result = self._get_max_out_donors_analyzer().analyze(max_out_extraction, report)
        geography_result = self._get_geography_analyzer().analyze(geography_extraction, report)
        donor_size_result = self._get_donor_size_analyzer().analyze(donor_size_extraction, report)
        funding_result = self._get_funding_source_analyzer().analyze(funding_extraction, report)
        expenditure_result = self._get_expenditure_analyzer().analyze(
            expenditure_extraction, report
        )

        # Phase 2b: Detailed AI analyzers
        logger.info("Phase 2b: Running AI analyzers...")
        industry_result = self._get_industry_analyzer().analyze(industry_extraction, report)
        grouped_result = self._get_grouped_donations_analyzer().analyze(grouped_extraction, report)

        # Phase 3: Compile summary last with all data
        logger.info("Phase 3: Compiling summary...")
        analysis_stats = self._format_analysis_stats(
            max_out_result,
            geography_result,
            donor_size_result,
            funding_result,
            expenditure_result,
        )
        summary = self.generate_summary(report, base_path, analysis_stats)

        # Cache individual analyses
        if base_path and self.blob_service:
            self._cache_analysis(f"{base_path}/analysis/max_out_donors.json", max_out_result)
            self._cache_analysis(f"{base_path}/analysis/geography.json", geography_result)
            self._cache_analysis(f"{base_path}/analysis/donor_size.json", donor_size_result)
            self._cache_analysis(f"{base_path}/analysis/funding.json", funding_result)
            self._cache_analysis(f"{base_path}/analysis/expenditures.json", expenditure_result)
            self._cache_analysis(f"{base_path}/analysis/industry.json", industry_result)
            self._cache_analysis(f"{base_path}/analysis/grouped_donations.json", grouped_result)

        return FullAnalysisResult(
            summary=summary,
            max_out_donors=max_out_result,
            geography=geography_result,
            donor_size=donor_size_result,
            funding_sources=funding_result,
            expenditures=expenditure_result,
            industry=industry_result,
            grouped_donations=grouped_result,
            all_stats={
                "max_out_donors": max_out_extraction.stats,
                "geography": geography_extraction.stats,
                "donor_size": donor_size_extraction.stats,
                "funding_sources": funding_extraction.stats,
                "expenditures": expenditure_extraction.stats,
            },
        )

    def _format_analysis_stats(
        self,
        max_out: AnalysisResult,
        geography: AnalysisResult,
        donor_size: AnalysisResult,
        funding: AnalysisResult,
        expenditure: AnalysisResult,
    ) -> str:
        """Format all statistics for the summary prompt."""
        lines = []

        # Maxed donors
        ms = max_out.stats
        lines.append(
            f"- Max Out Donors ($3,500): {ms.get('count', 0)} donors, "
            f"${ms.get('total', 0):,.2f}"
        )

        # Geography
        gs = geography.stats
        lines.append(
            f"- Geography: {gs.get('in_state_pct', 0):.1f}% in-state, "
            f"{gs.get('out_state_pct', 0):.1f}% out-of-state"
        )

        # Donor size
        ds = donor_size.stats
        lines.append(
            f"- Donor Size: {ds.get('small_pct', 0):.1f}% from small donors ($25 or less), "
            f"{ds.get('big_pct', 0):.1f}% from larger donors"
        )

        # Funding sources
        fs = funding.stats
        lines.append(
            f"- Funding Sources: {fs.get('individuals_pct', 0):.1f}% individuals, "
            f"{fs.get('pacs_pct', 0):.1f}% PACs, {fs.get('parties_pct', 0):.1f}% parties"
        )

        # Expenditures
        es = expenditure.stats
        lines.append(
            f"- Flagged Expenditures: {es.get('flagged_count', 0)} items "
            f"(${es.get('flagged_total', 0):,.2f})"
        )

        return "\n".join(lines)

    def _get_cached_analysis(self, cache_path: str) -> AnalysisResult | None:
        """Get cached analysis from blob storage."""
        if not self.blob_service:
            return None

        try:
            content = self.blob_service.download_bytes(cache_path)
            if content:
                data = json.loads(content.decode("utf-8"))
                return AnalysisResult(
                    feature=data["feature"],
                    data=data["data"],
                    stats=data["stats"],
                    narrative=data["narrative"],
                    cached=True,
                )
        except Exception as e:
            logger.debug(f"No cached analysis found at {cache_path}: {e}")

        return None

    def _cache_analysis(self, cache_path: str, result: AnalysisResult) -> None:
        """Cache analysis result to blob storage."""
        if not self.blob_service:
            return

        try:
            data = {
                "feature": result.feature,
                "data": result.data,
                "stats": result.stats,
                "narrative": result.narrative,
            }
            self.blob_service.upload_bytes(
                cache_path,
                json.dumps(data, indent=2).encode("utf-8"),
                content_type="application/json",
            )
            logger.info(f"Cached analysis: {cache_path}")
        except Exception as e:
            logger.warning(f"Failed to cache analysis at {cache_path}: {e}")

    def extract_only(
        self,
        parsed: ParsedQuarterlyCSV,
        report: Filings,
    ) -> dict:
        """Extract data without AI analysis (useful for testing).

        Args:
            parsed: Parsed FEC file.
            report: Report metadata.

        Returns:
            Dictionary with all extraction results.
        """
        return {
            "max_out_donors": {
                "data": self._max_out_donors_extractor.extract(parsed, report).data,
                "stats": self._max_out_donors_extractor.extract(parsed, report).stats,
            },
            "geography": {
                "data": self._geography_extractor.extract(parsed, report).data,
                "stats": self._geography_extractor.extract(parsed, report).stats,
            },
            "donor_size": {
                "data": self._donor_size_extractor.extract(parsed, report).data,
                "stats": self._donor_size_extractor.extract(parsed, report).stats,
            },
            "funding_sources": {
                "data": self._funding_source_extractor.extract(parsed, report).data,
                "stats": self._funding_source_extractor.extract(parsed, report).stats,
            },
            "expenditures": {
                "data": self._expenditure_extractor.extract(parsed, report).data,
                "stats": self._expenditure_extractor.extract(parsed, report).stats,
            },
            "industry": {
                "data": self._industry_extractor.extract(parsed, report).data,
                "stats": self._industry_extractor.extract(parsed, report).stats,
            },
            "grouped_donations": {
                "data": self._grouped_donations_extractor.extract(parsed, report).data,
                "stats": self._grouped_donations_extractor.extract(parsed, report).stats,
            },
        }
