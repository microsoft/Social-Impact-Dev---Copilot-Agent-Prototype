"""Email services and templates."""

from .service import (
    AzureEmailService,
    EmailMessage,
    EmailResult,
    EmailService,
)
from .templates import (
    build_report_html,
    build_report_plain_text,
    build_report_preview_html,
)
from .utils import format_date, format_period

__all__ = [
    "AzureEmailService",
    "EmailMessage",
    "EmailResult",
    "EmailService",
    "build_report_html",
    "build_report_plain_text",
    "build_report_preview_html",
    "format_date",
    "format_period",
]
