"""F3 form CSV parsing."""

from __future__ import annotations

import csv
import io

from .csv import F3CSV


def parse_f3(content: bytes | str) -> F3CSV:
    """Parse an FEC F3 CSV file and categorize records by type.

    Args:
        content: Raw CSV content as bytes or string.

    Returns:
        F3CSV with records grouped by type.
    """
    if isinstance(content, bytes):
        content = content.decode("utf-8", errors="replace")

    reader = csv.reader(io.StringIO(content))
    rows = list(reader)

    result = F3CSV(
        version="",
        header=[],
        summary=[],
    )

    for row in rows:
        if not row:
            continue

        result.all_rows.append(row)
        record_type = row[0].strip('"').upper()

        if record_type == "HDR":
            result.header = row
            if len(row) > 2:
                result.version = row[2].strip('"')
        elif record_type.startswith("F3"):
            result.summary = row
        elif record_type.startswith("SA"):
            result.contributions.append(row)
        elif record_type.startswith("SB"):
            result.disbursements.append(row)
        else:
            result.other.append(row)

    return result
