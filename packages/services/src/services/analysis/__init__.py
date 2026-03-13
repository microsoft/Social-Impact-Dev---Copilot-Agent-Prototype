"""FEC report analysis module.

Provides modular, cacheable analysis features for campaign finance data.
Uses a two-phase approach: data extraction (Python) + AI interpretation (LLM).

Standard Statistics (minimal/no AI):
- A. Max out donors ($3,500)
- B. In-state vs out-of-state percentage
- C. Small vs big donors ($25 threshold)
- D. Funding sources (individuals, loans, transfers, PACs)
- E. Geography breakdown
- F. Interesting expenditures

Detailed AI Analysis:
- Industry/Company analysis
- Grouped donations (fundraiser detection)
- Summary (compiled last with all data)
"""

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
    SummaryResult,
)
from .extractors import (
    DonorSizeExtractor,
    ExpenditureExtractor,
    ExtractionResult,
    FundingSourceExtractor,
    GeographyExtractor,
    GroupedDonationsExtractor,
    IndustryExtractor,
    MaxOutDonor,
    MaxOutDonorsExtractor,
)
from .service import (
    AnalysisService,
    FullAnalysisResult,
    OpenAIAnalysisService,
    get_summary_text,
)
from .types import CandidateDetail, CommitteeDetail, QuarterlyReport

__all__ = [
    # Type aliases
    "QuarterlyReport",
    "CandidateDetail",
    "CommitteeDetail",
    # Analysis results
    "AnalysisResult",
    "ExtractionResult",
    "FullAnalysisResult",
    "SummaryResult",
    # Data classes
    "MaxOutDonor",
    # Extractors (Phase 1 - Python data extraction)
    "DonorSizeExtractor",
    "ExpenditureExtractor",
    "FundingSourceExtractor",
    "GeographyExtractor",
    "GroupedDonationsExtractor",
    "IndustryExtractor",
    "MaxOutDonorsExtractor",
    # Analyzers (Phase 2)
    "DonorSizeAnalyzer",
    "ExpenditureAnalyzer",
    "FundingSourceAnalyzer",
    "GeographyAnalyzer",
    "GroupedDonationsAnalyzer",
    "IndustryAnalyzer",
    "MaxOutDonorsAnalyzer",
    "SummaryAnalyzer",
    # Service
    "AnalysisService",
    "OpenAIAnalysisService",
    "get_summary_text",
]
