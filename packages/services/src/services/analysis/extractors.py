"""Data extraction from FEC CSV files.

Extractors perform Phase 1 analysis: parsing CSV data into structured Python objects
and computing statistics without AI involvement.

Standard Statistics (minimal AI):
- A. Max out donors ($3,500)
- B. In-state vs out-of-state percentage
- C. Small vs big donors ($25 threshold)
- D. Funding sources (individuals, loans, transfers, PACs)
- E. Geography breakdown
- F. Interesting expenditures

Detailed Analysis (AI-powered):
- Industry/Company analysis
- Grouped donations (fundraiser detection)
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:
    from fec_api_client import Filings

    from ..report.format import ParsedFECFile


# =============================================================================
# Column Indices
# =============================================================================


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


class ScheduleBColumns:
    """Column indices for Schedule B (disbursements) records."""

    FORM_TYPE = 0
    COMMITTEE_ID = 1
    ENTITY_TYPE = 5
    PAYEE_ORG_NAME = 6
    PAYEE_LAST_NAME = 7
    PAYEE_FIRST_NAME = 8
    PAYEE_CITY = 14
    PAYEE_STATE = 15
    EXPENDITURE_DATE = 19
    EXPENDITURE_AMOUNT = 20
    PURPOSE_DESCRIPTION = 22
    CATEGORY_CODE = 23


# =============================================================================
# Constants
# =============================================================================

# Federal contribution limit per election
MAX_CONTRIBUTION_LIMIT = 3500.0

# Small donor threshold
SMALL_DONOR_THRESHOLD = 25.0

# Form type prefixes for contribution sources
INDIVIDUAL_CONTRIBUTION_TYPES = ("SA11AI",)  # Individual contributions
PARTY_CONTRIBUTION_TYPES = ("SA11B",)  # Political party contributions
PAC_CONTRIBUTION_TYPES = ("SA11C",)  # PAC contributions
TRANSFER_TYPES = ("SA12",)  # Transfers from affiliated committees
LOAN_TYPES = ("SA13", "SC")  # Loans (SA13 = loans received, SC = loan schedule)
OTHER_RECEIPT_TYPES = ("SA14", "SA15", "SA16", "SA17")  # Offsets and other receipts

# Keywords for flagging interesting expenditures
INTERESTING_EXPENDITURE_KEYWORDS = [
    # Travel & Hospitality
    "resort",
    "hotel",
    "spa",
    "vacation",
    "cruise",
    "airline",
    "flight",
    # Retail & Personal
    "retail",
    "clothing",
    "apparel",
    "gift",
    "jewelry",
    "amazon",
    "walmart",
    # Entertainment
    "entertainment",
    "restaurant",
    "catering",
    "golf",
    "country club",
    # Professional Services (potentially unusual)
    "legal settlement",
    "penalty",
    "fine",
    # Family/Related
    "spouse",
    "family member",
    "relative",
]


# =============================================================================
# Data Classes
# =============================================================================


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
class Contribution:
    """A single contribution record."""

    name: str
    employer: str
    occupation: str
    amount: float
    aggregate: float
    state: str
    city: str
    date: str
    form_type: str
    entity_type: str


@dataclass
class Expenditure:
    """A single expenditure record."""

    payee: str
    amount: float
    date: str
    purpose: str
    category: str
    city: str
    state: str
    form_type: str


@dataclass
class ExtractionResult:
    """Result of data extraction."""

    data: dict = field(default_factory=dict)
    stats: dict = field(default_factory=dict)
    raw_items: list[dict] = field(default_factory=list)


# =============================================================================
# Helper Functions
# =============================================================================


def _parse_currency(value: str) -> float:
    """Parse a currency string to float, handling empty/invalid values."""
    if not value or not value.strip():
        return 0.0
    try:
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


def _parse_date(date_str: str) -> str | None:
    """Parse FEC date format (YYYYMMDD) to ISO format."""
    if not date_str or len(date_str) < 8:
        return None
    try:
        return datetime.strptime(date_str[:8], "%Y%m%d").strftime("%Y-%m-%d")
    except ValueError:
        return None


def _get_candidate_state(report: Filings) -> str | None:
    """Extract candidate's state from report metadata."""
    # Try to get from the report's candidate info or committee info
    if hasattr(report, "state") and report.state:
        return report.state
    # Could also parse from committee_name or other fields if needed
    return None


class BaseExtractor(Protocol):
    """Protocol for data extractors."""

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract data from parsed FEC file."""
        ...


# =============================================================================
# Standard Statistics Extractors
# =============================================================================


class MaxedDonorsExtractor:
    """A. Extract donors who have reached the contribution limit ($3,500)."""

    def __init__(self, limit: float = MAX_CONTRIBUTION_LIMIT) -> None:
        self.limit = limit

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract maxed-out donors from contributions."""
        maxed_donors: list[MaxedDonor] = []
        total_individual_contributions = 0.0

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()

            if not form_type.startswith("SA11AI"):
                continue

            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            aggregate = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AGGREGATE))

            total_individual_contributions += amount

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

        unique_donors = self._deduplicate_donors(maxed_donors)
        total_from_maxed = sum(d.aggregate for d in unique_donors)
        employer_counts = Counter(d.employer for d in unique_donors if d.employer)
        occupation_counts = Counter(d.occupation for d in unique_donors if d.occupation)
        state_counts = Counter(d.state for d in unique_donors if d.state)

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


class GeographyExtractor:
    """B & E. Extract in-state vs out-of-state contribution statistics."""

    def __init__(self, candidate_state: str | None = None) -> None:
        self.candidate_state = candidate_state

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract geographic breakdown of contributions."""
        # Try to determine candidate state from report if not provided
        candidate_state = self.candidate_state or _get_candidate_state(report)

        in_state_total = 0.0
        in_state_count = 0
        out_state_total = 0.0
        out_state_count = 0
        state_totals: dict[str, float] = defaultdict(float)
        state_counts: dict[str, int] = defaultdict(int)
        unknown_state_total = 0.0

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()

            # Only individual contributions
            if not form_type.startswith("SA11AI"):
                continue

            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            state = _get_column(row, ScheduleAColumns.STATE).upper()

            if not state:
                unknown_state_total += amount
                continue

            state_totals[state] += amount
            state_counts[state] += 1

            if candidate_state and state == candidate_state.upper():
                in_state_total += amount
                in_state_count += 1
            else:
                out_state_total += amount
                out_state_count += 1

        total = in_state_total + out_state_total
        in_state_pct = (in_state_total / total * 100) if total > 0 else 0
        out_state_pct = (out_state_total / total * 100) if total > 0 else 0

        # Sort states by total amount
        top_states = sorted(state_totals.items(), key=lambda x: x[1], reverse=True)[:15]

        return ExtractionResult(
            data={
                "candidate_state": candidate_state,
                "top_states": [
                    {"state": s, "total": t, "count": state_counts[s]} for s, t in top_states
                ],
                "state_totals": dict(state_totals),
            },
            stats={
                "in_state_total": in_state_total,
                "in_state_count": in_state_count,
                "in_state_pct": in_state_pct,
                "out_state_total": out_state_total,
                "out_state_count": out_state_count,
                "out_state_pct": out_state_pct,
                "total": total,
                "unknown_state_total": unknown_state_total,
            },
            raw_items=[],
        )


class DonorSizeExtractor:
    """C. Extract small donor vs big donor statistics ($25 threshold)."""

    def __init__(self, threshold: float = SMALL_DONOR_THRESHOLD) -> None:
        self.threshold = threshold

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract small vs large donor breakdown."""
        small_total = 0.0
        small_count = 0
        big_total = 0.0
        big_count = 0

        # Track unique donors for more accurate counts
        small_donors: list[dict] = []
        big_donors: list[dict] = []

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()

            if not form_type.startswith("SA11AI"):
                continue

            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            first = _get_column(row, ScheduleAColumns.FIRST_NAME)
            last = _get_column(row, ScheduleAColumns.LAST_NAME)
            name = _format_name(first, last)

            if amount <= self.threshold:
                small_total += amount
                small_count += 1
                small_donors.append({"name": name, "amount": amount})
            else:
                big_total += amount
                big_count += 1
                big_donors.append({"name": name, "amount": amount})

        total = small_total + big_total
        small_pct = (small_total / total * 100) if total > 0 else 0
        big_pct = (big_total / total * 100) if total > 0 else 0

        return ExtractionResult(
            data={
                "threshold": self.threshold,
            },
            stats={
                "small_total": small_total,
                "small_count": small_count,
                "small_pct": small_pct,
                "big_total": big_total,
                "big_count": big_count,
                "big_pct": big_pct,
                "total": total,
                "total_count": small_count + big_count,
            },
            raw_items=[],
        )


class FundingSourceExtractor:
    """D. Extract funding source statistics (individuals, PACs, parties, etc.)."""

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract breakdown by funding source type."""
        sources: dict[str, dict] = {
            "individuals": {"total": 0.0, "count": 0, "items": []},
            "parties": {"total": 0.0, "count": 0, "items": []},
            "pacs": {"total": 0.0, "count": 0, "items": []},
            "transfers": {"total": 0.0, "count": 0, "items": []},
            "loans": {"total": 0.0, "count": 0, "items": []},
            "other": {"total": 0.0, "count": 0, "items": []},
        }

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()
            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            org_name = _get_column(row, ScheduleAColumns.ORGANIZATION_NAME)
            first = _get_column(row, ScheduleAColumns.FIRST_NAME)
            last = _get_column(row, ScheduleAColumns.LAST_NAME)
            name = org_name or _format_name(first, last)

            item = {"name": name, "amount": amount, "form_type": form_type}

            if form_type.startswith(INDIVIDUAL_CONTRIBUTION_TYPES):
                sources["individuals"]["total"] += amount
                sources["individuals"]["count"] += 1
            elif form_type.startswith(PARTY_CONTRIBUTION_TYPES):
                sources["parties"]["total"] += amount
                sources["parties"]["count"] += 1
                sources["parties"]["items"].append(item)
            elif form_type.startswith(PAC_CONTRIBUTION_TYPES):
                sources["pacs"]["total"] += amount
                sources["pacs"]["count"] += 1
                sources["pacs"]["items"].append(item)
            elif form_type.startswith(TRANSFER_TYPES):
                sources["transfers"]["total"] += amount
                sources["transfers"]["count"] += 1
                sources["transfers"]["items"].append(item)
            elif form_type.startswith(LOAN_TYPES):
                sources["loans"]["total"] += amount
                sources["loans"]["count"] += 1
                sources["loans"]["items"].append(item)
            elif form_type.startswith("SA"):
                sources["other"]["total"] += amount
                sources["other"]["count"] += 1

        total = sum(s["total"] for s in sources.values())

        # Calculate percentages
        for source in sources.values():
            source["pct"] = (source["total"] / total * 100) if total > 0 else 0

        return ExtractionResult(
            data={
                "sources": sources,
                "total": total,
            },
            stats={
                "individuals_total": sources["individuals"]["total"],
                "individuals_pct": sources["individuals"]["pct"],
                "individuals_count": sources["individuals"]["count"],
                "pacs_total": sources["pacs"]["total"],
                "pacs_pct": sources["pacs"]["pct"],
                "pacs_count": sources["pacs"]["count"],
                "parties_total": sources["parties"]["total"],
                "parties_pct": sources["parties"]["pct"],
                "transfers_total": sources["transfers"]["total"],
                "transfers_pct": sources["transfers"]["pct"],
                "loans_total": sources["loans"]["total"],
                "loans_pct": sources["loans"]["pct"],
                "other_total": sources["other"]["total"],
                "total": total,
            },
            raw_items=[],
        )


class ExpenditureExtractor:
    """F. Extract interesting or unusual expenditures."""

    def __init__(self, keywords: list[str] | None = None) -> None:
        self.keywords = keywords or INTERESTING_EXPENDITURE_KEYWORDS

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract expenditures flagged as potentially interesting."""
        flagged: list[Expenditure] = []
        total_expenditures = 0.0
        expenditure_categories: dict[str, float] = defaultdict(float)

        # Compile regex patterns for efficiency
        patterns = [re.compile(kw, re.IGNORECASE) for kw in self.keywords]

        for row in parsed.disbursements:
            form_type = _get_column(row, ScheduleBColumns.FORM_TYPE).upper()
            amount = _parse_currency(_get_column(row, ScheduleBColumns.EXPENDITURE_AMOUNT))
            purpose = _get_column(row, ScheduleBColumns.PURPOSE_DESCRIPTION)
            category = _get_column(row, ScheduleBColumns.CATEGORY_CODE)
            org_name = _get_column(row, ScheduleBColumns.PAYEE_ORG_NAME)
            first = _get_column(row, ScheduleBColumns.PAYEE_FIRST_NAME)
            last = _get_column(row, ScheduleBColumns.PAYEE_LAST_NAME)
            payee = org_name or _format_name(first, last)
            date = _parse_date(_get_column(row, ScheduleBColumns.EXPENDITURE_DATE)) or ""
            city = _get_column(row, ScheduleBColumns.PAYEE_CITY)
            state = _get_column(row, ScheduleBColumns.PAYEE_STATE)

            total_expenditures += amount

            # Track by category
            if category:
                expenditure_categories[category] += amount

            # Check for interesting keywords
            text_to_check = f"{purpose} {payee}".lower()
            matched_keywords = []
            for pattern in patterns:
                if pattern.search(text_to_check):
                    matched_keywords.append(pattern.pattern)

            if matched_keywords:
                flagged.append(
                    Expenditure(
                        payee=payee,
                        amount=amount,
                        date=date,
                        purpose=purpose,
                        category=category,
                        city=city,
                        state=state,
                        form_type=form_type,
                    )
                )

        # Sort flagged by amount descending
        flagged.sort(key=lambda x: x.amount, reverse=True)

        return ExtractionResult(
            data={
                "flagged_expenditures": [
                    {
                        "payee": e.payee,
                        "amount": e.amount,
                        "date": e.date,
                        "purpose": e.purpose,
                        "category": e.category,
                        "city": e.city,
                        "state": e.state,
                    }
                    for e in flagged
                ],
                "categories": dict(expenditure_categories),
                "keywords_used": self.keywords,
            },
            stats={
                "flagged_count": len(flagged),
                "flagged_total": sum(e.amount for e in flagged),
                "total_expenditures": total_expenditures,
                "flagged_pct": (
                    sum(e.amount for e in flagged) / total_expenditures * 100
                    if total_expenditures > 0
                    else 0
                ),
            },
            raw_items=[
                {
                    "payee": e.payee,
                    "amount": e.amount,
                    "date": e.date,
                    "purpose": e.purpose,
                }
                for e in flagged
            ],
        )


# =============================================================================
# Detailed Analysis Extractors (for AI interpretation)
# =============================================================================


class IndustryExtractor:
    """Extract employer/industry breakdown for AI analysis."""

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract contributions grouped by employer and occupation (proxy for industry)."""
        employer_totals: dict[str, dict] = defaultdict(
            lambda: {"total": 0.0, "count": 0, "donors": []}
        )
        occupation_totals: dict[str, dict] = defaultdict(lambda: {"total": 0.0, "count": 0})

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()

            if not form_type.startswith("SA11AI"):
                continue

            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            employer = _get_column(row, ScheduleAColumns.EMPLOYER)
            occupation = _get_column(row, ScheduleAColumns.OCCUPATION)
            first = _get_column(row, ScheduleAColumns.FIRST_NAME)
            last = _get_column(row, ScheduleAColumns.LAST_NAME)
            name = _format_name(first, last)

            if employer:
                employer_key = employer.upper().strip()
                employer_totals[employer_key]["total"] += amount
                employer_totals[employer_key]["count"] += 1
                employer_totals[employer_key]["donors"].append(
                    {"name": name, "amount": amount, "occupation": occupation}
                )

            if occupation:
                occupation_key = occupation.upper().strip()
                occupation_totals[occupation_key]["total"] += amount
                occupation_totals[occupation_key]["count"] += 1

        # Sort by total and get top entries
        top_employers = sorted(
            [(k, v) for k, v in employer_totals.items()],
            key=lambda x: x[1]["total"],
            reverse=True,
        )[:25]

        top_occupations = sorted(
            [(k, v) for k, v in occupation_totals.items()],
            key=lambda x: x[1]["total"],
            reverse=True,
        )[:25]

        # Find employers with multiple donors (potential company giving)
        multi_donor_employers = [(k, v) for k, v in employer_totals.items() if v["count"] >= 2]
        multi_donor_employers.sort(key=lambda x: x[1]["total"], reverse=True)

        return ExtractionResult(
            data={
                "top_employers": [
                    {
                        "employer": k,
                        "total": v["total"],
                        "count": v["count"],
                        "donors": v["donors"][:10],  # Limit donors per employer
                    }
                    for k, v in top_employers
                ],
                "top_occupations": [
                    {"occupation": k, "total": v["total"], "count": v["count"]}
                    for k, v in top_occupations
                ],
                "multi_donor_employers": [
                    {
                        "employer": k,
                        "total": v["total"],
                        "count": v["count"],
                        "donors": v["donors"],
                    }
                    for k, v in multi_donor_employers[:15]
                ],
            },
            stats={
                "unique_employers": len(employer_totals),
                "unique_occupations": len(occupation_totals),
                "multi_donor_employer_count": len(multi_donor_employers),
            },
            raw_items=[],
        )


class GroupedDonationsExtractor:
    """Extract donations that may indicate fundraising events."""

    def extract(self, parsed: ParsedFECFile, report: Filings) -> ExtractionResult:
        """Extract donations grouped by date, location, or employer patterns."""
        contributions: list[Contribution] = []

        for row in parsed.contributions:
            form_type = _get_column(row, ScheduleAColumns.FORM_TYPE).upper()

            if not form_type.startswith("SA11AI"):
                continue

            amount = _parse_currency(_get_column(row, ScheduleAColumns.CONTRIBUTION_AMOUNT))
            first = _get_column(row, ScheduleAColumns.FIRST_NAME)
            last = _get_column(row, ScheduleAColumns.LAST_NAME)
            date_str = _get_column(row, ScheduleAColumns.CONTRIBUTION_DATE)
            date = _parse_date(date_str) or date_str

            contributions.append(
                Contribution(
                    name=_format_name(first, last),
                    employer=_get_column(row, ScheduleAColumns.EMPLOYER),
                    occupation=_get_column(row, ScheduleAColumns.OCCUPATION),
                    amount=amount,
                    aggregate=_parse_currency(
                        _get_column(row, ScheduleAColumns.CONTRIBUTION_AGGREGATE)
                    ),
                    state=_get_column(row, ScheduleAColumns.STATE),
                    city=_get_column(row, ScheduleAColumns.CITY),
                    date=date,
                    form_type=form_type,
                    entity_type=_get_column(row, ScheduleAColumns.ENTITY_TYPE),
                )
            )

        # Group by date
        by_date: dict[str, list[Contribution]] = defaultdict(list)
        for c in contributions:
            if c.date:
                by_date[c.date].append(c)

        # Find dates with significant activity (5+ donations)
        significant_dates = [
            (date, contribs) for date, contribs in by_date.items() if len(contribs) >= 5
        ]
        significant_dates.sort(key=lambda x: sum(c.amount for c in x[1]), reverse=True)

        # Group by city+date (potential events)
        by_city_date: dict[str, list[Contribution]] = defaultdict(list)
        for c in contributions:
            if c.city and c.date:
                key = f"{c.city.upper()}, {c.state}|{c.date}"
                by_city_date[key].append(c)

        potential_events = [
            (key, contribs) for key, contribs in by_city_date.items() if len(contribs) >= 3
        ]
        potential_events.sort(key=lambda x: sum(c.amount for c in x[1]), reverse=True)

        # Group by employer+date (corporate events)
        by_employer_date: dict[str, list[Contribution]] = defaultdict(list)
        for c in contributions:
            if c.employer and c.date:
                key = f"{c.employer.upper()}|{c.date}"
                by_employer_date[key].append(c)

        employer_events = [
            (key, contribs) for key, contribs in by_employer_date.items() if len(contribs) >= 3
        ]
        employer_events.sort(key=lambda x: sum(c.amount for c in x[1]), reverse=True)

        return ExtractionResult(
            data={
                "significant_dates": [
                    {
                        "date": date,
                        "count": len(contribs),
                        "total": sum(c.amount for c in contribs),
                        "donations": [
                            {
                                "name": c.name,
                                "amount": c.amount,
                                "employer": c.employer,
                                "city": c.city,
                                "state": c.state,
                            }
                            for c in contribs[:20]
                        ],
                    }
                    for date, contribs in significant_dates[:10]
                ],
                "potential_events": [
                    {
                        "location": key.split("|")[0],
                        "date": key.split("|")[1],
                        "count": len(contribs),
                        "total": sum(c.amount for c in contribs),
                        "donations": [
                            {"name": c.name, "amount": c.amount, "employer": c.employer}
                            for c in contribs
                        ],
                    }
                    for key, contribs in potential_events[:10]
                ],
                "employer_events": [
                    {
                        "employer": key.split("|")[0],
                        "date": key.split("|")[1],
                        "count": len(contribs),
                        "total": sum(c.amount for c in contribs),
                        "donations": [{"name": c.name, "amount": c.amount} for c in contribs],
                    }
                    for key, contribs in employer_events[:10]
                ],
            },
            stats={
                "total_contributions": len(contributions),
                "significant_date_count": len(significant_dates),
                "potential_event_count": len(potential_events),
                "employer_event_count": len(employer_events),
            },
            raw_items=[],
        )
