"""Data extraction from FEC CSV files.

Extractors perform Phase 1 analysis: parsing CSV data into structured Python objects
and computing statistics without AI involvement.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from fec_api_client import Filings

    from ..format import ParsedFECFile


# Schedule A column indices (0-indexed)
# Based on SCHEDULE_A_COLUMNS in constants.py
class ScheduleAColumns:
    """Column indices for Schedule A (contributions) records."""

    FORM_TYPE = 0
    COMMITTEE_ID = 1
    ENTITY_TYPE = 5
    ORGANIZATION_NAME = 6
    LAST_NAME = 7
    FIRST_NAME = 8
    MIDDLE_NAME = 9
    CITY = 14
    STATE = 15
    ZIP = 16
    CONTRIBUTION_DATE = 19
    CONTRIBUTION_AMOUNT = 20
    CONTRIBUTION_AGGREGATE = 21
    EMPLOYER = 23
    OCCUPATION = 24


# Federal contribution limit per election
MAX_CONTRIBUTION_LIMIT = 3500.0


@dataclass
class MaxedDonor:
    """A donor who has reached the contribution limit."""

    name: str
    employer: str
    occupation: str
    aggregate: float
    state: str
    city: str


@dataclass
class ExtractionResult:
    """Result of data extraction."""

    data: dict = field(default_factory=dict)
    stats: dict = field(default_factory=dict)
    raw_items: list[dict] = field(default_factory=list)


class BaseExtractor(Protocol):
    """Protocol for data extractors."""

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract data from parsed FEC file.

        Args:
            parsed: Parsed FEC file with contributions and disbursements.
            report: Report metadata from FEC API.

        Returns:
            ExtractionResult with extracted data and statistics.
        """
        ...


def _parse_currency(value: str) -> float:
    """Parse a currency string to float, handling empty/invalid values."""
    if not value or not value.strip():
        return 0.0
    try:
        # Remove quotes, commas, and whitespace
        cleaned = value.strip().strip('"').replace(",", "")
        return float(cleaned)
    except (ValueError, TypeError):
        return 0.0


def _get_column(row: list[str], index: int, default: str = "") -> str:
    """Safely get a column value from a row."""
    if index < len(row):
        return row[index].strip().strip('"')
    return default


def _format_name(first: str, last: str, middle: str = "") -> str:
    """Format a name from first, last, and optional middle."""
    parts = [p for p in [first, middle, last] if p]
    return " ".join(parts)


class MaxedDonorsExtractor:
    """Extract donors who have reached the contribution limit ($3,500)."""

    def __init__(self, limit: float = MAX_CONTRIBUTION_LIMIT) -> None:
        """Initialize extractor with contribution limit.

        Args:
            limit: The maximum contribution limit to filter by.
        """
        self.limit = limit

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract maxed-out donors from contributions.

        Args:
            parsed: Parsed FEC file with contributions.
            report: Report metadata.

        Returns:
            ExtractionResult with maxed donors data and statistics.
        """
        maxed_donors: list[MaxedDonor] = []
        total_individual_contributions = 0.0

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()

            # Only process individual contributions (SA11AI)
            if not form_type.startswith("SA11AI"):
                continue

            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            aggregate = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AGGREGATE))

            total_individual_contributions += amount

            # Check if donor has reached the limit
            if aggregate >= self.limit:
                first = _get_column(row, ScheduleAColumns.FIRST_NAME)
                last = _get_column(row, ScheduleAColumns.LAST_NAME)
                middle = _get_column(row, ScheduleAColumns.MIDDLE_NAME)

                donor = MaxedDonor(
                    name=_format_name(first, last, middle),
                    employer=_get_column(row, ScheduleAColumns.EMPLOYER),
                    occupation=_get_column(row, ScheduleAColumns.OCCUPATION),
                    aggregate=aggregate,
                    state=_get_column(row, ScheduleAColumns.STATE),
                    city=_get_column(row, ScheduleAColumns.CITY),
                )
                maxed_donors.append(donor)

        # Deduplicate by name (same donor may appear multiple times)
        unique_donors = self._deduplicate_donors(maxed_donors)

        # Compute statistics
        total_from_maxed = sum(d.aggregate for d in unique_donors)
        employer_counts = Counter(d.employer for d in unique_donors if d.employer)
        occupation_counts = Counter(d.occupation for d in unique_donors if d.occupation)
        state_counts = Counter(d.state for d in unique_donors if d.state)

        # Calculate percentage of individual contributions
        pct_of_individual = 0.0
        if total_individual_contributions > 0:
            pct_of_individual = (total_from_maxed / total_individual_contributions) * 100

        return ExtractionResult(
            data={
                "donors": [
                    {
                        "name": d.name,
                        "employer": d.employer,
                        "occupation": d.occupation,
                        "aggregate": d.aggregate,
                        "state": d.state,
                        "city": d.city,
                    }
                    for d in unique_donors
                ],
                "top_employers": employer_counts.most_common(10),
                "top_occupations": occupation_counts.most_common(10),
                "top_states": state_counts.most_common(10),
            },
            stats={
                "count": len(unique_donors),
                "total": total_from_maxed,
                "total_individual_contributions": total_individual_contributions,
                "pct_of_individual": pct_of_individual,
            },
            raw_items=[
                {
                    "name": d.name,
                    "employer": d.employer,
                    "occupation": d.occupation,
                    "aggregate": d.aggregate,
                    "state": d.state,
                    "city": d.city,
                }
                for d in unique_donors
            ],
        )

    def _deduplicate_donors(self, donors: list[MaxedDonor]) -> list[MaxedDonor]:
        """Deduplicate donors by name, keeping highest aggregate."""
        seen: dict[str, MaxedDonor] = {}
        for donor in donors:
            key = donor.name.lower()
            if key not in seen or donor.aggregate > seen[key].aggregate:
                seen[key] = donor
        return list(seen.values())
