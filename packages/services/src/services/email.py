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

    def send_candidate_report_email(
        self,
        recipients: list[str],
        report: Any,
        summary: str,
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

    def send_candidate_report_email(
        self,
        recipients: list[str],
        report,
        summary: str,
    ) -> EmailResult:
        """Send an email summarizing a candidate's quarterly report.

        Args:
            recipients: List of email addresses to send to.
            report: CandidateReport object with filing details.
            summary: AI-generated summary text.

        Returns:
            EmailResult with success status and message ID or error.
        """
        if not recipients:
            logger.warning("No recipients provided, skipping email")
            return EmailResult(success=False, error="No recipients provided")

        html_content = self._build_candidate_report_html(report, summary)
        plain_text_content = self._build_candidate_report_plain_text(report, summary)

        message = EmailMessage(
            subject=f"FEC Quarterly Report: {report.candidate_name} ({report.report_type})",
            html_content=html_content,
            plain_text_content=plain_text_content,
        )

        return self.send_email(recipients, message)

    def _build_candidate_report_html(self, report, summary: str) -> str:
        """Build HTML content for candidate report email."""
        financials = ""
        if report.total_receipts is not None:
            financials += f"<li><strong>Total Receipts:</strong> ${report.total_receipts:,.2f}</li>"
        if report.total_disbursements is not None:
            financials += (
                f"<li><strong>Total Disbursements:</strong> ${report.total_disbursements:,.2f}</li>"
            )
        if report.cash_on_hand is not None:
            financials += f"<li><strong>Cash on Hand:</strong> ${report.cash_on_hand:,.2f}</li>"

        links = ""
        if report.pdf_url:
            links += f'<a href="{report.pdf_url}" style="color: #0066cc;">View PDF</a>'
        if report.csv_url:
            if links:
                links += " | "
            links += f'<a href="{report.csv_url}" style="color: #0066cc;">Download CSV</a>'

        period = f"{report.coverage_start_date} to {report.coverage_end_date}"
        return f"""
        <html>
        <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
            <h2 style="color: #1a1a1a;">{report.candidate_name} - {report.report_type} Report</h2>

            <div style="background: #f5f5f5; padding: 15px; border-radius: 5px;">
                <p><strong>Committee:</strong> {report.committee_name}</p>
                <p><strong>Period:</strong> {period}</p>
                <p><strong>Filed:</strong> {report.receipt_date}</p>
            </div>

            {"<h3>Financial Summary</h3><ul>" + financials + "</ul>" if financials else ""}

            <h3>AI Summary</h3>
            <div style="background: #e8f4f8; padding: 15px; border-radius: 5px;">
                <p>{summary}</p>
            </div>

            {f"<p>{links}</p>" if links else ""}

            <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
            <p style="font-size: 12px; color: #666;">
                This is an automated notification from the FEC Filing Monitor.
            </p>
        </body>
        </html>
        """

    def _build_candidate_report_plain_text(self, report, summary: str) -> str:
        """Build plain text content for candidate report email."""
        lines = [
            f"{report.candidate_name} - {report.report_type} Report",
            "=" * 50,
            "",
            f"Committee: {report.committee_name}",
            f"Report Period: {report.coverage_start_date} to {report.coverage_end_date}",
            f"Filed: {report.receipt_date}",
            "",
        ]

        if report.total_receipts is not None:
            lines.append(f"Total Receipts: ${report.total_receipts:,.2f}")
        if report.total_disbursements is not None:
            lines.append(f"Total Disbursements: ${report.total_disbursements:,.2f}")
        if report.cash_on_hand is not None:
            lines.append(f"Cash on Hand: ${report.cash_on_hand:,.2f}")

        lines.extend(
            [
                "",
                "AI Summary",
                "-" * 30,
                summary,
                "",
            ]
        )

        if report.pdf_url:
            lines.append(f"PDF: {report.pdf_url}")
        if report.csv_url:
            lines.append(f"CSV: {report.csv_url}")

        return "\n".join(lines)
