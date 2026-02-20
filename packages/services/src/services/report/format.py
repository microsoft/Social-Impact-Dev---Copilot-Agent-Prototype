"""FEC CSV processing and Excel formatting service."""

from __future__ import annotations

import csv
import io
from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from openpyxl.worksheet.worksheet import Worksheet

from .constants import (
    F3_COLUMNS,
    FORM_TYPE_HEADERS,
    HDR_COLUMNS,
    HDR_HEADERS,
    SCHEDULE_A_COLUMNS,
    SCHEDULE_A_HEADERS,
    SCHEDULE_B_COLUMNS,
    SCHEDULE_B_HEADERS,
    HeaderDef,
)


@dataclass
class Section:
    """A section of FEC data with headers and rows."""

    name: str
    headers: list[str]
    columns: list[HeaderDef]
    rows: list[list[str]]


@dataclass
class ParsedQuarterlyCSV:
    """Parsed FEC quarterly report CSV with records grouped by type.

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

    def get_sections(self) -> list[Section]:
        """Get all sections with their headers and column definitions.

        Returns:
            List of Section objects for Summary, Contributions, and Disbursements.
        """
        sections: list[Section] = []

        if self.summary:
            headers = _get_headers_for_form_type(self.summary[0])
            # Trim headers/columns to match actual data length
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


def _get_headers_for_form_type(form_type: str) -> list[str]:
    """Get the appropriate headers for a form type."""
    form_type_upper = form_type.upper().strip('"')

    # Check exact match first
    if form_type_upper in FORM_TYPE_HEADERS:
        return FORM_TYPE_HEADERS[form_type_upper]

    # Check prefix match (e.g., SA11AI -> SA, SB17 -> SB, F3N -> F3)
    for prefix, headers in FORM_TYPE_HEADERS.items():
        if form_type_upper.startswith(prefix):
            return headers

    return []


def _pad_row(row: list[str], headers: list[str]) -> list[str]:
    """Pad a row to match the number of headers."""
    if len(row) < len(headers):
        return row + [""] * (len(headers) - len(row))
    return row[: len(headers)]


def parse_fec_csv(content: bytes | str) -> ParsedQuarterlyCSV:
    """Parse an FEC CSV file and categorize records by type.

    Args:
        content: Raw CSV content as bytes or string.

    Returns:
        ParsedQuarterlyCSV with records grouped by type.
    """
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")

    reader = csv.reader(io.StringIO(content))
    rows = list(reader)

    result = ParsedQuarterlyCSV(
        version="",
        header=[],
        summary=[],
    )

    for row in rows:
        if not row:
            continue

        result.all_rows.append(row)
        form_type = row[0].strip('"').upper()

        if form_type == "HDR":
            result.header = row
            # Extract version (typically in column 3)
            if len(row) > 2:
                result.version = row[2].strip('"')
        elif form_type.startswith("F3"):
            result.summary = row
        elif form_type.startswith("SA"):
            result.contributions.append(row)
        elif form_type.startswith("SB"):
            result.disbursements.append(row)
        else:
            result.other.append(row)

    return result


def add_headers_to_csv(content: bytes | str | ParsedQuarterlyCSV) -> str:
    """Add headers to an FEC CSV file.

    Creates a CSV where each record type section has its appropriate headers.

    Args:
        content: Raw FEC CSV content or pre-parsed ParsedQuarterlyCSV.

    Returns:
        CSV string with headers added for each section.
    """
    parsed = content if isinstance(content, ParsedQuarterlyCSV) else parse_fec_csv(content)
    output = io.StringIO()
    writer = csv.writer(output)

    # Write header record
    hdr_section = parsed.get_header_section()
    if hdr_section:
        writer.writerow(hdr_section.headers)
        for row in hdr_section.rows:
            writer.writerow(row)
        writer.writerow([])

    # Write main sections
    for section in parsed.get_sections():
        writer.writerow(section.headers)
        for row in section.rows:
            writer.writerow(row)
        writer.writerow([])

    # Write other records
    if parsed.other:
        writer.writerow(["form_type", "data..."])
        for row in parsed.other:
            writer.writerow(row)

    return output.getvalue()


def create_xlsx(content: bytes | str | ParsedQuarterlyCSV) -> bytes:
    """Convert FEC CSV to XLSX with multiple sheets.

    Creates an Excel workbook with:
    - "Summary" sheet: Filing summary (F3 record)
    - "Contributions" sheet: All Schedule A records with headers
    - "Disbursements" sheet: All Schedule B records with headers

    Args:
        content: Raw FEC CSV content or pre-parsed ParsedQuarterlyCSV.

    Returns:
        XLSX file as bytes.
    """
    try:
        import openpyxl
    except ImportError as e:
        raise ImportError(
            "openpyxl is required for XLSX export. Install with: pip install openpyxl"
        ) from e

    parsed = content if isinstance(content, ParsedQuarterlyCSV) else parse_fec_csv(content)
    wb = openpyxl.Workbook()
    formatter = FormatService()

    # Remove default sheet, we'll add our own
    wb.remove(wb.active)

    # Create sheets from sections
    for section in parsed.get_sections():
        ws = wb.create_sheet(section.name)
        ws.append(section.headers)
        for row in section.rows:
            ws.append(row)
        formatter.format_sheet(ws, section.columns)

    # Save to bytes
    output = io.BytesIO()
    wb.save(output)
    return output.getvalue()


class FormatService:
    """Service for formatting Excel worksheets based on FEC column types."""

    def __init__(
        self,
        *,
        header_color: str = "4472C4",
        header_font_color: str = "FFFFFF",
        min_col_width: int = 12,
        max_col_width: int = 50,
    ) -> None:
        """Initialize the format service.

        Args:
            header_color: Background color for header row (hex).
            header_font_color: Font color for header row (hex).
            min_col_width: Minimum column width in characters.
            max_col_width: Maximum column width in characters.
        """
        self.header_color = header_color
        self.header_font_color = header_font_color
        self.min_col_width = min_col_width
        self.max_col_width = max_col_width

    def format_sheet(self, ws: Worksheet, columns: list[HeaderDef] | None = None) -> None:
        """Format a worksheet with header styling and auto-width columns.

        Args:
            ws: The openpyxl worksheet to format.
            columns: Unused, kept for API compatibility.
        """
        self._format_header_row(ws)
        self._auto_width_columns(ws)

    def _format_header_row(self, ws: Worksheet) -> None:
        """Format the first row as a header with styling and auto-filter."""
        try:
            from openpyxl.styles import Alignment, Font, PatternFill
            from openpyxl.utils import get_column_letter
        except ImportError:
            return

        header_fill = PatternFill(
            start_color=self.header_color,
            end_color=self.header_color,
            fill_type="solid",
        )
        header_font = Font(bold=True, color=self.header_font_color)

        for cell in ws[1]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center", wrap_text=True)

        # Freeze header row
        ws.freeze_panes = "A2"

        # Add auto-filter for sorting
        if ws.max_column > 0 and ws.max_row > 1:
            last_col = get_column_letter(ws.max_column)
            ws.auto_filter.ref = f"A1:{last_col}{ws.max_row}"

    def _auto_width_columns(self, ws: Worksheet) -> None:
        """Auto-size columns based on content."""
        try:
            from openpyxl.utils import get_column_letter
        except ImportError:
            return

        for col_idx, column_cells in enumerate(ws.columns, 1):
            max_length = 0
            column_cells_list = list(column_cells)

            for cell in column_cells_list:
                try:
                    if cell.value:
                        max_length = max(max_length, len(str(cell.value)))
                except Exception:
                    pass

            # Apply min/max constraints with padding
            adjusted_width = max(
                min(max_length + 3, self.max_col_width),
                self.min_col_width,
            )
            ws.column_dimensions[get_column_letter(col_idx)].width = adjusted_width
