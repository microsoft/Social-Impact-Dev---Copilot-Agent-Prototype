from unittest.mock import MagicMock, patch

import pytest
from services import AzureBlobStorageService


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
