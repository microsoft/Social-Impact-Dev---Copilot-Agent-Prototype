"""Tests for the templates module."""

from types import SimpleNamespace

from services.analysis.analyzers import AnalysisResult
from services.analysis.service import FullAnalysisResult
from services.email.templates import (
    _build_analysis_section_html,
    _build_analysis_section_plain_text,
    _build_detailed_analysis_html,
    _build_financials_html,
    _build_links_html,
    build_report_html,
    build_report_plain_text,
    build_report_preview_html,
)


def make_test_report(
    *,
    candidate_name=None,
    committee_name="Test Committee",
    total_receipts=None,
    total_disbursements=None,
    cash_on_hand_end_period=None,
    pdf_url=None,
    csv_url=None,
):
    """Create a test report with the given attributes."""
    return SimpleNamespace(
        candidate_name=candidate_name,
        committee_name=committee_name,
        committee_id="C00123456",
        report_type="Q1",
        coverage_start_date="2024-01-01",
        coverage_end_date="2024-03-31",
        receipt_date="2024-04-15",
        total_receipts=total_receipts,
        total_disbursements=total_disbursements,
        cash_on_hand_end_period=cash_on_hand_end_period,
        pdf_url=pdf_url,
        csv_url=csv_url,
    )


def make_test_analysis(
    *,
    maxed_donors_stats=None,
    geography_stats=None,
    donor_size_stats=None,
    funding_sources_stats=None,
    expenditures_stats=None,
    industry_narrative=None,
    grouped_donations_narrative=None,
):
    """Create a test FullAnalysisResult with the given data."""
    return FullAnalysisResult(
        summary="Test summary",
        maxed_donors=AnalysisResult(
            feature="maxed_donors",
            data={},
            stats=maxed_donors_stats or {},
            narrative="",
        )
        if maxed_donors_stats
        else None,
        geography=AnalysisResult(
            feature="geography",
            data={},
            stats=geography_stats or {},
            narrative="",
        )
        if geography_stats
        else None,
        donor_size=AnalysisResult(
            feature="donor_size",
            data={},
            stats=donor_size_stats or {},
            narrative="",
        )
        if donor_size_stats
        else None,
        funding_sources=AnalysisResult(
            feature="funding_sources",
            data={},
            stats=funding_sources_stats or {},
            narrative="",
        )
        if funding_sources_stats
        else None,
        expenditures=AnalysisResult(
            feature="expenditures",
            data={},
            stats=expenditures_stats or {},
            narrative="",
        )
        if expenditures_stats
        else None,
        industry=AnalysisResult(
            feature="industry",
            data={},
            stats={},
            narrative=industry_narrative or "",
        )
        if industry_narrative
        else None,
        grouped_donations=AnalysisResult(
            feature="grouped_donations",
            data={},
            stats={},
            narrative=grouped_donations_narrative or "",
        )
        if grouped_donations_narrative
        else None,
    )


class TestBuildFinancialsHtml:
    """Tests for _build_financials_html."""

    def test_empty_financials(self):
        """Test with no financial data."""
        report = make_test_report()
        result = _build_financials_html(report)
        assert result == ""

    def test_total_receipts_only(self):
        """Test with only total receipts."""
        report = make_test_report(total_receipts=100000.0)
        result = _build_financials_html(report)
        assert "Total Receipts" in result
        assert "$100,000.00" in result
        assert "Disbursements" not in result

    def test_all_financials(self):
        """Test with all financial data."""
        report = make_test_report(
            total_receipts=100000.0,
            total_disbursements=80000.0,
            cash_on_hand_end_period=20000.0,
        )
        result = _build_financials_html(report)
        assert "Total Receipts" in result
        assert "$100,000.00" in result
        assert "Total Disbursements" in result
        assert "$80,000.00" in result
        assert "Cash on Hand" in result
        assert "$20,000.00" in result


class TestBuildAnalysisSectionHtml:
    """Tests for _build_analysis_section_html."""

    def test_none_analysis(self):
        """Test with no analysis."""
        result = _build_analysis_section_html(None)
        assert result == ""

    def test_empty_analysis(self):
        """Test with empty analysis (no stats)."""
        analysis = FullAnalysisResult()
        result = _build_analysis_section_html(analysis)
        assert result == ""

    def test_maxed_donors_section(self):
        """Test maxed donors section."""
        analysis = make_test_analysis(
            maxed_donors_stats={"count": 10, "total": 35000.0, "pct_of_individual": 25.5}
        )
        result = _build_analysis_section_html(analysis)
        assert "Analysis Summary" in result
        assert "Maxed Donors ($3,500)" in result
        assert "10 donors" in result
        assert "$35,000.00" in result
        assert "25.5%" in result

    def test_geography_section(self):
        """Test geography section."""
        analysis = make_test_analysis(geography_stats={"in_state_pct": 60.0, "out_state_pct": 40.0})
        result = _build_analysis_section_html(analysis)
        assert "Geography" in result
        assert "60.0% in-state" in result
        assert "40.0% out-of-state" in result

    def test_donor_size_section(self):
        """Test donor size section."""
        analysis = make_test_analysis(donor_size_stats={"small_pct": 15.0, "big_pct": 85.0})
        result = _build_analysis_section_html(analysis)
        assert "Donor Composition" in result
        assert "15.0% from small donors" in result
        assert "85.0% from larger donors" in result

    def test_funding_sources_section(self):
        """Test funding sources section with multiple sources."""
        analysis = make_test_analysis(
            funding_sources_stats={
                "individuals_pct": 70.0,
                "pacs_pct": 20.0,
                "parties_pct": 5.0,
                "transfers_pct": 3.0,
                "loans_pct": 2.0,
            }
        )
        result = _build_analysis_section_html(analysis)
        assert "Funding Sources" in result
        assert "70.0% individuals" in result
        assert "20.0% PACs" in result
        assert "5.0% parties" in result
        assert "3.0% transfers" in result
        assert "2.0% loans" in result

    def test_expenditures_section(self):
        """Test flagged expenditures section."""
        analysis = make_test_analysis(
            expenditures_stats={"flagged_count": 5, "flagged_total": 10000.0}
        )
        result = _build_analysis_section_html(analysis)
        assert "Flagged Expenditures" in result
        assert "5 items" in result
        assert "$10,000.00" in result

    def test_expenditures_hidden_when_zero(self):
        """Test that expenditures section is hidden when count is zero."""
        analysis = make_test_analysis(expenditures_stats={"flagged_count": 0, "flagged_total": 0})
        result = _build_analysis_section_html(analysis)
        # Should not show section header since no stats are shown
        assert "Flagged Expenditures" not in result


class TestBuildDetailedAnalysisHtml:
    """Tests for _build_detailed_analysis_html."""

    def test_none_analysis(self):
        """Test with no analysis."""
        result = _build_detailed_analysis_html(None)
        assert result == ""

    def test_empty_narratives(self):
        """Test with empty narratives."""
        analysis = FullAnalysisResult()
        result = _build_detailed_analysis_html(analysis)
        assert result == ""

    def test_industry_narrative(self):
        """Test with industry narrative."""
        analysis = make_test_analysis(industry_narrative="Tech sector dominates donations.")
        result = _build_detailed_analysis_html(analysis)
        assert "Detailed Analysis" in result
        assert "Industry/Employer Analysis" in result
        assert "Tech sector dominates donations" in result

    def test_grouped_donations_narrative(self):
        """Test with grouped donations narrative."""
        analysis = make_test_analysis(
            grouped_donations_narrative="Notable same-day donation patterns."
        )
        result = _build_detailed_analysis_html(analysis)
        assert "Detailed Analysis" in result
        assert "Donation Patterns" in result
        assert "Notable same-day donation patterns" in result

    def test_both_narratives(self):
        """Test with both narratives."""
        analysis = make_test_analysis(
            industry_narrative="Industry analysis text.",
            grouped_donations_narrative="Donation patterns text.",
        )
        result = _build_detailed_analysis_html(analysis)
        assert "Industry/Employer Analysis" in result
        assert "Industry analysis text" in result
        assert "Donation Patterns" in result
        assert "Donation patterns text" in result


class TestBuildLinksHtml:
    """Tests for _build_links_html."""

    def test_no_links(self):
        """Test with no links."""
        report = make_test_report()
        result = _build_links_html(report)
        assert result == ""

    def test_fec_links_only(self):
        """Test with FEC links only."""
        report = make_test_report(
            pdf_url="https://fec.gov/filing.pdf",
            csv_url="https://fec.gov/filing.csv",
        )
        result = _build_links_html(report)
        assert "Original FEC Filing" in result
        assert "PDF" in result
        assert "CSV" in result
        assert "fec.gov/filing.pdf" in result
        assert "fec.gov/filing.csv" in result

    def test_processed_links_only(self):
        """Test with processed links only."""
        report = make_test_report()
        result = _build_links_html(
            report,
            formatted_csv_url="https://blob.storage/formatted.csv",
            xlsx_url="https://blob.storage/formatted.xlsx",
        )
        assert "Processed Data" in result
        assert "CSV" in result
        assert "Excel" in result

    def test_all_links(self):
        """Test with all links."""
        report = make_test_report(
            pdf_url="https://fec.gov/filing.pdf",
            csv_url="https://fec.gov/filing.csv",
        )
        result = _build_links_html(
            report,
            formatted_csv_url="https://blob.storage/formatted.csv",
            xlsx_url="https://blob.storage/formatted.xlsx",
        )
        assert "Original FEC Filing" in result
        assert "Processed Data" in result


class TestBuildReportHtml:
    """Tests for build_report_html."""

    def test_minimal_report(self):
        """Test with minimal report data."""
        report = make_test_report()
        result = build_report_html(report, "Test summary text")

        assert "<html>" in result
        assert "Test Committee" in result
        assert "Test summary text" in result
        assert "Quarterly" in result  # Report type is formatted

    def test_with_financials(self):
        """Test with financial data."""
        report = make_test_report(
            total_receipts=100000.0,
            total_disbursements=80000.0,
            cash_on_hand_end_period=20000.0,
        )
        result = build_report_html(report, "Summary")

        assert "Financial Summary" in result
        assert "$100,000.00" in result

    def test_with_analysis(self):
        """Test with analysis data."""
        report = make_test_report()
        analysis = make_test_analysis(
            maxed_donors_stats={"count": 5, "total": 17500.0, "pct_of_individual": 20.0}
        )
        result = build_report_html(report, "Summary", analysis=analysis)

        assert "Analysis Summary" in result
        assert "Maxed Donors" in result

    def test_with_links(self):
        """Test with download links."""
        report = make_test_report(
            pdf_url="https://fec.gov/filing.pdf",
            csv_url="https://fec.gov/filing.csv",
        )
        result = build_report_html(
            report,
            "Summary",
            formatted_csv_url="https://blob.storage/formatted.csv",
            xlsx_url="https://blob.storage/formatted.xlsx",
        )

        assert "Original FEC Filing" in result
        assert "Processed Data" in result

    def test_uses_committee_name(self):
        """Test that committee name is used for display."""
        report = make_test_report(
            candidate_name="John Smith",
            committee_name="Smith for Congress",
        )
        result = build_report_html(report, "Summary")

        assert "Smith for Congress" in result


class TestBuildAnalysisSectionPlainText:
    """Tests for _build_analysis_section_plain_text."""

    def test_none_analysis(self):
        """Test with no analysis."""
        result = _build_analysis_section_plain_text(None)
        assert result == []

    def test_with_all_sections(self):
        """Test with all analysis sections."""
        analysis = make_test_analysis(
            maxed_donors_stats={"count": 10, "total": 35000.0, "pct_of_individual": 25.0},
            geography_stats={"in_state_pct": 60.0, "out_state_pct": 40.0},
            donor_size_stats={"small_pct": 15.0, "big_pct": 85.0},
            funding_sources_stats={"individuals_pct": 80.0, "pacs_pct": 20.0},
            expenditures_stats={"flagged_count": 3, "flagged_total": 5000.0},
            industry_narrative="Tech sector dominates.",
            grouped_donations_narrative="Same-day patterns found.",
        )
        result = _build_analysis_section_plain_text(analysis)
        text = "\n".join(result)

        assert "Analysis Summary" in text
        assert "Maxed Donors" in text
        assert "Geography" in text
        assert "Donor Composition" in text
        assert "Funding Sources" in text
        assert "Flagged Expenditures" in text
        assert "Industry Analysis" in text
        assert "Donation Patterns" in text


class TestBuildReportPlainText:
    """Tests for build_report_plain_text."""

    def test_minimal_report(self):
        """Test with minimal report data."""
        report = make_test_report()
        result = build_report_plain_text(report, "Test summary text")

        assert "Test Committee" in result
        assert "Test summary text" in result
        assert "Quarterly" in result  # Report type is formatted
        assert "AI Summary" in result

    def test_with_financials(self):
        """Test with financial data."""
        report = make_test_report(
            total_receipts=100000.0,
            total_disbursements=80000.0,
            cash_on_hand_end_period=20000.0,
        )
        result = build_report_plain_text(report, "Summary")

        assert "Total Receipts: $100,000.00" in result
        assert "Total Disbursements: $80,000.00" in result
        assert "Cash on Hand: $20,000.00" in result

    def test_with_fec_links(self):
        """Test with FEC download links."""
        report = make_test_report(
            pdf_url="https://fec.gov/filing.pdf",
            csv_url="https://fec.gov/filing.csv",
        )
        result = build_report_plain_text(report, "Summary")

        assert "Original FEC Filing" in result
        assert "PDF: https://fec.gov/filing.pdf" in result
        assert "CSV: https://fec.gov/filing.csv" in result

    def test_with_processed_links(self):
        """Test with processed download links."""
        report = make_test_report()
        result = build_report_plain_text(
            report,
            "Summary",
            formatted_csv_url="https://blob.storage/formatted.csv",
            xlsx_url="https://blob.storage/formatted.xlsx",
        )

        assert "Processed Data" in result
        assert "CSV: https://blob.storage/formatted.csv" in result
        assert "Excel: https://blob.storage/formatted.xlsx" in result

    def test_with_analysis(self):
        """Test with analysis data."""
        report = make_test_report()
        analysis = make_test_analysis(
            maxed_donors_stats={"count": 5, "total": 17500.0, "pct_of_individual": 20.0}
        )
        result = build_report_plain_text(report, "Summary", analysis=analysis)

        assert "Analysis Summary" in result
        assert "Maxed Donors" in result


class TestBuildReportPreviewHtml:
    """Tests for build_report_preview_html."""

    def test_includes_page_wrapper(self):
        """Test that preview includes page wrapper."""
        report = make_test_report()
        result = build_report_preview_html(report, "Summary")

        assert "<!DOCTYPE html>" in result
        assert "<title>FEC Report: Test Committee</title>" in result
        assert "max-width: 800px" in result

    def test_includes_report_content(self):
        """Test that preview includes report content."""
        report = make_test_report(total_receipts=100000.0)
        result = build_report_preview_html(report, "Test summary")

        assert "Test Committee" in result
        assert "Test summary" in result
        assert "$100,000.00" in result

    def test_with_analysis(self):
        """Test preview with analysis."""
        report = make_test_report()
        analysis = make_test_analysis(industry_narrative="Industry insights here.")
        result = build_report_preview_html(report, "Summary", analysis=analysis)

        assert "Industry insights here" in result
