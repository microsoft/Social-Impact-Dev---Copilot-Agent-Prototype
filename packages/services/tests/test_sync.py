from __future__ import annotations

from unittest.mock import MagicMock, Mock

import pytest
from services.sync import SyncService


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


# sync_candidate_reports tests


def test_sync_candidate_reports_no_candidates(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        candidate_ids=None,
    )
    result = service.sync_candidate_reports()
    assert result == {}
    mock_fec_client.get_v1_filings.assert_not_called()


def test_sync_candidate_reports_stores_reports(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        candidate_ids=["P00001", "P00002"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [{"file_number": 12345, "candidate_name": "Test Candidate"}]
    }
    mock_fec_client.get_v1_filings.return_value = mock_response

    mock_blob_service.exists.return_value = True  # Skip file downloads

    result = service.sync_candidate_reports()

    assert "P00001" in result
    assert "P00002" in result
    assert result["P00001"]["file_number"] == 12345

    # Verify reports were stored
    upload_calls = mock_blob_service.upload_bytes.call_args_list
    report_calls = [c for c in upload_calls if c[0][0].startswith("reports/")]
    assert len(report_calls) == 2


def test_sync_candidate_reports_handles_missing(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        candidate_ids=["P00001"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": []}
    mock_fec_client.get_v1_filings.return_value = mock_response

    result = service.sync_candidate_reports()

    assert result["P00001"] is None


def test_sync_candidate_reports_handles_api_error(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        candidate_ids=["P00001"],
    )

    mock_response = Mock()
    mock_response.status_code = 500
    mock_fec_client.get_v1_filings.return_value = mock_response

    result = service.sync_candidate_reports()

    assert result["P00001"] is None


def test_sync_candidate_reports_uses_custom_report_types(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        candidate_ids=["P00001"],
        report_types=["Q1", "Q2"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": []}
    mock_fec_client.get_v1_filings.return_value = mock_response

    service.sync_candidate_reports()

    mock_fec_client.get_v1_filings.assert_called_with(
        candidate_id=["P00001"],
        report_type=["Q1", "Q2"],
        sort=["-receipt_date"],
        per_page=1,
    )


def test_sync_candidate_reports_downloads_files(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
        candidate_ids=["P00001"],
    )

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [{
            "file_number": 12345,
            "csv_url": "https://example.com/12345.csv",
            "pdf_url": "https://example.com/12345.pdf",
        }]
    }
    mock_fec_client.get_v1_filings.return_value = mock_response

    mock_blob_service.exists.return_value = False
    file_response = Mock()
    file_response.content = b"data"
    mock_http_client.get.return_value = file_response

    service.sync_candidate_reports()

    # Should download CSV and PDF
    assert mock_http_client.get.call_count == 2


# _download_and_store_file tests


def test_download_skips_existing_blob(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )
    mock_blob_service.exists.return_value = True
    result = service._download_and_store_file(
        "https://example.com/file.csv",
        "filings/123/123.csv",
        "text/csv",
    )
    assert result is False
    mock_http_client.get.assert_not_called()


def test_download_stores_new_file(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )
    mock_blob_service.exists.return_value = False
    mock_response = Mock()
    mock_response.content = b"csv,data"
    mock_http_client.get.return_value = mock_response

    result = service._download_and_store_file(
        "https://example.com/file.csv",
        "filings/123/123.csv",
        "text/csv",
    )

    assert result is True
    mock_http_client.get.assert_called_once_with("https://example.com/file.csv")
    mock_blob_service.upload_bytes.assert_called_once_with(
        "filings/123/123.csv",
        b"csv,data",
        content_type="text/csv",
    )


# _process_filing tests


def test_process_filing_no_file_number(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )
    result = service._process_filing({})
    assert result == 0


def test_process_filing_with_csv_and_pdf(mock_fec_client, mock_blob_service, mock_http_client):
    service = SyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )
    mock_blob_service.exists.return_value = False
    mock_response = Mock()
    mock_response.content = b"data"
    mock_http_client.get.return_value = mock_response

    filing = {
        "file_number": 12345,
        "csv_url": "https://example.com/12345.csv",
        "pdf_url": "https://example.com/12345.pdf",
    }

    result = service._process_filing(filing)
    assert result == 2
    assert mock_http_client.get.call_count == 2
