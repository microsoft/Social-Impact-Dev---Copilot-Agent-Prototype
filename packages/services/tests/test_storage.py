from unittest.mock import MagicMock, patch

import pytest
from services import AzureBlobStorageService, BlobPathComponents, parse_blob_path


@pytest.fixture
def mock_blob_service_client():
    with patch("services.storage.BlobServiceClient") as mock:
        yield mock


@pytest.fixture
def mock_default_credential():
    with patch("services.storage.DefaultAzureCredential") as mock:
        yield mock


def test_init_with_connection_string(mock_blob_service_client):
    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    mock_blob_service_client.from_connection_string.assert_called_once_with(
        "DefaultEndpointsProtocol=https;AccountName=test"
    )
    assert service.container_name == "test-container"


def test_init_with_account_url_and_system_assigned_mi(
    mock_blob_service_client, mock_default_credential
):
    _service = AzureBlobStorageService(
        account_url="https://testaccount.blob.core.windows.net",
        container_name="test-container",
    )
    mock_default_credential.assert_called_once_with()
    mock_blob_service_client.assert_called_once_with(
        account_url="https://testaccount.blob.core.windows.net",
        credential=mock_default_credential.return_value,
    )


def test_init_with_account_url_and_user_assigned_mi(
    mock_blob_service_client, mock_default_credential
):
    _service = AzureBlobStorageService(
        account_url="https://testaccount.blob.core.windows.net",
        container_name="test-container",
        managed_identity_client_id="00000000-0000-0000-0000-000000000000",
    )
    mock_default_credential.assert_called_once_with(
        managed_identity_client_id="00000000-0000-0000-0000-000000000000"
    )


def test_init_from_env_vars(mock_blob_service_client, monkeypatch):
    monkeypatch.setenv("BLOB_ACCOUNT_URL", "https://envaccount.blob.core.windows.net")
    monkeypatch.setenv("BLOB_CONTAINER_NAME", "env-container")
    monkeypatch.setenv(
        "AZURE_STORAGE_CONNECTION_STRING",
        "DefaultEndpointsProtocol=https;AccountName=env",
    )

    service = AzureBlobStorageService()
    assert service.account_url == "https://envaccount.blob.core.windows.net"
    assert service.container_name == "env-container"
    mock_blob_service_client.from_connection_string.assert_called_once()


def test_init_raises_without_account_url_or_connection_string():
    with pytest.raises(
        ValueError, match="Either account_url or connection_string must be provided"
    ):
        AzureBlobStorageService(container_name="test")


def test_ensure_container_exists():
    mock_client = MagicMock()
    mock_container = MagicMock()
    mock_container.exists.return_value = False
    mock_client.get_container_client.return_value = mock_container

    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    service._client = mock_client
    service.ensure_container_exists()

    mock_client.get_container_client.assert_called_once_with("test-container")
    mock_container.exists.assert_called_once()
    mock_container.create_container.assert_called_once()


def test_upload_bytes():
    mock_client = MagicMock()
    mock_blob = MagicMock()
    mock_blob.url = "https://testaccount.blob.core.windows.net/container/test.txt"
    mock_client.get_blob_client.return_value = mock_blob

    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    service._client = mock_client

    url = service.upload_bytes("test.txt", b"Hello, Azure!", content_type="text/plain")

    assert url == "https://testaccount.blob.core.windows.net/container/test.txt"
    mock_client.get_blob_client.assert_called_once_with(container="test-container", blob="test.txt")
    call_args = mock_blob.upload_blob.call_args
    assert call_args.args == (b"Hello, Azure!",)
    assert call_args.kwargs["overwrite"] is True
    assert call_args.kwargs["content_settings"].content_type == "text/plain"


def test_download_bytes():
    mock_client = MagicMock()
    mock_blob = MagicMock()
    mock_download = MagicMock()
    mock_download.readall.return_value = b"blob content"
    mock_blob.download_blob.return_value = mock_download
    mock_client.get_blob_client.return_value = mock_blob

    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    service._client = mock_client

    content = service.download_bytes("test.txt")

    assert content == b"blob content"
    mock_client.get_blob_client.assert_called_once_with(container="test-container", blob="test.txt")
    mock_blob.download_blob.assert_called_once()


def test_list_blobs():
    mock_client = MagicMock()
    mock_container = MagicMock()
    mock_blob1 = MagicMock()
    mock_blob1.name = "file1.txt"
    mock_blob2 = MagicMock()
    mock_blob2.name = "file2.txt"
    mock_container.list_blobs.return_value = [mock_blob1, mock_blob2]
    mock_client.get_container_client.return_value = mock_container

    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    service._client = mock_client

    blobs = service.list_blobs(prefix="file")

    assert blobs == ["file1.txt", "file2.txt"]
    mock_container.list_blobs.assert_called_once_with(name_starts_with="file")


def test_exists_returns_true():
    mock_client = MagicMock()
    mock_blob = MagicMock()
    mock_blob.exists.return_value = True
    mock_client.get_blob_client.return_value = mock_blob

    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    service._client = mock_client

    assert service.exists("test.txt") is True
    mock_blob.exists.assert_called_once()


def test_exists_returns_false():
    mock_client = MagicMock()
    mock_blob = MagicMock()
    mock_blob.exists.return_value = False
    mock_client.get_blob_client.return_value = mock_blob

    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="test-container",
    )
    service._client = mock_client

    assert service.exists("test.txt") is False


# Tests for parse_blob_path and BlobPathComponents


def test_parse_blob_path_standard_path():
    result = parse_blob_path("C00718866/2024-Q1/report.json")

    assert result is not None
    assert result.committee_id == "C00718866"
    assert result.year_quarter == "2024-Q1"
    assert result.filename == "report.json"
    assert result.base_path == "C00718866/2024-Q1"


def test_parse_blob_path_with_nested_filename():
    result = parse_blob_path("C00718866/2024-Q1/subdir/data.csv")

    assert result is not None
    assert result.committee_id == "C00718866"
    assert result.year_quarter == "2024-Q1"
    assert result.filename == "subdir/data.csv"
    assert result.base_path == "C00718866/2024-Q1"


def test_parse_blob_path_returns_none_for_short_path():
    assert parse_blob_path("C00718866/2024-Q1") is None
    assert parse_blob_path("C00718866") is None
    assert parse_blob_path("") is None


def test_parse_blob_path_with_different_committee_ids():
    result = parse_blob_path("C00000001/2023-Q4/summary.xlsx")

    assert result is not None
    assert result.committee_id == "C00000001"
    assert result.year_quarter == "2023-Q4"
    assert result.filename == "summary.xlsx"


def test_blob_path_components_base_path_property():
    components = BlobPathComponents(
        committee_id="C00718866",
        year_quarter="2024-Q1",
        filename="report.json",
    )

    assert components.base_path == "C00718866/2024-Q1"


# Tests for parse_blob_path_from_url


def test_parse_blob_path_from_url_standard():
    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="fec-filings",
    )

    url = "https://account.blob.core.windows.net/fec-filings/C00718866/2024-Q1/report.json"
    result = service.parse_blob_path_from_url(url)

    assert result == "C00718866/2024-Q1/report.json"


def test_parse_blob_path_from_url_with_encoded_characters():
    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="fec-filings",
    )

    url = "https://account.blob.core.windows.net/fec-filings/C00718866/2024-Q1/file%20name.csv"
    result = service.parse_blob_path_from_url(url)

    assert result == "C00718866/2024-Q1/file name.csv"


def test_parse_blob_path_from_url_wrong_container():
    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name="fec-filings",
    )

    url = "https://account.blob.core.windows.net/other-container/C00718866/2024-Q1/report.json"
    result = service.parse_blob_path_from_url(url)

    assert result is None


def test_parse_blob_path_from_url_no_container_name():
    service = AzureBlobStorageService(
        connection_string="DefaultEndpointsProtocol=https;AccountName=test",
        container_name=None,
    )
    service.container_name = None  # Override after init

    url = "https://account.blob.core.windows.net/fec-filings/C00718866/2024-Q1/report.json"
    result = service.parse_blob_path_from_url(url)

    assert result is None
