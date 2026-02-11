"""Email templates for notification services."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .quarterly_reports import QuarterlyReport


def build_filing_notification_html(
    filing_count: int,
    summary: str,
    files: list[dict],
    file_urls: list[str],
) -> str:
    """Build HTML email content for filing notifications."""
    files_html = ""
    if file_urls:
        files_html = "<h3>Files</h3><ul>"
        for i, url in enumerate(file_urls):
            file = files[i] if i < len(files) else {}
            name = file.get("committee_name", file.get("file_number", f"File {i + 1}"))
            files_html += f'<li><a href="{url}">{name}</a></li>'
        files_html += "</ul>"

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
        h2 {{ color: #0066cc; }}
        .summary {{ background-color: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        ul {{ padding-left: 20px; }}
        a {{ color: #0066cc; }}
    </style>
</head>
<body>
    <h2>FEC Filing Update</h2>
    <p><strong>{filing_count}</strong> new filing(s) have been processed.</p>

    <div class="summary">
        <h3>Summary</h3>
        <p>{summary}</p>
    </div>

    {files_html}

    <hr>
    <p style="font-size: 12px; color: #666;">
        This is an automated notification from the FEC Data Sync system.
    </p>
</body>
</html>"""


def build_filing_notification_plain_text(
    filing_count: int,
    summary: str,
    files: list[dict],
    file_urls: list[str],
) -> str:
    """Build plain text email content for filing notifications."""
    lines = [
        "FEC Filing Update",
        "=" * 40,
        "",
        f"{filing_count} new filing(s) have been processed.",
        "",
        "Summary:",
        "-" * 20,
        summary,
        "",
    ]

    if file_urls:
        lines.append("Files:")
        lines.append("-" * 20)
        for i, url in enumerate(file_urls):
            file = files[i] if i < len(files) else {}
            name = file.get("committee_name", file.get("file_number", f"File {i + 1}"))
            lines.append(f"- {name}: {url}")

    lines.extend(["", "-" * 40, "This is an automated notification from the FEC Data Sync system."])
    return "\n".join(lines)


def _build_quarterly_financials_html(report: QuarterlyReport) -> str:
    """Build HTML list items for financial data."""
    financials = ""
    if report.total_receipts is not None:
        financials += f"<li><strong>Total Receipts:</strong> ${report.total_receipts:,.2f}</li>"
    if report.total_disbursements is not None:
        financials += (
            f"<li><strong>Total Disbursements:</strong> ${report.total_disbursements:,.2f}</li>"
        )
    if report.cash_on_hand is not None:
        financials += f"<li><strong>Cash on Hand:</strong> ${report.cash_on_hand:,.2f}</li>"
    return financials


def _build_quarterly_links_html(report: QuarterlyReport) -> str:
    """Build HTML links for PDF and CSV downloads."""
    links = ""
    if report.pdf_url:
        links += f'<a href="{report.pdf_url}" style="color: #0066cc;">View PDF</a>'
    if report.csv_url:
        if links:
            links += " | "
        links += f'<a href="{report.csv_url}" style="color: #0066cc;">Download CSV</a>'
    return links


def build_quarterly_report_html(report: QuarterlyReport, summary: str) -> str:
    """Build HTML content for quarterly report email."""
    financials = _build_quarterly_financials_html(report)
    links = _build_quarterly_links_html(report)
    period = f"{report.coverage_start_date} to {report.coverage_end_date}"

    return f"""<html>
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
</html>"""


def build_quarterly_report_plain_text(report: QuarterlyReport, summary: str) -> str:
    """Build plain text content for quarterly report email."""
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


def build_quarterly_report_preview_html(report: QuarterlyReport, summary: str) -> str:
    """Build HTML preview page for quarterly report (for browser viewing)."""
    financials = _build_quarterly_financials_html(report)
    links = _build_quarterly_links_html(report)
    period = f"{report.coverage_start_date} to {report.coverage_end_date}"

    return f"""<!DOCTYPE html>
<html>
<head>
    <title>FEC Report Preview: {report.committee_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333;
               max-width: 800px; margin: 40px auto; padding: 20px; }}
        .header {{ background: #1a1a1a; color: white; padding: 20px; border-radius: 5px; }}
        .info-box {{ background: #f5f5f5; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .summary-box {{ background: #e8f4f8; padding: 15px; border-radius: 5px; margin: 20px 0; }}
        .footer {{ font-size: 12px; color: #666; border-top: 1px solid #ddd;
                   padding-top: 20px; margin-top: 30px; }}
        a {{ color: #0066cc; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>{report.candidate_name} - {report.report_type} Report</h1>
        <p>Preview of email notification</p>
    </div>
    <div class="info-box">
        <p><strong>Committee:</strong> {report.committee_name}</p>
        <p><strong>Period:</strong> {period}</p>
        <p><strong>Filed:</strong> {report.receipt_date}</p>
    </div>
    {"<h3>Financial Summary</h3><ul>" + financials + "</ul>" if financials else ""}
    <h3>AI Summary</h3>
    <div class="summary-box">
        <p>{summary}</p>
    </div>
    {f"<p>{links}</p>" if links else ""}
    <div class="footer">
        <p>This is a preview of the automated notification from the FEC Filing Monitor.</p>
    </div>
</body>
</html>"""
