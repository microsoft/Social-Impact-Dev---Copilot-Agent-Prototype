"""Analysis service orchestrator.

Coordinates extraction and analysis, handles caching.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING, Protocol

from .analyzers import AnalysisResult, MaxedDonorsAnalyzer, SummaryAnalyzer
from .extractors import MaxedDonorsExtractor

if TYPE_CHECKING:
    from fec_api_client import Filings

    from ..format import ParsedFECFile
    from ..storage import BlobStorageService

logger = logging.getLogger(__name__)


@dataclass
class FullAnalysisResult:
    """Result containing all analysis features."""

    summary: str | None = None
    maxed_donors: AnalysisResult | None = None

    def get_combined_narrative(self) -> str:
        """Get combined narrative from all analyses."""
        narratives = []
        if self.summary:
            narratives.append(self.summary)
        if self.maxed_donors and self.maxed_donors.narrative:
            narratives.append(self.maxed_donors.narrative)
        return "\n\n".join(narratives)


class AnalysisService(Protocol):
    """Protocol for analysis services."""

    def generate_summary(
        self,
        report: Filings,
        base_path: str | None = None,
    ) -> str:
        """Generate summary for a report.

        Args:
            report: Report metadata.
            base_path: Optional blob path for caching.

        Returns:
            Summary text.
        """
        ...

    def analyze_maxed_donors(
        self,
        parsed: ParsedFECFile,
        report: Filings,
        base_path: str | None = None,
    ) -> AnalysisResult:
        """Analyze maxed-out donors.

        Args:
            parsed: Parsed FEC file.
            report: Report metadata.
            base_path: Optional blob path for caching.

        Returns:
            AnalysisResult with maxed donors analysis.
        """
        ...

    def run_full_analysis(
        self,
        parsed: ParsedFECFile,
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
    """OpenAI-powered analysis service with caching."""

    def __init__(
        self,
        blob_service: BlobStorageService | None = None,
    ) -> None:
        """Initialize analysis service.

        Args:
            blob_service: Optional blob storage service for caching.
        """
        self.blob_service = blob_service
        self._extractor = MaxedDonorsExtractor()
        self._maxed_donors_analyzer: MaxedDonorsAnalyzer | None = None
        self._summary_analyzer: SummaryAnalyzer | None = None

    def _get_maxed_donors_analyzer(self) -> MaxedDonorsAnalyzer:
        """Lazy-load maxed donors analyzer to defer credential validation."""
        if self._maxed_donors_analyzer is None:
            self._maxed_donors_analyzer = MaxedDonorsAnalyzer()
        return self._maxed_donors_analyzer

    def _get_summary_analyzer(self) -> SummaryAnalyzer:
        """Lazy-load summary analyzer to defer credential validation."""
        if self._summary_analyzer is None:
            self._summary_analyzer = SummaryAnalyzer()
        return self._summary_analyzer

    def generate_summary(
        self,
        report: Filings,
        base_path: str | None = None,
    ) -> str:
        """Generate AI summary for a report with caching.

        Args:
            report: Report metadata.
            base_path: Optional blob path for caching (e.g., "C00718866/2024-Q1").

        Returns:
            Summary text.
        """
        from ..reports import get_display_name

        cache_path = f"{base_path}/summary.txt" if base_path else None
        fallback = f"New report filed by {get_display_name(report)}."

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
            result = analyzer.analyze(report)
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

    def analyze_maxed_donors(
        self,
        parsed: ParsedFECFile,
        report: Filings,
        base_path: str | None = None,
    ) -> AnalysisResult:
        """Analyze maxed-out donors with caching.

        Args:
            parsed: Parsed FEC file.
            report: Report metadata.
            base_path: Optional blob path for caching (e.g., "C00718866/2024-Q1").

        Returns:
            AnalysisResult with maxed donors analysis.
        """
        cache_path = f"{base_path}/analysis/maxed_donors.json" if base_path else None

        # Try to get cached result
        if cache_path and self.blob_service:
            cached = self._get_cached_analysis(cache_path)
            if cached:
                logger.info(f"Using cached maxed donors analysis: {cache_path}")
                return cached

        # Extract data
        extraction = self._extractor.extract(parsed, report)

        # Generate analysis with AI
        analyzer = self._get_maxed_donors_analyzer()
        result = analyzer.analyze(extraction, report)

        # Cache result
        if cache_path and self.blob_service:
            self._cache_analysis(cache_path, result)

        return result

    def run_full_analysis(
        self,
        parsed: ParsedFECFile,
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
        summary = self.generate_summary(report, base_path)
        maxed_donors = self.analyze_maxed_donors(parsed, report, base_path)

        return FullAnalysisResult(
            summary=summary,
            maxed_donors=maxed_donors,
        )

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
        parsed: ParsedFECFile,
        report: Filings,
    ) -> dict:
        """Extract data without AI analysis (useful for testing).

        Args:
            parsed: Parsed FEC file.
            report: Report metadata.

        Returns:
            Dictionary with extraction results.
        """
        extraction = self._extractor.extract(parsed, report)
        return {
            "maxed_donors": {
                "data": extraction.data,
                "stats": extraction.stats,
            }
        }
