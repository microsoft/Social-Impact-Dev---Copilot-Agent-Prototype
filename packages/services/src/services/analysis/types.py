"""Type definitions for FEC report analysis.

This module provides semantic type aliases for FEC data structures,
making the analysis API more intuitive and self-documenting.
"""

from fec_api_client import CandidateDetail, CommitteeDetail, Filings

# Type alias for quarterly FEC filing reports
# This is the same as Filings but with a more descriptive name for analysis context
QuarterlyReport = Filings

__all__ = [
    "QuarterlyReport",
    "CandidateDetail",
    "CommitteeDetail",
]
