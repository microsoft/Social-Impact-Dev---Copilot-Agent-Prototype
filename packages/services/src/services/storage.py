from __future__ import annotations

import os
from typing import Protocol

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContentSettings


class BlobStorageService(Protocol):
    def ensure_container_exists(self) -> None: ...

    def upload_bytes(
        self,
        blob_name: str,
        data: bytes,
        *,
        content_type: str | None = None,
        overwrite: bool = True,
    ) -> str: ...

    def download_bytes(self, blob_name: str) -> bytes | None: ...

    def list_blobs(self, prefix: str | None = None) -> list[str]: ...

    def exists(self, blob_name: str) -> bool: ...


class AzureBlobStorageService:
    def __init__(
        self,
        account_url: str | None = None,
        container_name: str | None = None,
        managed_identity_client_id: str | None = None,
        connection_string: str | None = None,
    ) -> None:
        self.account_url = account_url or os.getenv("BLOB_ACCOUNT_URL")
        self.container_name = container_name or os.getenv("BLOB_CONTAINER_NAME")
        self.connection_string = connection_string or os.getenv("AZURE_STORAGE_CONNECTION_STRING")
        self.managed_identity_client_id = managed_identity_client_id or os.getenv("AZURE_CLIENT_ID")

        if self.connection_string:
            self._client = BlobServiceClient.from_connection_string(self.connection_string)
        elif self.account_url:
            credential = (
                DefaultAzureCredential(managed_identity_client_id=self.managed_identity_client_id)
                if self.managed_identity_client_id
                else DefaultAzureCredential()
            )
            self._client = BlobServiceClient(account_url=self.account_url, credential=credential)
        else:
            raise ValueError("Either account_url or connection_string must be provided")

    def ensure_container_exists(self) -> None:
        if not self.container_name:
            raise ValueError("container_name must be set")
        container_client = self._client.get_container_client(self.container_name)
        if not container_client.exists():
            container_client.create_container()

    def upload_bytes(
        self,
        blob_name: str,
        data: bytes,
        *,
        content_type: str | None = None,
        overwrite: bool = True,
    ) -> str:
        if not self.container_name:
            raise ValueError("container_name must be set")
        blob_client = self._client.get_blob_client(container=self.container_name, blob=blob_name)
        content_settings = ContentSettings(content_type=content_type) if content_type else None
        blob_client.upload_blob(data, overwrite=overwrite, content_settings=content_settings)
        return blob_client.url

    def download_bytes(self, blob_name: str) -> bytes | None:
        if not self.container_name:
            raise ValueError("container_name must be set")
        blob_client = self._client.get_blob_client(container=self.container_name, blob=blob_name)
        blob = blob_client.download_blob().readall()
        if isinstance(blob, bytes):
            return blob
        if isinstance(blob, str):
            return blob.encode()
        return None

    def list_blobs(self, prefix: str | None = None) -> list[str]:
        if not self.container_name:
            raise ValueError("container_name must be set")
        container_client = self._client.get_container_client(self.container_name)
        return [blob.name for blob in container_client.list_blobs(name_starts_with=prefix)]

    def exists(self, blob_name: str) -> bool:
        if not self.container_name:
            raise ValueError("container_name must be set")
        blob_client = self._client.get_blob_client(container=self.container_name, blob=blob_name)
        return blob_client.exists()
