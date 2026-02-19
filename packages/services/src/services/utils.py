"""Shared utilities for services."""

from __future__ import annotations


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
