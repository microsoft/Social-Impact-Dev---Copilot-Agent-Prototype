"""Tests for the reports module."""

import json
from types import SimpleNamespace
from unittest.mock import MagicMock

import pytest
from services.email import EmailResult
from services.reports import (
    ProcessingResult,
    ReportService,
    get_display_name,
)


def make_test_report(candidate_name=None, committee_name="Test Committee"):
    """Create a test report object."""
    return SimpleNamespace(
        candidate_name=candidate_name,
        committee_name=committee_name,
        committee_id="C00123456",
    )


class TestGetDisplayName:
    """Tests for get_display_name function."""

    def test_returns_candidate_name_when_present(self):
        """Test that candidate name is used when available."""
        report = make_test_report(candidate_name="John Smith", committee_name="Committee")
        assert get_display_name(report) == "John Smith"

    def test_returns_committee_name_when_no_candidate(self):
        """Test fallback to committee name."""
        report = make_test_report(candidate_name=None, committee_name="Test Committee")
        assert get_display_name(report) == "Test Committee"

    def test_returns_unknown_when_both_missing(self):
        """Test fallback to 'Unknown' when both names are missing."""
        report = make_test_report(candidate_name=None, committee_name=None)
        assert get_display_name(report) == "Unknown"

    def test_returns_committee_when_candidate_empty_string(self):
        """Test that empty string candidate falls back to committee."""
        report = make_test_report(candidate_name="", committee_name="Test Committee")
        assert get_display_name(report) == "Test Committee"


class TestProcessingResult:
    """Tests for ProcessingResult dataclass."""

    def test_creation(self):
        """Test ProcessingResult creation."""
        result = ProcessingResult(
            committees_processed=5,
            emails_sent=3,
            errors=["Error 1", "Error 2"],
        )
        assert result.committees_processed == 5
        assert result.emails_sent == 3
        assert len(result.errors) == 2

    def test_empty_errors(self):
        """Test ProcessingResult with empty errors."""
        result = ProcessingResult(committees_processed=1, emails_sent=1, errors=[])
        assert result.errors == []


class TestReportService:
    """Tests for ReportService class."""

    @pytest.fixture
    def mock_blob_service(self):
        """Create a mock blob storage service."""
        return MagicMock()

    @pytest.fixture
    def mock_analysis_service(self):
        """Create a mock analysis service."""
        service = MagicMock()
        service.generate_summary.return_value = "AI generated summary"
        return service

    @pytest.fixture
    def mock_email_service(self):
        """Create a mock email service."""
        service = MagicMock()
        service.send_report_email.return_value = EmailResult(
            success=True,
            message_id="test-message-id",
        )
        return service

    @pytest.fixture
    def report_service(self, mock_blob_service, mock_analysis_service, mock_email_service):
        """Create a ReportService with mocked dependencies."""
        return ReportService(
            blob_service=mock_blob_service,
            analysis_service=mock_analysis_service,
            email_service=mock_email_service,
        )

    def test_init(self, mock_blob_service, mock_analysis_service, mock_email_service):
        """Test ReportService initialization."""
        service = ReportService(
            blob_service=mock_blob_service,
            analysis_service=mock_analysis_service,
            email_service=mock_email_service,
        )
        assert service.blob_service is mock_blob_service
        assert service.analysis_service is mock_analysis_service
        assert service.email_service is mock_email_service

    def test_process_committees_empty_list(self, report_service):
        """Test processing empty list of committees."""
        result = report_service.process_committees([], ["test@example.com"])

        assert result.committees_processed == 0
        assert result.emails_sent == 0
        assert result.errors == []

    def test_process_committees_no_report_found(self, report_service, mock_blob_service):
        """Test processing when no report is found in storage."""
        mock_blob_service.download_bytes.return_value = None

        result = report_service.process_committees(["C00123456"], ["test@example.com"])

        assert result.committees_processed == 0
        assert result.emails_sent == 0
        assert len(result.errors) == 1
        assert "No report in storage" in result.errors[0]

    def test_process_committees_successful(
        self,
        report_service,
        mock_blob_service,
        mock_analysis_service,
        mock_email_service,
    ):
        """Test successful processing of committees."""
        # Create report data that can be parsed as JSON
        report_data = {
            "committee_id": "C00123456",
            "committee_name": "Test Committee",
            "candidate_name": None,
        }
        mock_blob_service.download_bytes.return_value = json.dumps(report_data).encode()

        result = report_service.process_committees(["C00123456"], ["test@example.com"])

        assert result.committees_processed == 1
        assert result.emails_sent == 1
        assert result.errors == []

        # Verify email was sent
        mock_email_service.send_report_email.assert_called_once()

    def test_process_committees_email_failure(
        self,
        report_service,
        mock_blob_service,
        mock_email_service,
    ):
        """Test processing when email sending fails."""
        report_data = {
            "committee_id": "C00123456",
            "committee_name": "Test Committee",
        }
        mock_blob_service.download_bytes.return_value = json.dumps(report_data).encode()
        mock_email_service.send_report_email.return_value = EmailResult(
            success=False,
            error="SMTP connection failed",
        )

        result = report_service.process_committees(["C00123456"], ["test@example.com"])

        assert result.committees_processed == 1
        assert result.emails_sent == 0
        assert len(result.errors) == 1
        assert "Email failed" in result.errors[0]

    def test_process_committees_multiple(
        self,
        report_service,
        mock_blob_service,
        mock_email_service,
    ):
        """Test processing multiple committees."""
        report_data = {
            "committee_id": "C00123456",
            "committee_name": "Test Committee",
        }
        mock_blob_service.download_bytes.return_value = json.dumps(report_data).encode()

        result = report_service.process_committees(
            ["C00123456", "C00789012", "C00345678"],
            ["test@example.com"],
        )

        assert result.committees_processed == 3
        assert result.emails_sent == 3
        assert mock_email_service.send_report_email.call_count == 3

    def test_process_committees_exception_handling(
        self,
        report_service,
        mock_blob_service,
    ):
        """Test that exceptions in storage are logged and report is skipped."""
        # Exception in storage read is caught and returns None,
        # which is then recorded as "No report in storage"
        mock_blob_service.download_bytes.side_effect = Exception("Storage error")

        result = report_service.process_committees(["C00123456"], ["test@example.com"])

        assert result.committees_processed == 0
        assert result.emails_sent == 0
        assert len(result.errors) == 1
        assert "C00123456" in result.errors[0]
        # Error is recorded as "No report in storage" since the exception
        # was caught in _read_report_from_storage
        assert "No report in storage" in result.errors[0]

    def test_read_report_from_storage_success(self, report_service, mock_blob_service):
        """Test reading report from storage successfully."""
        report_data = {
            "committee_id": "C00123456",
            "committee_name": "Test Committee",
            "total_receipts": 100000.0,
        }
        mock_blob_service.download_bytes.return_value = json.dumps(report_data).encode()

        result = report_service._read_report_from_storage("C00123456")

        assert result is not None
        assert result.committee_name == "Test Committee"
        mock_blob_service.download_bytes.assert_called_once_with("reports/C00123456.json")

    def test_read_report_from_storage_not_found(self, report_service, mock_blob_service):
        """Test reading report that doesn't exist."""
        mock_blob_service.download_bytes.return_value = None

        result = report_service._read_report_from_storage("C00123456")

        assert result is None

    def test_read_report_from_storage_exception(self, report_service, mock_blob_service):
        """Test reading report when exception occurs."""
        mock_blob_service.download_bytes.side_effect = Exception("Connection error")

        result = report_service._read_report_from_storage("C00123456")

        assert result is None

    def test_generate_summary_delegates_to_analysis_service(
        self, report_service, mock_analysis_service
    ):
        """Test that summary generation is delegated to analysis service."""
        report = make_test_report()

        result = report_service._generate_summary(report)

        assert result == "AI generated summary"
        mock_analysis_service.generate_summary.assert_called_once_with(report)
