from __future__ import annotations

from unittest.mock import MagicMock, Mock

import pytest
from services.file_sync import METADATA_BLOB_PATH, FileSyncService, SyncResult


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


@pytest.fixture
def sync_service(mock_fec_client, mock_blob_service, mock_http_client):
    return FileSyncService(
        fec_client=mock_fec_client,
        blob_service=mock_blob_service,
        http_client=mock_http_client,
    )


# SyncResult tests


def test_sync_result_creation():
    result = SyncResult(
        last_sync_date="2024-01-15",
        filings_processed=42,
        files_uploaded=10,
    )
    assert result.last_sync_date == "2024-01-15"
    assert result.filings_processed == 42
    assert result.files_uploaded == 10


# get_last_sync tests


def test_get_last_sync_no_metadata(sync_service, mock_blob_service):
    mock_blob_service.download_bytes.return_value = None
    assert sync_service.get_last_sync() is None


def test_get_last_sync_with_metadata(sync_service, mock_blob_service):
    mock_blob_service.download_bytes.return_value = b'{"last_checked_date": "2024-01-10"}'
    assert sync_service.get_last_sync() == "2024-01-10"


def test_get_last_sync_exception(sync_service, mock_blob_service):
    mock_blob_service.download_bytes.side_effect = Exception("Not found")
    assert sync_service.get_last_sync() is None


# sync tests


def test_sync_single_page(sync_service, mock_fec_client, mock_blob_service):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [{"file_number": 1}, {"file_number": 2}],
        "pagination": {"pages": 1},
    }
    mock_fec_client.get_v1_filings.return_value = mock_response

    result = sync_service.sync(since_date="2024-01-01")

    assert result.filings_processed == 2
    mock_fec_client.get_v1_filings.assert_called_once()
    mock_blob_service.ensure_container_exists.assert_called_once()


def test_sync_multiple_pages(sync_service, mock_fec_client, mock_blob_service):
    page1_response = Mock()
    page1_response.status_code = 200
    page1_response.json.return_value = {
        "results": [{"file_number": 1}],
        "pagination": {"pages": 2},
    }

    page2_response = Mock()
    page2_response.status_code = 200
    page2_response.json.return_value = {
        "results": [{"file_number": 2}],
        "pagination": {"pages": 2},
    }

    mock_fec_client.get_v1_filings.side_effect = [page1_response, page2_response]

    result = sync_service.sync(since_date="2024-01-01")

    assert result.filings_processed == 2
    assert mock_fec_client.get_v1_filings.call_count == 2


def test_sync_uses_last_sync_if_no_date_provided(sync_service, mock_fec_client, mock_blob_service):
    mock_blob_service.download_bytes.return_value = b'{"last_checked_date": "2024-01-05"}'

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"results": [], "pagination": {"pages": 1}}
    mock_fec_client.get_v1_filings.return_value = mock_response

    sync_service.sync()

    mock_fec_client.get_v1_filings.assert_called_with(
        min_receipt_date="2024-01-05",
        page=1,
        per_page=100,
    )


# _download_and_store_file tests


def test_download_skips_existing_blob(sync_service, mock_blob_service, mock_http_client):
    mock_blob_service.exists.return_value = True
    result = sync_service._download_and_store_file(
        "https://example.com/file.csv",
        "filings/123/123.csv",
        "text/csv",
    )
    assert result is False
    mock_http_client.get.assert_not_called()


def test_download_stores_new_file(sync_service, mock_blob_service, mock_http_client):
    mock_blob_service.exists.return_value = False
    mock_response = Mock()
    mock_response.content = b"csv,data"
    mock_http_client.get.return_value = mock_response

    result = sync_service._download_and_store_file(
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


def test_process_filing_no_file_number(sync_service):
    result = sync_service._process_filing({})
    assert result == 0


def test_process_filing_with_csv_and_pdf(sync_service, mock_blob_service, mock_http_client):
    mock_blob_service.exists.return_value = False
    mock_response = Mock()
    mock_response.content = b"data"
    mock_http_client.get.return_value = mock_response

    filing = {
        "file_number": 12345,
        "csv_url": "https://example.com/12345.csv",
        "pdf_url": "https://example.com/12345.pdf",
    }

    result = sync_service._process_filing(filing)
    assert result == 2
    assert mock_http_client.get.call_count == 2


# Full sync flow test


def test_full_sync_flow(sync_service, mock_fec_client, mock_blob_service, mock_http_client):
    mock_blob_service.download_bytes.return_value = None
    mock_blob_service.exists.return_value = False

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "results": [
            {
                "file_number": 1,
                "csv_url": "https://example.com/1.csv",
                "pdf_url": "https://example.com/1.pdf",
            }
        ],
        "pagination": {"pages": 1},
    }
    mock_fec_client.get_v1_filings.return_value = mock_response

    file_response = Mock()
    file_response.content = b"data"
    mock_http_client.get.return_value = file_response

    result = sync_service.sync()

    assert result.filings_processed == 1
    assert result.files_uploaded == 2
    assert result.last_sync_date is not None

    # Verify metadata was saved
    save_calls = [
        c for c in mock_blob_service.upload_bytes.call_args_list if c[0][0] == METADATA_BLOB_PATH
    ]
    assert len(save_calls) == 1
