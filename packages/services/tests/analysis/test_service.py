"""Tests for the analysis service module."""

from unittest.mock import MagicMock, patch

import pytest
from services.analysis.analyzers import AnalysisResult
from services.analysis.service import FullAnalysisResult, OpenAIAnalysisService
from services.report.format import ParsedQuarterlyCSV


def make_mock_report(candidate_name=None, committee_name="Test Committee"):
    """Create a mock report with proper attributes.

    Uses SimpleNamespace to avoid MagicMock's auto-attribute creation,
    which can interfere with format string operations.
    """
    from types import SimpleNamespace

    return SimpleNamespace(
        candidate_name=candidate_name,
        committee_name=committee_name,
        committee_id="C00123456",
        state="WA",
        report_year=2024,
        report_type="Q1",
        form_type="F3",
        coverage_start_date="2024-01-01",
        coverage_end_date="2024-03-31",
        receipt_date="2024-04-15",
        # Financial fields need to be real numbers for formatting
        total_receipts=100000.0,
        total_disbursements=80000.0,
        cash_on_hand_end_period=20000.0,
        debts_owed_by=0.0,
        debts_owed_to=0.0,
    )


class TestFullAnalysisResult:
    """Tests for FullAnalysisResult dataclass."""

    def test_get_combined_narrative_empty(self):
        """Test combined narrative with no analyses."""
        result = FullAnalysisResult()
        assert result.get_combined_narrative() == ""

    def test_get_combined_narrative_summary_only(self):
        """Test combined narrative with only summary."""
        result = FullAnalysisResult(summary="This is a summary.")
        assert result.get_combined_narrative() == "This is a summary."

    def test_get_combined_narrative_all_sections(self):
        """Test combined narrative with all sections populated."""
        result = FullAnalysisResult(
            summary="Summary text",
            maxed_donors=AnalysisResult(
                feature="maxed_donors",
                data={},
                stats={},
                narrative="Maxed donors narrative",
            ),
            geography=AnalysisResult(
                feature="geography",
                data={},
                stats={},
                narrative="Geography narrative",
            ),
            donor_size=AnalysisResult(
                feature="donor_size",
                data={},
                stats={},
                narrative="Donor size narrative",
            ),
            funding_sources=AnalysisResult(
                feature="funding_sources",
                data={},
                stats={},
                narrative="Funding sources narrative",
            ),
            expenditures=AnalysisResult(
                feature="expenditures",
                data={},
                stats={},
                narrative="Expenditures narrative",
            ),
            industry=AnalysisResult(
                feature="industry",
                data={},
                stats={},
                narrative="Industry narrative",
            ),
            grouped_donations=AnalysisResult(
                feature="grouped_donations",
                data={},
                stats={},
                narrative="Grouped donations narrative",
            ),
        )

        combined = result.get_combined_narrative()

        assert "Summary text" in combined
        assert "**Maxed Donors:** Maxed donors narrative" in combined
        assert "**Geography:** Geography narrative" in combined
        assert "**Donor Size:** Donor size narrative" in combined
        assert "**Funding Sources:** Funding sources narrative" in combined
        assert "**Expenditures:** Expenditures narrative" in combined
        assert "**Industry Analysis:** Industry narrative" in combined
        assert "**Grouped Donations:** Grouped donations narrative" in combined
        # Check sections are separated by double newlines
        assert "\n\n" in combined

    def test_get_combined_narrative_skips_empty_narratives(self):
        """Test that sections with empty narratives are skipped."""
        result = FullAnalysisResult(
            summary="Summary",
            maxed_donors=AnalysisResult(
                feature="maxed_donors",
                data={},
                stats={},
                narrative="",  # Empty narrative
            ),
            geography=AnalysisResult(
                feature="geography",
                data={},
                stats={},
                narrative="Geography info",
            ),
        )

        combined = result.get_combined_narrative()

        assert "Summary" in combined
        assert "Geography info" in combined
        assert "Maxed Donors" not in combined

    def test_get_stats_summary_empty(self):
        """Test stats summary with no analyses."""
        result = FullAnalysisResult()
        assert result.get_stats_summary() == {}

    def test_get_stats_summary_all_sections(self):
        """Test stats summary with all sections populated."""
        result = FullAnalysisResult(
            maxed_donors=AnalysisResult(
                feature="maxed_donors",
                data={},
                stats={"count": 10, "total": 35000},
                narrative="",
            ),
            geography=AnalysisResult(
                feature="geography",
                data={},
                stats={"in_state_pct": 60.0, "out_state_pct": 40.0},
                narrative="",
            ),
            donor_size=AnalysisResult(
                feature="donor_size",
                data={},
                stats={"small_pct": 25.0, "big_pct": 75.0},
                narrative="",
            ),
            funding_sources=AnalysisResult(
                feature="funding_sources",
                data={},
                stats={"individuals_pct": 80.0, "pacs_pct": 20.0},
                narrative="",
            ),
            expenditures=AnalysisResult(
                feature="expenditures",
                data={},
                stats={"flagged_count": 5, "flagged_total": 10000},
                narrative="",
            ),
            industry=AnalysisResult(
                feature="industry",
                data={},
                stats={"top_industry": "Tech"},
                narrative="",
            ),
            grouped_donations=AnalysisResult(
                feature="grouped_donations",
                data={},
                stats={"groups_found": 3},
                narrative="",
            ),
        )

        stats = result.get_stats_summary()

        assert stats["maxed_donors"]["count"] == 10
        assert stats["geography"]["in_state_pct"] == 60.0
        assert stats["donor_size"]["small_pct"] == 25.0
        assert stats["funding_sources"]["individuals_pct"] == 80.0
        assert stats["expenditures"]["flagged_count"] == 5
        assert stats["industry"]["top_industry"] == "Tech"
        assert stats["grouped_donations"]["groups_found"] == 3


class TestOpenAIAnalysisService:
    """Tests for OpenAIAnalysisService."""

    @pytest.fixture
    def mock_blob_service(self):
        """Create a mock blob storage service."""
        service = MagicMock()
        service.download_bytes.return_value = None
        service.upload_bytes.return_value = None
        return service

    @pytest.fixture
    def mock_report(self):
        """Create a mock report."""
        return make_mock_report()

    @pytest.fixture
    def sample_parsed_file(self):
        """Create a sample parsed FEC file."""
        return ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[],
            disbursements=[],
        )

    def test_init_without_blob_service(self):
        """Test service initialization without blob service."""
        service = OpenAIAnalysisService()
        assert service.blob_service is None

    def test_init_with_blob_service(self, mock_blob_service):
        """Test service initialization with blob service."""
        service = OpenAIAnalysisService(blob_service=mock_blob_service)
        assert service.blob_service is mock_blob_service

    def test_lazy_loading_analyzers(self, mock_blob_service):
        """Test that analyzers are lazy-loaded."""
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        # Initially all analyzers should be None
        assert service._maxed_donors_analyzer is None
        assert service._geography_analyzer is None
        assert service._donor_size_analyzer is None
        assert service._funding_source_analyzer is None
        assert service._expenditure_analyzer is None
        assert service._industry_analyzer is None
        assert service._grouped_donations_analyzer is None
        assert service._summary_analyzer is None

    @patch("services.analysis.service.OpenAIAnalysisService._get_summary_analyzer")
    def test_generate_summary_with_cache_hit(
        self, mock_get_analyzer, mock_blob_service, mock_report
    ):
        """Test generate_summary returns cached result when available."""
        mock_blob_service.download_bytes.return_value = b"Cached summary text"
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        result = service.generate_summary(mock_report, base_path="C00123456/2024-Q1")

        assert result == "Cached summary text"
        mock_blob_service.download_bytes.assert_called_once_with("C00123456/2024-Q1/summary.txt")
        # AI analyzer should not be called when cache hits
        mock_get_analyzer.assert_not_called()

    @patch.dict(
        "os.environ",
        {
            "AZURE_OPENAI_ENDPOINT": "https://test.openai.azure.com",
            "AZURE_OPENAI_API_KEY": "test-key",
            "AZURE_OPENAI_DEPLOYMENT": "test-deployment",
        },
    )
    @patch("services.analysis.analyzers.AzureOpenAI")
    def test_generate_summary_with_cache_miss(self, mock_openai_class, mock_blob_service):
        """Test generate_summary calls AI when cache misses."""
        mock_blob_service.download_bytes.return_value = None

        # Create report with proper attributes for formatting
        report = make_mock_report()

        # Mock OpenAI response
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "AI generated summary"
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai_class.return_value = mock_client

        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        result = service.generate_summary(report, base_path="C00123456/2024-Q1")

        assert result == "AI generated summary"
        # Should cache the result
        mock_blob_service.upload_bytes.assert_called()

    def test_generate_summary_fallback_on_ai_error(self, mock_blob_service):
        """Test generate_summary returns fallback when AI fails."""
        mock_blob_service.download_bytes.return_value = None
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        # Use report with committee_name only (no candidate_name)
        report = make_mock_report(candidate_name=None, committee_name="Test Committee")

        # Don't mock OpenAI - let it fail due to missing credentials
        result = service.generate_summary(report, base_path="C00123456/2024-Q1")

        assert "Test Committee" in result
        assert "AI summary unavailable" in result

    def test_generate_summary_without_base_path(self, mock_blob_service):
        """Test generate_summary without caching when no base_path."""
        mock_blob_service.download_bytes.return_value = None
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        # Use report with committee_name only (no candidate_name)
        report = make_mock_report(candidate_name=None, committee_name="Test Committee")

        result = service.generate_summary(report, base_path=None)

        # Should not attempt to read cache
        mock_blob_service.download_bytes.assert_not_called()
        # Should return fallback since no AI credentials
        assert "Test Committee" in result

    def test_get_cached_analysis_returns_none_without_blob_service(self):
        """Test _get_cached_analysis returns None without blob service."""
        service = OpenAIAnalysisService(blob_service=None)

        result = service._get_cached_analysis("some/path.json")

        assert result is None

    def test_get_cached_analysis_returns_none_on_miss(self, mock_blob_service):
        """Test _get_cached_analysis returns None on cache miss."""
        mock_blob_service.download_bytes.return_value = None
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        result = service._get_cached_analysis("some/path.json")

        assert result is None

    def test_get_cached_analysis_returns_result_on_hit(self, mock_blob_service):
        """Test _get_cached_analysis returns AnalysisResult on cache hit."""
        import json

        cached_data = {
            "feature": "test_feature",
            "data": {"key": "value"},
            "stats": {"count": 10},
            "narrative": "Test narrative",
        }
        mock_blob_service.download_bytes.return_value = json.dumps(cached_data).encode()
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        result = service._get_cached_analysis("some/path.json")

        assert result is not None
        assert result.feature == "test_feature"
        assert result.data == {"key": "value"}
        assert result.stats == {"count": 10}
        assert result.narrative == "Test narrative"
        assert result.cached is True

    def test_cache_analysis_does_nothing_without_blob_service(self):
        """Test _cache_analysis does nothing without blob service."""
        service = OpenAIAnalysisService(blob_service=None)
        result = AnalysisResult(feature="test", data={}, stats={}, narrative="test")

        # Should not raise
        service._cache_analysis("some/path.json", result)

    def test_cache_analysis_uploads_to_blob(self, mock_blob_service):
        """Test _cache_analysis uploads result to blob storage."""
        service = OpenAIAnalysisService(blob_service=mock_blob_service)
        result = AnalysisResult(
            feature="test_feature",
            data={"key": "value"},
            stats={"count": 10},
            narrative="Test narrative",
        )

        service._cache_analysis("some/path.json", result)

        mock_blob_service.upload_bytes.assert_called_once()
        call_args = mock_blob_service.upload_bytes.call_args
        assert call_args[0][0] == "some/path.json"
        assert b"test_feature" in call_args[0][1]

    @patch.dict(
        "os.environ",
        {
            "AZURE_OPENAI_ENDPOINT": "https://test.openai.azure.com",
            "AZURE_OPENAI_API_KEY": "test-key",
            "AZURE_OPENAI_DEPLOYMENT": "test-deployment",
        },
    )
    @patch("services.analysis.analyzers.AzureOpenAI")
    def test_run_full_analysis_returns_complete_result(
        self,
        mock_openai_class,
        mock_blob_service,
        mock_report,
        sample_parsed_file,
    ):
        """Test run_full_analysis returns FullAnalysisResult with all fields."""
        mock_blob_service.download_bytes.return_value = None

        # Mock OpenAI response for AI analyzers
        mock_client = MagicMock()
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "AI analysis result"
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai_class.return_value = mock_client

        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        result = service.run_full_analysis(
            sample_parsed_file, mock_report, base_path="C00123456/2024-Q1"
        )

        assert isinstance(result, FullAnalysisResult)
        assert result.summary is not None
        assert result.maxed_donors is not None
        assert result.geography is not None
        assert result.donor_size is not None
        assert result.funding_sources is not None
        assert result.expenditures is not None
        assert result.industry is not None
        assert result.grouped_donations is not None

    def test_format_analysis_stats(self, mock_blob_service):
        """Test _format_analysis_stats formats stats correctly."""
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        maxed = AnalysisResult(
            feature="maxed_donors",
            data={},
            stats={"count": 10, "total": 35000},
            narrative="",
        )
        geography = AnalysisResult(
            feature="geography",
            data={},
            stats={"in_state_pct": 60.0, "out_state_pct": 40.0},
            narrative="",
        )
        donor_size = AnalysisResult(
            feature="donor_size",
            data={},
            stats={"small_pct": 15.0, "big_pct": 85.0},
            narrative="",
        )
        funding = AnalysisResult(
            feature="funding_sources",
            data={},
            stats={"individuals_pct": 80.0, "pacs_pct": 15.0, "parties_pct": 5.0},
            narrative="",
        )
        expenditure = AnalysisResult(
            feature="expenditures",
            data={},
            stats={"flagged_count": 3, "flagged_total": 5000},
            narrative="",
        )

        result = service._format_analysis_stats(maxed, geography, donor_size, funding, expenditure)

        assert "Maxed Donors ($3,500): 10 donors" in result
        assert "$35,000.00" in result
        assert "Geography: 60.0% in-state" in result
        assert "Donor Size: 15.0% from small donors" in result
        assert "Funding Sources: 80.0% individuals" in result
        assert "Flagged Expenditures: 3 items" in result

    def test_analyze_maxed_donors_with_cache_hit(
        self, mock_blob_service, mock_report, sample_parsed_file
    ):
        """Test analyze_maxed_donors returns cached result."""
        import json

        cached_data = {
            "feature": "maxed_donors",
            "data": {"donors": []},
            "stats": {"count": 5, "total": 17500},
            "narrative": "Cached narrative",
        }
        mock_blob_service.download_bytes.return_value = json.dumps(cached_data).encode()
        service = OpenAIAnalysisService(blob_service=mock_blob_service)

        result = service.analyze_maxed_donors(
            sample_parsed_file, mock_report, base_path="C00123456/2024-Q1"
        )

        assert result.cached is True
        assert result.stats["count"] == 5
        assert result.narrative == "Cached narrative"


class TestExtractOnly:
    """Tests for extract_only method."""

    @pytest.fixture
    def sample_parsed_file(self):
        """Create a sample parsed FEC file with some data."""
        contribution_row = [
            "SA11AI",
            "C00123456",
            "TXN001",
            "",
            "",
            "IND",
            "",
            "Doe",
            "John",
            "",
            "",
            "",
            "123 Main St",
            "",
            "Seattle",
            "WA",
            "98101",
            "",
            "",
            "20240101",
            "1000.00",
            "1000.00",
            "",
            "Tech Company",
            "Engineer",
        ]
        return ParsedQuarterlyCSV(
            version="8.5",
            header=["HDR"],
            summary=["F3"],
            contributions=[contribution_row],
            disbursements=[],
        )

    @pytest.fixture
    def mock_report(self):
        """Create a mock report."""
        return make_mock_report()

    def test_extract_only_returns_all_extractions(self, sample_parsed_file, mock_report):
        """Test extract_only returns all extraction results."""
        service = OpenAIAnalysisService()

        result = service.extract_only(sample_parsed_file, mock_report)

        assert "maxed_donors" in result
        assert "geography" in result
        assert "donor_size" in result
        assert "funding_sources" in result
        assert "expenditures" in result
        assert "industry" in result
        assert "grouped_donations" in result

        # Each should have data and stats
        for key in result:
            assert "data" in result[key]
            assert "stats" in result[key]
