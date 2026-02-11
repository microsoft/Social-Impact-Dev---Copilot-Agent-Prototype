"""Shared utilities for services."""

from __future__ import annotations

from datetime import datetime


def parse_comma_list(value: str | None) -> list[str]:
    """Parse comma-separated string into list of stripped values.

    Args:
        value: Comma-separated string, or None/empty string.

    Returns:
        List of non-empty stripped values. Empty list if input is None/empty.
    """
    if not value:
        return []
    return [v.strip() for v in value.split(",") if v.strip()]


def format_date(date_str: str | None) -> str:
    """Format a date string to a readable format (e.g., 'January 15, 2024').

    Handles various input formats:
    - ISO format: 2024-01-15T00:00:00+00:00
    - Date only: 2024-01-15
    - FEC format: 20240115

    Args:
        date_str: Date string in various formats.

    Returns:
        Human-readable date string (e.g., "January 15, 2024"), or "Unknown" if None.
    """
    if not date_str:
        return "Unknown"

    # Try parsing different formats
    formats_to_try = [
        "%Y-%m-%dT%H:%M:%S%z",  # ISO with timezone
        "%Y-%m-%dT%H:%M:%S",  # ISO without timezone
        "%Y-%m-%d",  # Date only
        "%Y%m%d",  # FEC format (YYYYMMDD)
    ]

    # Handle timezone suffix like +00:00
    clean_date = date_str.replace("+00:00", "").replace("Z", "")

    for fmt in formats_to_try:
        try:
            dt = datetime.strptime(clean_date[: len("2024-01-15T00:00:00")], fmt)
            return dt.strftime("%B %d, %Y")  # e.g., "January 15, 2024"
        except ValueError:
            continue

    # If all parsing fails, return the original
    return date_str


def format_period(start_date: str | None, end_date: str | None) -> str:
    """Format coverage period dates.

    Args:
        start_date: Period start date.
        end_date: Period end date.

    Returns:
        Formatted period string (e.g., "January 01, 2024 to March 31, 2024").
    """
    start = format_date(start_date)
    end = format_date(end_date)
    return f"{start} to {end}"
