"""Shared utilities for services."""

from __future__ import annotations

import math


def round_percentages(percentages: dict[str, float], decimals: int = 1) -> dict[str, float]:
    """Round percentages to ensure they sum to 100% using largest remainder method.

    This prevents display issues where rounded percentages don't add up to 100%
    (e.g., 13.0% + 0.3% + 86.6% = 99.9%).

    Also clamps values to [0, 100] range to handle edge cases with refunds.

    Args:
        percentages: Dictionary of {name: percentage} values.
        decimals: Number of decimal places to round to (default 1).

    Returns:
        Dictionary with same keys but adjusted values that sum to 100%.
    """
    if not percentages:
        return {}

    # Clamp values to [0, 100] range first
    clamped = {k: min(100, max(0, v)) for k, v in percentages.items()}

    # Filter out zero values for the algorithm
    positive = {k: v for k, v in clamped.items() if v > 0}
    if not positive:
        return {k: 0.0 for k in percentages}

    # If clamped sum doesn't equal 100, use clamped values directly
    # (this happens when refunds cause negative totals)
    clamped_sum = sum(positive.values())
    if abs(clamped_sum - 100) > 0.5:
        # Just round each value individually, don't try to make them sum to 100
        multiplier = 10**decimals
        result = {k: 0.0 for k in percentages}
        for k, v in positive.items():
            result[k] = round(v * multiplier) / multiplier
        return result

    multiplier = 10**decimals
    target = 100 * multiplier  # e.g., 1000 for 1 decimal place

    # Scale and floor each value
    floored = {k: math.floor(v * multiplier) for k, v in positive.items()}
    remainders = {k: (v * multiplier) - floored[k] for k, v in positive.items()}

    # Calculate how much we need to distribute
    current_sum = sum(floored.values())
    remainder_to_distribute = int(target - current_sum)

    # Sort by remainder (descending) and distribute
    sorted_keys = sorted(remainders.keys(), key=lambda k: remainders[k], reverse=True)
    for i in range(min(remainder_to_distribute, len(sorted_keys))):
        floored[sorted_keys[i]] += 1

    # Convert back to percentages and include zero values
    result = {k: 0.0 for k in percentages}
    for k, v in floored.items():
        result[k] = v / multiplier

    return result


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
