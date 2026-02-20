"""Instrumentation utilities for tracking operation metrics.

Provides timing and metrics tracking that integrates with Application Insights
via structured logging with custom dimensions.
"""

from __future__ import annotations

import logging
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class OperationMetrics:
    """Metrics collected for an operation."""

    operation: str
    duration_ms: float
    success: bool = True
    record_count: int | None = None
    extra: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        """Convert to dictionary for logging."""
        result = {
            "operation": self.operation,
            "duration_ms": round(self.duration_ms, 2),
            "success": self.success,
        }
        if self.record_count is not None:
            result["record_count"] = self.record_count
        result.update(self.extra)
        return result


@contextmanager
def track_operation(operation: str, **extra: Any):
    """Context manager to track operation timing and log metrics.

    Usage:
        with track_operation("sync_reports") as metrics:
            # do work
            metrics.record_count = 5
            metrics.extra["committee_id"] = "C00123"

    Args:
        operation: Name of the operation being tracked.
        **extra: Additional fields to include in the metrics.

    Yields:
        OperationMetrics object that can be updated during the operation.
    """
    metrics = OperationMetrics(operation=operation, duration_ms=0, extra=extra)
    start_time = time.perf_counter()

    try:
        yield metrics
        metrics.success = True
    except Exception:
        metrics.success = False
        raise
    finally:
        elapsed = time.perf_counter() - start_time
        metrics.duration_ms = elapsed * 1000

        log_level = logging.INFO if metrics.success else logging.WARNING
        logger.log(
            log_level,
            f"Operation completed: {operation}",
            extra={"custom_dimensions": metrics.to_dict()},
        )


def log_metrics(operation: str, duration_ms: float, **kwargs: Any) -> None:
    """Log operation metrics directly without context manager.

    Args:
        operation: Name of the operation.
        duration_ms: Duration in milliseconds.
        **kwargs: Additional metrics (record_count, success, etc.)
    """
    metrics = OperationMetrics(
        operation=operation,
        duration_ms=duration_ms,
        success=kwargs.pop("success", True),
        record_count=kwargs.pop("record_count", None),
        extra=kwargs,
    )

    log_level = logging.INFO if metrics.success else logging.WARNING
    logger.log(
        log_level,
        f"Operation completed: {operation}",
        extra={"custom_dimensions": metrics.to_dict()},
    )
