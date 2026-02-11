"""Email templates for notification services."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .reports import Report


def _build_financials_html(report: Report) -> str:
    """Build HTML list items for financial data."""
    from .reports import get_display_name  # noqa: F401 - used in templates

    financials = ""
    if report.total_receipts is not None:
        financials += f"<li><strong>Total Receipts:</strong> ${report.total_receipts:,.2f}</li>"
    if report.total_disbursements is not None:
        financials += (
            f"<li><strong>Total Disbursements:</strong> ${report.total_disbursements:,.2f}</li>"
        )
    if report.cash_on_hand_end_period is not None:
        financials += (
            f"<li><strong>Cash on Hand:</strong> ${report.cash_on_hand_end_period:,.2f}</li>"
        )
    return financials


def _build_links_html(
    report: Report,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
) -> str:
    """Build HTML links for original FEC files and processed downloads."""
    sections = []

    # Original FEC files (from report object)
    fec_links = []
    if report.pdf_url:
        fec_links.append(f'<a href="{report.pdf_url}" style="color: #0066cc;">PDF</a>')
    if report.csv_url:
        fec_links.append(f'<a href="{report.csv_url}" style="color: #0066cc;">CSV</a>')
    if fec_links:
        sections.append(f"<strong>Original FEC Filing:</strong> {' | '.join(fec_links)}")

    # Processed files
    processed_links = []
    if formatted_csv_url:
        processed_links.append(f'<a href="{formatted_csv_url}" style="color: #0066cc;">CSV</a>')
    if xlsx_url:
        processed_links.append(f'<a href="{xlsx_url}" style="color: #0066cc;">Excel</a>')
    if processed_links:
        sections.append(f"<strong>Processed Data:</strong> {' | '.join(processed_links)}")

    return "<br>".join(sections)


def build_report_html(
    report: Report,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
) -> str:
    """Build HTML content for report email."""
    from .reports import get_display_name

    financials = _build_financials_html(report)
    links = _build_links_html(report, formatted_csv_url=formatted_csv_url, xlsx_url=xlsx_url)
    period = f"{report.coverage_start_date} to {report.coverage_end_date}"
    display_name = get_display_name(report)

    return f"""<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <h2 style="color: #1a1a1a;">{display_name} - {report.report_type} Report</h2>

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


def build_report_plain_text(
    report: Report,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
) -> str:
    """Build plain text content for report email."""
    from .reports import get_display_name

    display_name = get_display_name(report)
    lines = [
        f"{display_name} - {report.report_type} Report",
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
    if report.cash_on_hand_end_period is not None:
        lines.append(f"Cash on Hand: ${report.cash_on_hand_end_period:,.2f}")

    lines.extend(
        [
            "",
            "AI Summary",
            "-" * 30,
            summary,
            "",
        ]
    )

    if report.pdf_url or report.csv_url:
        lines.append("Original FEC Filing:")
        if report.pdf_url:
            lines.append(f"  PDF: {report.pdf_url}")
        if report.csv_url:
            lines.append(f"  CSV: {report.csv_url}")
        lines.append("")

    if formatted_csv_url or xlsx_url:
        lines.append("Processed Data:")
        if formatted_csv_url:
            lines.append(f"  CSV: {formatted_csv_url}")
        if xlsx_url:
            lines.append(f"  Excel: {xlsx_url}")

    return "\n".join(lines)


def build_report_preview_html(
    report: Report,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
) -> str:
    """Build HTML preview page for report (for browser viewing).

    Wraps the actual email HTML with a page container for centered viewing.
    """
    email_html = build_report_html(
        report,
        summary,
        formatted_csv_url=formatted_csv_url,
        xlsx_url=xlsx_url,
    )

    return f"""<!DOCTYPE html>
<html>
<head>
    <title>FEC Report: {report.committee_name}</title>
    <style>
        body {{ max-width: 800px; margin: 40px auto; padding: 20px; }}
    </style>
</head>
{email_html[email_html.find("<body") :]}"""
