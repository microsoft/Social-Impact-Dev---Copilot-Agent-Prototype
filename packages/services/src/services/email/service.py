from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, Protocol

from azure.communication.email import EmailClient
from azure.identity import DefaultAzureCredential
from fec_api_client import format_report_type

from ..instrumentation import Operation, track_operation
from .templates import (
    build_report_html,
    build_report_plain_text,
)

if TYPE_CHECKING:
    from ..analysis import FullAnalysisResult

logger = logging.getLogger(__name__)


@dataclass
class EmailMessage:
    """Represents an email message to be sent."""

    subject: str
    html_content: str
    plain_text_content: str | None = None


@dataclass
class EmailResult:
    """Result of sending an email."""

    success: bool
    message_id: str | None = None
    error: str | None = None


class EmailService(Protocol):
    """Protocol for email sending services."""

    def send_email(
        self,
        recipients: list[str],
        message: EmailMessage,
    ) -> EmailResult: ...

    def send_report_email(
        self,
        recipients: list[str],
        report: Any,
        summary: str,
        *,
        formatted_csv_url: str | None = None,
        xlsx_url: str | None = None,
        analysis: FullAnalysisResult | None = None,
        notice: str | None = None,
    ) -> EmailResult: ...


class AzureEmailService:
    """Azure Communication Services email sender."""

    def __init__(
        self,
        connection_string: str | None = None,
        endpoint: str | None = None,
        sender_address: str | None = None,
    ) -> None:
        self.connection_string = connection_string or os.getenv("EMAIL_CONNECTION_STRING")
        self.endpoint = endpoint or os.getenv("EMAIL_ENDPOINT")
        self.sender_address = sender_address or os.getenv("EMAIL_SENDER_ADDRESS")

        if not self.sender_address:
            raise ValueError("sender_address or EMAIL_SENDER_ADDRESS must be provided")

        if self.connection_string:
            self._client = EmailClient.from_connection_string(self.connection_string)  # type: ignore[union-attr]
        elif self.endpoint:
            credential = DefaultAzureCredential()
            self._client = EmailClient(self.endpoint, credential)
        else:
            raise ValueError("Either connection_string or endpoint must be provided")

    def send_email(
        self,
        recipients: list[str],
        message: EmailMessage,
    ) -> EmailResult:
        """Send an email to the specified recipients.

        Args:
            recipients: List of email addresses to send to.
            message: The email message to send.

        Returns:
            EmailResult with success status and message ID or error.
        """
        if not recipients:
            return EmailResult(success=False, error="No recipients provided")

        with track_operation(Operation.SEND_EMAIL, recipient_count=len(recipients)) as metrics:
            content: dict[str, str] = {
                "subject": message.subject,
                "html": message.html_content,
            }
            if message.plain_text_content:
                content["plainText"] = message.plain_text_content

            email_message: dict[str, Any] = {
                "senderAddress": self.sender_address,
                "recipients": {
                    "to": [{"address": addr} for addr in recipients],
                },
                "content": content,
            }

            try:
                poller = self._client.begin_send(email_message)
                result = poller.result()
                message_id = result.get("id") if isinstance(result, dict) else str(result)
                logger.info(f"Email sent successfully: {message_id}")
                metrics.extra["message_id"] = message_id
                return EmailResult(success=True, message_id=message_id)
            except Exception as e:
                logger.error(f"Failed to send email: {e}")
                metrics.success = False
                metrics.extra["error"] = str(e)
                return EmailResult(success=False, error=str(e))

    def send_report_email(
        self,
        recipients: list[str],
        report,
        summary: str,
        *,
        formatted_csv_url: str | None = None,
        xlsx_url: str | None = None,
        analysis: FullAnalysisResult | None = None,
        notice: str | None = None,
    ) -> EmailResult:
        """Send an email summarizing a report.

        Args:
            recipients: List of email addresses to send to.
            report: Report (Filings) object with filing details.
            summary: AI-generated summary text.
            formatted_csv_url: Optional URL to formatted CSV with headers.
            xlsx_url: Optional URL to Excel download.
            analysis: Optional full analysis result with all features.
            notice: Optional notice message to display (e.g., unsupported form type).

        Returns:
            EmailResult with success status and message ID or error.
        """
        if not recipients:
            logger.warning("No recipients provided, skipping email")
            return EmailResult(success=False, error="No recipients provided")

        committee_id = getattr(report, "committee_id", None)

        with track_operation(
            Operation.SEND_REPORT_EMAIL,
            committee_id=committee_id,
            recipient_count=len(recipients),
        ) as metrics:
            # Generate email content
            with track_operation(Operation.GENERATE_EMAIL_CONTENT, committee_id=committee_id):
                html_content = build_report_html(
                    report,
                    summary,
                    formatted_csv_url=formatted_csv_url,
                    xlsx_url=xlsx_url,
                    analysis=analysis,
                    notice=notice,
                )
                plain_text_content = build_report_plain_text(
                    report,
                    summary,
                    formatted_csv_url=formatted_csv_url,
                    xlsx_url=xlsx_url,
                    analysis=analysis,
                    notice=notice,
                )

            display_name = report.committee_name
            report_type_display = format_report_type(report.report_type)
            message = EmailMessage(
                subject=f"FEC Report: {display_name} ({report_type_display})",
                html_content=html_content,
                plain_text_content=plain_text_content,
            )

            result = self.send_email(recipients, message)
            metrics.success = result.success
            if result.message_id:
                metrics.extra["message_id"] = result.message_id
            if result.error:
                metrics.extra["error"] = result.error

            return result
