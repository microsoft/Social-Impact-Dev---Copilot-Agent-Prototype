"""F3 form CSV dataclass."""

from __future__ import annotations

from dataclasses import dataclass, field

from ..base import Section, SectionName
from ..constants import HDR_COLUMNS, HDR_HEADERS
from .columns import (
    F3_COLUMNS,
    F3_FORM_TYPE_HEADERS,
    SCHEDULE_A_COLUMNS,
    SCHEDULE_A_HEADERS,
    SCHEDULE_B_COLUMNS,
    SCHEDULE_B_HEADERS,
)


@dataclass
class F3CSV:
    """Parsed FEC F3 form CSV with records grouped by type.

    F3 is used for House and Senate campaign reports.

    Attributes:
        version: FEC e-filing format version (e.g., "8.5").
        header: HDR record containing file metadata.
        summary: F3 summary record with financial totals.
        contributions: Schedule A records (itemized receipts).
        disbursements: Schedule B records (itemized expenditures).
        other: Any other record types not categorized above.
        all_rows: All rows in original order for raw export.
    """

    version: str
    header: list[str]
    summary: list[str]
    contributions: list[list[str]] = field(default_factory=list)
    disbursements: list[list[str]] = field(default_factory=list)
    other: list[list[str]] = field(default_factory=list)
    all_rows: list[list[str]] = field(default_factory=list)

    @property
    def form_type(self) -> str:
        """The base form type code."""
        return "F3"

    def get_sections(self) -> list[Section]:
        """Get all sections with their headers and column definitions."""
        sections: list[Section] = []

        if self.summary:
            headers = _get_headers_for_record_type(self.summary[0])
            trimmed_headers = headers[: len(self.summary)] if headers else []
            trimmed_columns = F3_COLUMNS[: len(self.summary)]
            sections.append(
                Section(
                    name="Summary",
                    headers=trimmed_headers,
                    columns=trimmed_columns,
                    rows=[self.summary],
                )
            )

        if self.contributions:
            padded_rows = [_pad_row(row, SCHEDULE_A_HEADERS) for row in self.contributions]
            sections.append(
                Section(
                    name="Contributions",
                    headers=SCHEDULE_A_HEADERS,
                    columns=SCHEDULE_A_COLUMNS,
                    rows=padded_rows,
                )
            )

        if self.disbursements:
            padded_rows = [_pad_row(row, SCHEDULE_B_HEADERS) for row in self.disbursements]
            sections.append(
                Section(
                    name="Disbursements",
                    headers=SCHEDULE_B_HEADERS,
                    columns=SCHEDULE_B_COLUMNS,
                    rows=padded_rows,
                )
            )

        return sections

    def get_header_section(self) -> Section | None:
        """Get the HDR section if present."""
        if self.header:
            trimmed_headers = HDR_HEADERS[: len(self.header)]
            trimmed_columns = HDR_COLUMNS[: len(self.header)]
            return Section(
                name="Header",
                headers=trimmed_headers,
                columns=trimmed_columns,
                rows=[self.header],
            )
        return None

    def get_section_rows(self, name: SectionName) -> list[list[str]]:
        """Get rows for a named section."""
        if name == "Summary":
            return [self.summary] if self.summary else []
        if name == "Contributions":
            return self.contributions
        if name == "Disbursements":
            return self.disbursements
        if name == "Header":
            return [self.header] if self.header else []
        return []


def _get_headers_for_record_type(record_type: str) -> list[str]:
    """Get the appropriate headers for a record type prefix."""
    record_type_upper = record_type.upper().strip('"')

    if record_type_upper in F3_FORM_TYPE_HEADERS:
        return F3_FORM_TYPE_HEADERS[record_type_upper]

    for prefix, headers in F3_FORM_TYPE_HEADERS.items():
        if record_type_upper.startswith(prefix):
            return headers

    return []


def _pad_row(row: list[str], headers: list[str]) -> list[str]:
    """Pad a row to match the number of headers."""
    if len(row) < len(headers):
        return row + [""] * (len(headers) - len(row))
    return row[: len(headers)]
