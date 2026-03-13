"""Shared constants for FEC report processing.

FEC Electronic Filing Format v8.5
See: https://www.fec.gov/campaign-finance-data/e-filing-parse-tool/
Column definitions source: https://github.com/newsdev/fec-csv-sources
"""

from typing import Literal

from fec_api_client.types import ReportTypeCode, get_base_form_type

ColumnType = Literal["text", "currency", "date", "id"]
HeaderDef = tuple[str, ColumnType]

# Report type sets
QUARTERLY_REPORT_TYPES: set[ReportTypeCode] = {"Q1", "Q2", "Q3", "YE"}
MONTHLY_REPORT_TYPES: set[ReportTypeCode] = {
    "M1",
    "M2",
    "M3",
    "M4",
    "M5",
    "M6",
    "M7",
    "M8",
    "M9",
    "M10",
    "M11",
    "M12",
}

# Form type sets
F3_FORM_TYPES: set[str] = {"F3"}
F3X_FORM_TYPES: set[str] = {"F3X"}

# Currently supported types
SUPPORTED_REPORT_TYPES = frozenset(QUARTERLY_REPORT_TYPES)
SUPPORTED_FORM_TYPES = frozenset(F3_FORM_TYPES)


def is_supported_report_type(report_type: str | None) -> bool:
    """Check if a report type is supported for syncing."""
    return report_type in SUPPORTED_REPORT_TYPES if report_type else False


def is_supported_form_type(form_type: str | None) -> bool:
    """Check if a form type is supported for CSV parsing."""
    base_type = get_base_form_type(form_type)
    return base_type in SUPPORTED_FORM_TYPES if base_type else False


def get_unsupported_form_notice(form_type: str | None) -> str | None:
    """Get a notice message if form type is not supported, otherwise None."""
    if is_supported_form_type(form_type):
        return None
    return (
        f"This report uses form type {form_type}, which is not yet supported "
        f"for detailed AI analysis. Only basic filing information is shown."
    )


# HDR columns (shared across all form types)
HDR_COLUMNS: list[HeaderDef] = [
    ("Record Type", "text"),
    ("EF Type", "text"),
    ("FEC Version", "text"),
    ("Software Name", "text"),
    ("Software Version", "text"),
    ("Name Delimiter", "text"),
    ("Report ID", "id"),
    ("Report Number", "text"),
    ("Comment", "text"),
]

HDR_HEADERS: list[str] = [col[0] for col in HDR_COLUMNS]
