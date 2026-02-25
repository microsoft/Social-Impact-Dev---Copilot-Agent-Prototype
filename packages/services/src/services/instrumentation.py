"""Instrumentation utilities for tracking operation metrics.

Provides timing and metrics tracking that integrates with Application Insights
via structured logging with custom dimensions.
"""

from __future__ import annotations

import logging
import time
from contextlib import contextmanager
from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any

logger = logging.getLogger(__name__)


class Operation(StrEnum):
    """Operation names for instrumentation metrics."""

    # Sync operations
    SYNC_REPORTS = "sync_reports"
    DOWNLOAD_CSV = "download_csv"
    FORMAT_AND_SAVE_CSV = "format_and_save_csv"
    CREATE_AND_SAVE_XLSX = "create_and_save_xlsx"
    SAVE_REPORT = "save_report"

    # Email operations
    SEND_REPORT_EMAIL = "send_report_email"
    GENERATE_EMAIL_CONTENT = "generate_email_content"
    SEND_EMAIL = "send_email"

    # Analysis operations
    RUN_FULL_ANALYSIS = "run_full_analysis"
    ANALYSIS_EXTRACTION = "analysis_extraction"
    ANALYSIS_STANDARD = "analysis_standard"
    ANALYSIS_AI = "analysis_ai"
    ANALYSIS_MAX_OUT_DONORS = "analysis_max_out_donors"
    ANALYSIS_GEOGRAPHY = "analysis_geography"
    ANALYSIS_DONOR_SIZE = "analysis_donor_size"
    ANALYSIS_FUNDING_SOURCES = "analysis_funding_sources"
    ANALYSIS_INDUSTRY = "analysis_industry"
    ANALYSIS_UNUSUAL_EXPENDITURES = "analysis_unusual_expenditures"
    ANALYSIS_GROUPED_DONATIONS = "analysis_grouped_donations"
    ANALYSIS_SUMMARY = "analysis_summary"


@dataclass
class OperationMetrics:
    """Metrics collected for an operation."""

    operation: str
    duration_ms: float
    success: bool = True
    record_count: int | None = None
    input_size_bytes: int | None = None
    output_size_bytes: int | None = None
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
        if self.input_size_bytes is not None:
            result["input_size_bytes"] = self.input_size_bytes
        if self.output_size_bytes is not None:
            result["output_size_bytes"] = self.output_size_bytes
        result.update(self.extra)
        return result

    def _format_size(self, size_bytes: int) -> str:
        """Format bytes as human-readable string."""
        if size_bytes >= 1024 * 1024:
            return f"{size_bytes / (1024 * 1024):.1f}MB"
        elif size_bytes >= 1024:
            return f"{size_bytes / 1024:.1f}KB"
        return f"{size_bytes}B"


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
        metrics_dict = metrics.to_dict()

        # Build log message with optional size info
        msg_parts = [f"[METRICS] {operation}: {metrics.duration_ms:.1f}ms"]
        if metrics.record_count:
            msg_parts.append(f"({metrics.record_count} records)")
        if metrics.input_size_bytes is not None:
            msg_parts.append(f"in={metrics._format_size(metrics.input_size_bytes)}")
        if metrics.output_size_bytes is not None:
            msg_parts.append(f"out={metrics._format_size(metrics.output_size_bytes)}")

        logger.log(
            log_level,
            " ".join(msg_parts),
            extra={"custom_dimensions": metrics_dict},
        )


