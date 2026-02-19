from __future__ import annotations

from unittest.mock import MagicMock, Mock

import pytest
from fec_api_client import Filings
from services.report.sync import SyncService


@pytest.fixture
def mock_fec_client():
    return MagicMock()


@pytest.fixture
def mock_blob_service():
    service = MagicMock()
    service.exists.return_value = False
    service.download_bytes.return_value = None
    return service


@pytest.fixture
def mock_http_client():
    return MagicMock()


# sync_reports tests


def test_sync_reports_no_committees(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        committee_ids=None,
    )
    result = service.sync_reports()
    assert result == {}
    mock_fec_client.get_v1_filings.assert_not_called()


def test_sync_reports_stores_reports(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        committee_ids=["C00000001", "C00000002"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [
            {
                "file_number": 12345,
                "committee_name": "Test Committee",
                "report_year": 2024,
                "report_type": "Q1",
            }
        ]
    }
    mock_fec_client.get_v1_filings.return_value = mock_response

    mock_blob_service.exists.return_value = False  # Report doesn't exist yet

    result = service.sync_reports()

    assert "C00000001" in result
    assert "C00000002" in result
    assert result["C00000001"] is not None
    assert result["C00000001"].file_number == 12345

    # Verify reports were stored with new path structure
    upload_calls = mock_blob_service.upload_bytes.call_args_list
    report_calls = [c for c in upload_calls if c[0][0].endswith("/report.json")]
    assert len(report_calls) == 2


def test_sync_reports_handles_missing(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        committee_ids=["C00000001"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": []}
    mock_fec_client.get_v1_filings.return_value = mock_response

    result = service.sync_reports()

    assert result["C00000001"] is None


def test_sync_reports_handles_api_error(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        committee_ids=["C00000001"],
    )

    mock_response = Mock()
    mock_response.status_code = 500
    mock_fec_client.get_v1_filings.return_value = mock_response

    result = service.sync_reports()

    assert result["C00000001"] is None


def test_sync_reports_uses_custom_report_types(
    mock_fec_client, mock_blob_service, mock_http_client
):
    api_key = "test-api-key"
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        committee_ids=["C00000001"],
        report_types=["Q1", "Q2"],
        api_key=api_key,
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": []}
    mock_fec_client.get_v1_filings.return_value = mock_response

    service.sync_reports()

    mock_fec_client.get_v1_filings.assert_called_with(
        committee_id=["C00000001"],
        report_type=["Q1", "Q2"],
        sort=["-receipt_date"],
        per_page=1,
        api_key=api_key,
    )


def test_sync_reports_downloads_files(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        committee_ids=["C00000001"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [
            {
                "file_number": 12345,
                "csv_url": "https://docquery.fec.gov/csv/12345.csv",
                "pdf_url": "https://docquery.fec.gov/pdf/12345.pdf",
            }
        ]
    }
    mock_fec_client.get_v1_filings.return_value = mock_response

    mock_blob_service.exists.return_value = False
    file_response = Mock()
    file_response.content = b"data"
    mock_http_client.get.return_value = file_response

    service.sync_reports()

    # Should download CSV only (PDF uses original FEC URL)
    assert mock_http_client.get.call_count == 1


# _process_filing tests


def test_process_filing_no_urls(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )
    filing = Filings.from_dict({})
    result = service._process_filing("C00123456/2024-Q1", filing)
    assert result == 0


def test_process_filing_with_csv_and_pdf(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )
    mock_blob_service.exists.return_value = False

    # Mock CSV response with valid FEC CSV content
    csv_content = (
        b'"HDR","FEC","8.0","Test","1.0","",""\n'
        b'"SA11AI","C00123456","TX001","","","IND","","DOE","JOHN","","","","123 MAIN ST",'
        b'"","CITY","TX","12345","P2024","","20240101","100.00","100.00","","CONTRIBUTION",'
        b'"ACME","ENGINEER","","","","","","","","","","","","","","","","",""'
    )

    mock_response = Mock()
    mock_response.content = csv_content
    mock_response.raise_for_status = Mock()
    mock_http_client.get.return_value = mock_response

    filing = Filings.from_dict(
        {
            "file_number": 12345,
            "csv_url": "https://docquery.fec.gov/csv/12345.csv",
            "pdf_url": "https://docquery.fec.gov/pdf/12345.pdf",
        }
    )

    result = service._process_filing("C00123456/2024-Q1", filing)
    # 2 files: formatted CSV and XLSX (PDF/raw CSV use original FEC URL)
    assert result == 2
    assert mock_http_client.get.call_count == 1


def test_download_file_blocks_untrusted_domains(
    mock_fec_client, mock_blob_service, mock_http_client
):
    """Test that SSRF protection blocks downloads from untrusted domains."""
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )

    # Untrusted domain should be blocked
    result = service._download_file("https://evil.com/malicious.csv")
    assert result is None
    mock_http_client.get.assert_not_called()

    # FEC domain should be allowed
    mock_response = Mock()
    mock_response.content = b"data"
    mock_response.raise_for_status = Mock()
    mock_http_client.get.return_value = mock_response

    result = service._download_file("https://docquery.fec.gov/csv/12345.csv")
    assert result == b"data"
    mock_http_client.get.assert_called_once()


def test_download_file_blocks_invalid_schemes(mock_fec_client, mock_blob_service, mock_http_client):
    """Test that SSRF protection blocks non-HTTP(S) schemes."""
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )

    # File scheme should be blocked
    result = service._download_file("file:///etc/passwd")
    assert result is None
    mock_http_client.get.assert_not_called()
