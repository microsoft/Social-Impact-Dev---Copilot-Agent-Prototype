"""FEC report analysis module.

Provides modular, cacheable analysis features for campaign finance data.
Uses a two-phase approach: data extraction (Python) + AI interpretation (LLM).
"""

from .analyzers import AnalysisResult, MaxedDonorsAnalyzer, SummaryAnalyzer, SummaryResult
from .extractors import ExtractionResult, MaxedDonor, MaxedDonorsExtractor
from .service import AnalysisService, OpenAIAnalysisService

__all__ = [
    "AnalysisResult",
    "AnalysisService",
    "ExtractionResult",
    "MaxedDonor",
    "MaxedDonorsAnalyzer",
    "MaxedDonorsExtractor",
    "OpenAIAnalysisService",
    "SummaryAnalyzer",
    "SummaryResult",
]
