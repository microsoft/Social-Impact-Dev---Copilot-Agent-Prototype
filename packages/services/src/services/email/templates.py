"""Email templates for notification services."""

from __future__ import annotations

from fec_api_client import Filings, format_report_type

from ..analysis import FullAnalysisResult
from .utils import format_date, format_period


def _build_financials_html(report: Filings) -> str:
    """Build HTML list items for financial data."""
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


def _build_analysis_section_html(analysis: FullAnalysisResult | None) -> str:
    """Build HTML section for all analysis results as bulleted list."""
    if not analysis:
        return ""

    sections = []

    # Maxed donors
    if analysis.max_out_donors and analysis.max_out_donors.stats.get("count", 0) > 0:
        stats = analysis.max_out_donors.stats
        sections.append(
            f"<li><strong>Max Out Donors ($3,500):</strong> {stats['count']} donors, "
            f"${stats['total']:,.2f}</li>"
        )

    # Geography
    if analysis.geography:
        gs = analysis.geography.stats
        if gs.get("in_state_pct", 0) > 0 or gs.get("out_state_pct", 0) > 0:
            sections.append(
                f"<li><strong>Geography:</strong> {gs.get('in_state_pct', 0):.1f}% "
                f"in-state, {gs.get('out_state_pct', 0):.1f}% out-of-state</li>"
            )

    # Donor size
    if analysis.donor_size:
        ds = analysis.donor_size.stats
        sections.append(
            f"<li><strong>Donor Composition:</strong> {ds.get('small_pct', 0):.1f}% "
            f"from small donors ($25 or less), {ds.get('big_pct', 0):.1f}% from "
            f"larger donors</li>"
        )

    # Funding sources
    if analysis.funding_sources:
        fs = analysis.funding_sources.stats
        parts = []
        if fs.get("individuals_pct", 0) > 0:
            parts.append(f"{fs['individuals_pct']:.1f}% individuals")
        if fs.get("pacs_pct", 0) > 0:
            parts.append(f"{fs['pacs_pct']:.1f}% PACs")
        if fs.get("parties_pct", 0) > 0:
            parts.append(f"{fs['parties_pct']:.1f}% parties")
        if fs.get("transfers_pct", 0) > 0:
            parts.append(f"{fs['transfers_pct']:.1f}% transfers")
        if fs.get("loans_pct", 0) > 0:
            parts.append(f"{fs['loans_pct']:.1f}% loans")
        if fs.get("other_pct", 0) > 0:
            parts.append(f"{fs['other_pct']:.1f}% other")
        if parts:
            sections.append(f"<li><strong>Funding Sources:</strong> {', '.join(parts)}</li>")

    if not sections:
        return ""

    return f"""
    <h3>Analysis Summary</h3>
    <ul>
        {"".join(sections)}
    </ul>
    """


def _build_detailed_analysis_html(analysis: FullAnalysisResult | None) -> str:
    """Build HTML section for detailed AI analysis (industry, grouped donations)."""
    if not analysis:
        return ""

    sections = []

    # Industry analysis
    if analysis.industry and analysis.industry.narrative:
        sections.append(
            f"""
            <div style="background: #f0f7e6; padding: 15px; border-radius: 5px;
                        margin-bottom: 10px;">
                <strong>Industry/Employer Analysis:</strong>
                <p style="margin: 5px 0 0 0;">{analysis.industry.narrative}</p>
                <p style="font-size: 11px; color: #666; margin: 10px 0 0 0; text-align: right;">
                    <em>Analysis by AI</em>
                </p>
            </div>
            """
        )

    # Expenditure analysis
    if analysis.unusual_expenditures and analysis.unusual_expenditures.narrative:
        sections.append(
            f"""
            <div style="background: #f0f7e6; padding: 15px; border-radius: 5px;
                        margin-bottom: 10px;">
                <strong>Expenditure Analysis:</strong>
                <p style="margin: 5px 0 0 0;">{analysis.unusual_expenditures.narrative}</p>
                <p style="font-size: 11px; color: #666; margin: 10px 0 0 0; text-align: right;">
                    <em>Analysis by AI</em>
                </p>
            </div>
            """
        )

    # Grouped donations
    if analysis.grouped_donations and analysis.grouped_donations.narrative:
        sections.append(
            f"""
            <div style="background: #f0f7e6; padding: 15px; border-radius: 5px;
                        margin-bottom: 10px;">
                <strong>Donation Patterns:</strong>
                <p style="margin: 5px 0 0 0;">{analysis.grouped_donations.narrative}</p>
                <p style="font-size: 11px; color: #666; margin: 10px 0 0 0; text-align: right;">
                    <em>Analysis by AI</em>
                </p>
            </div>
            """
        )

    if not sections:
        return ""

    return f"""
    <h3>Detailed Analysis</h3>
    {"".join(sections)}
    """


def _build_links_html(
    report: Filings,
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
    report: Filings,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
    analysis: FullAnalysisResult | None = None,
) -> str:
    """Build HTML content for report email.

    Args:
        report: Report metadata.
        summary: AI-generated summary text.
        formatted_csv_url: Optional URL to formatted CSV.
        xlsx_url: Optional URL to Excel file.
        analysis: Full analysis result with all features.
    """
    financials = _build_financials_html(report)
    links = _build_links_html(report, formatted_csv_url=formatted_csv_url, xlsx_url=xlsx_url)
    analysis_section = _build_analysis_section_html(analysis)
    detailed_section = _build_detailed_analysis_html(analysis)
    period = format_period(report.coverage_start_date, report.coverage_end_date)
    display_name = report.committee_name
    report_type_display = format_report_type(report.report_type)
    filed_date = format_date(report.receipt_date)

    return f"""<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
    <h2 style="color: #1a1a1a;">{display_name} - {report_type_display} Report</h2>

    <div style="background: #f5f5f5; padding: 15px; border-radius: 5px;">
        <p><strong>Committee:</strong> {report.committee_name}</p>
        <p><strong>Period:</strong> {period}</p>
        <p><strong>Filed:</strong> {filed_date}</p>
    </div>

    {"<h3>Financial Summary</h3><ul>" + financials + "</ul>" if financials else ""}

    <h3>Summary</h3>
    <div style="background: #e8f4f8; padding: 15px; border-radius: 5px;">
        <p>{summary}</p>
        <p style="font-size: 11px; color: #666; margin: 10px 0 0 0; text-align: right;">
            <em>Analysis by AI</em>
        </p>
    </div>

    {analysis_section}

    {detailed_section}

    {f"<p>{links}</p>" if links else ""}

    <hr style="border: none; border-top: 1px solid #ddd; margin: 20px 0;">
    <p style="font-size: 12px; color: #666;">
        This is an automated notification from the FEC Filing Monitor.
    </p>
</body>
</html>"""


def _build_analysis_section_plain_text(analysis: FullAnalysisResult | None) -> list[str]:
    """Build plain text section for all analysis results."""
    if not analysis:
        return []

    lines = ["", "Analysis Summary", "-" * 30]

    # Maxed donors
    if analysis.max_out_donors and analysis.max_out_donors.stats.get("count", 0) > 0:
        stats = analysis.max_out_donors.stats
        lines.append(f"  Max Out Donors: {stats['count']} donors, ${stats['total']:,.2f}")

    # Geography
    if analysis.geography:
        gs = analysis.geography.stats
        if gs.get("in_state_pct", 0) > 0 or gs.get("out_state_pct", 0) > 0:
            lines.append(
                f"  Geography: {gs.get('in_state_pct', 0):.1f}% in-state, "
                f"{gs.get('out_state_pct', 0):.1f}% out-of-state"
            )

    # Donor size
    if analysis.donor_size:
        ds = analysis.donor_size.stats
        lines.append(
            f"  Donor Composition: {ds.get('small_pct', 0):.1f}% small donors, "
            f"{ds.get('big_pct', 0):.1f}% larger donors"
        )

    # Funding sources
    if analysis.funding_sources:
        fs = analysis.funding_sources.stats
        parts = []
        if fs.get("individuals_pct", 0) > 0:
            parts.append(f"{fs['individuals_pct']:.1f}% individuals")
        if fs.get("pacs_pct", 0) > 0:
            parts.append(f"{fs['pacs_pct']:.1f}% PACs")
        if fs.get("parties_pct", 0) > 0:
            parts.append(f"{fs['parties_pct']:.1f}% parties")
        if fs.get("transfers_pct", 0) > 0:
            parts.append(f"{fs['transfers_pct']:.1f}% transfers")
        if fs.get("loans_pct", 0) > 0:
            parts.append(f"{fs['loans_pct']:.1f}% loans")
        if fs.get("other_pct", 0) > 0:
            parts.append(f"{fs['other_pct']:.1f}% other")
        if parts:
            lines.append(f"  Funding Sources: {', '.join(parts)}")

    # Detailed analysis narratives
    if analysis.industry and analysis.industry.narrative:
        lines.extend(
            ["", "Industry Analysis:", f"  {analysis.industry.narrative}", "  [Analysis by AI]"]
        )

    if analysis.unusual_expenditures and analysis.unusual_expenditures.narrative:
        lines.extend(
            [
                "",
                "Expenditure Analysis:",
                f"  {analysis.unusual_expenditures.narrative}",
                "  [Analysis by AI]",
            ]
        )

    if analysis.grouped_donations and analysis.grouped_donations.narrative:
        lines.extend(
            [
                "",
                "Donation Patterns:",
                f"  {analysis.grouped_donations.narrative}",
                "  [Analysis by AI]",
            ]
        )

    return lines


def build_report_plain_text(
    report: Filings,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
    analysis: FullAnalysisResult | None = None,
) -> str:
    """Build plain text content for report email.

    Args:
        report: Report metadata.
        summary: AI-generated summary text.
        formatted_csv_url: Optional URL to formatted CSV.
        xlsx_url: Optional URL to Excel file.
        analysis: Full analysis result with all features.
    """
    display_name = report.committee_name
    report_type_display = format_report_type(report.report_type)
    period = format_period(report.coverage_start_date, report.coverage_end_date)
    filed_date = format_date(report.receipt_date)

    lines = [
        f"{display_name} - {report_type_display} Report",
        "=" * 50,
        "",
        f"Committee: {report.committee_name}",
        f"Report Period: {period}",
        f"Filed: {filed_date}",
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
            "Summary",
            "-" * 30,
            summary,
            "[Analysis by AI]",
            "",
        ]
    )

    # Add analysis section
    lines.extend(_build_analysis_section_plain_text(analysis))

    if report.pdf_url or report.csv_url:
        lines.extend(["", "Original FEC Filing:"])
        if report.pdf_url:
            lines.append(f"  PDF: {report.pdf_url}")
        if report.csv_url:
            lines.append(f"  CSV: {report.csv_url}")

    if formatted_csv_url or xlsx_url:
        lines.extend(["", "Processed Data:"])
        if formatted_csv_url:
            lines.append(f"  CSV: {formatted_csv_url}")
        if xlsx_url:
            lines.append(f"  Excel: {xlsx_url}")

    return "\n".join(lines)


def build_report_preview_html(
    report: Filings,
    summary: str,
    *,
    formatted_csv_url: str | None = None,
    xlsx_url: str | None = None,
    analysis: FullAnalysisResult | None = None,
) -> str:
    """Build HTML preview page for report (for browser viewing).

    Wraps the actual email HTML with a page container for centered viewing.

    Args:
        report: Report metadata.
        summary: AI-generated summary text.
        formatted_csv_url: Optional URL to formatted CSV.
        xlsx_url: Optional URL to Excel file.
        analysis: Full analysis result with all features.
    """
    email_html = build_report_html(
        report,
        summary,
        formatted_csv_url=formatted_csv_url,
        xlsx_url=xlsx_url,
        analysis=analysis,
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
