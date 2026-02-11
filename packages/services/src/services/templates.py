"""Email templates for notification services."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .analysis import AnalysisResult
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


def _build_maxed_donors_html(analysis: AnalysisResult | None) -> str:
    """Build HTML section for maxed donors analysis."""
    if not analysis or analysis.stats.get("count", 0) == 0:
        return ""

    stats = analysis.stats
    data = analysis.data

    # Build top employers list
    top_employers = data.get("top_employers", [])[:5]
    employers_html = ""
    if top_employers:
        employer_items = ", ".join(f"{name} ({count})" for name, count in top_employers)
        employers_html = f"<li><strong>Top Employers:</strong> {employer_items}</li>"

    # Build top states list
    top_states = data.get("top_states", [])[:5]
    states_html = ""
    if top_states:
        state_items = ", ".join(f"{state} ({count})" for state, count in top_states)
        states_html = f"<li><strong>Top States:</strong> {state_items}</li>"

    count = stats.get("count", 0)
    total = stats.get("total", 0)
    pct = stats.get("pct_of_individual", 0)

    return f"""
    <h3>Maxed Out Donors ($3,500 limit)</h3>
    <ul>
        <li><strong>{count}</strong> donors reached the contribution limit</li>
        <li><strong>${total:,.2f}</strong> total from maxed donors
            ({pct:.1f}% of individual contributions)</li>
        {employers_html}
        {states_html}
    </ul>
    <div style="background: #f0f7e6; padding: 15px; border-radius: 5px; margin-top: 10px;">
        <p style="margin: 0;">{analysis.narrative}</p>
    </div>
    """


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
    maxed_donors_analysis: AnalysisResult | None = None,
) -> str:
    """Build HTML content for report email.

    Args:
        report: Report metadata.
        summary: AI-generated summary text.
        formatted_csv_url: Optional URL to formatted CSV.
        xlsx_url: Optional URL to Excel file.
        maxed_donors_analysis: Optional maxed donors analysis result.
    """
    from .reports import get_display_name

    financials = _build_financials_html(report)
    links = _build_links_html(report, formatted_csv_url=formatted_csv_url, xlsx_url=xlsx_url)
    maxed_donors_section = _build_maxed_donors_html(maxed_donors_analysis)
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

    {maxed_donors_section}

    {f"<p>{links}</p>" if links else ""}

    <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
    <p style="font-size: 12px; color: #666;">
        This is an automated notification from the FEC Filing Monitor.
    </p>
</body>
</html>"""


def _build_maxed_donors_plain_text(analysis: AnalysisResult | None) -> list[str]:
    """Build plain text section for maxed donors analysis."""
    if not analysis or analysis.stats.get("count", 0) == 0:
        return []

    stats = analysis.stats
    data = analysis.data

    count = stats.get("count", 0)
    total = stats.get("total", 0)
    pct = stats.get("pct_of_individual", 0)

    lines = [
        "",
        "Maxed Out Donors ($3,500 limit)",
        "-" * 30,
        f"  {count} donors reached the contribution limit",
        f"  ${total:,.2f} total ({pct:.1f}% of individual contributions)",
    ]

    top_employers = data.get("top_employers", [])[:5]
    if top_employers:
        employer_items = ", ".join(f"{name} ({count})" for name, count in top_employers)
        lines.append(f"  Top Employers: {employer_items}")

    top_states = data.get("top_states", [])[:5]
    if top_states:
        state_items = ", ".join(f"{state} ({count})" for state, count in top_states)
        lines.append(f"  Top States: {state_items}")

    lines.extend(["", analysis.narrative, ""])

    return lines


def build_report_plain_text(
    report: Report,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
    maxed_donors_analysis: AnalysisResult | None = None,
) -> str:
    """Build plain text content for report email.

    Args:
        report: Report metadata.
        summary: AI-generated summary text.
        formatted_csv_url: Optional URL to formatted CSV.
        xlsx_url: Optional URL to Excel file.
        maxed_donors_analysis: Optional maxed donors analysis result.
    """
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

    # Add maxed donors section
    lines.extend(_build_maxed_donors_plain_text(maxed_donors_analysis))

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
    maxed_donors_analysis: AnalysisResult | None = None,
) -> str:
    """Build HTML preview page for report (for browser viewing).

    Wraps the actual email HTML with a page container for centered viewing.

    Args:
        report: Report metadata.
        summary: AI-generated summary text.
        formatted_csv_url: Optional URL to formatted CSV.
        xlsx_url: Optional URL to Excel file.
        maxed_donors_analysis: Optional maxed donors analysis result.
    """
    email_html = build_report_html(
        report,
        summary,
        formatted_csv_url=formatted_csv_url,
        xlsx_url=xlsx_url,
        maxed_donors_analysis=maxed_donors_analysis,
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
