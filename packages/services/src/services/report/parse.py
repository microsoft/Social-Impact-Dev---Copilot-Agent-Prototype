"""FEC CSV parsing dispatcher."""

from __future__ import annotations

from .base import FormCSV
from .constants import SUPPORTED_FORM_TYPES, is_supported_form_type
from .f3 import parse_f3


def parse_fec_csv(content: bytes | str, form_type: str | None = None) -> FormCSV:
    """Parse an FEC CSV file and categorize records by type.

    Routes to the appropriate form-specific parser based on form_type.

    Args:
        content: Raw CSV content as bytes or string.
        form_type: Form type code (e.g., 'F3', 'F3A'). Required to select parser.

    Returns:
        Parsed form CSV implementing FormCSV protocol.

    Raises:
        ValueError: If form_type is not provided or not supported.
    """
    if not form_type:
        raise ValueError("form_type is required to parse FEC CSV")

    if not is_supported_form_type(form_type):
        raise ValueError(
            f"Form type '{form_type}' is not supported. "
            f"Supported form types: {', '.join(sorted(SUPPORTED_FORM_TYPES))}"
        )

    # Route to appropriate parser based on form type
    # Currently only F3 is supported; add F3X, F3P, etc. as needed
    return parse_f3(content)
