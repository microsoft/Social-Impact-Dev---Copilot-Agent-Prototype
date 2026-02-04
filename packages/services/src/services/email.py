from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Any, Protocol

from azure.communication.email import EmailClient
from azure.identity import DefaultAzureCredential

from .templates import build_filing_notification_html, build_filing_notification_plain_text

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

    def send_summary_email(
        self,
        recipients: list[str],
        filings: list[dict],
        summary: str,
        file_urls: list[str],
    ) -> EmailResult: ...

    @staticmethod
    def parse_recipient_list(recipient_list: str) -> list[str]: ...


class AzureEmailService:
    """Azure Communication Services email sender."""

    @staticmethod
    def parse_recipient_list(recipient_list: str) -> list[str]:
        """Parse a comma-separated recipient list string into a list of email addresses."""
        return [r.strip() for r in recipient_list.split(",") if r.strip()]

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
            return EmailResult(success=True, message_id=message_id)
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return EmailResult(success=False, error=str(e))

    def send_summary_email(
        self,
        recipients: list[str],
        filings: list[dict],
        summary: str,
        file_urls: list[str],
    ) -> EmailResult:
        """Send a summary email with filing information.

        Args:
            recipients: List of email addresses to send to.
            filings: List of filing dictionaries with metadata.
            summary: AI-generated or fallback summary text.
            file_urls: List of URLs to the filed documents.

        Returns:
            EmailResult with success status and message ID or error.
        """
        if not recipients:
            logger.warning("No recipients provided, skipping email")
            return EmailResult(success=False, error="No recipients provided")

        filing_count = len(filings)
        html_content = build_filing_notification_html(
            filing_count=filing_count,
            summary=summary,
            files=filings,
            file_urls=file_urls,
        )
        plain_text_content = build_filing_notification_plain_text(
            filing_count=filing_count,
            summary=summary,
            files=filings,
            file_urls=file_urls,
        )

        message = EmailMessage(
            subject=f"FEC Filing Update: {filing_count} New File(s)",
            html_content=html_content,
            plain_text_content=plain_text_content,
        )

        return self.send_email(recipients, message)
