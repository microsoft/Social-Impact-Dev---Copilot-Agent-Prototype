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

    def build_file_urls(self, files: list[dict]) -> list[str]: ...

    def get_metadata(self, blob_name: str) -> dict[str, str]: ...

    def set_metadata(self, blob_name: str, metadata: dict[str, str]) -> None: ...

    def mark_as_processed(self, blob_name: str) -> None: ...

    def is_processed(self, blob_name: str) -> bool: ...


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

    def build_file_urls(self, files: list[dict]) -> list[str]:
        """Build public URLs for files stored in blob storage."""
        if not self.account_url or not self.container_name:
            return []

        urls = []
        for file in files:
            if "blob_path" in file:
                url = f"{self.account_url.rstrip('/')}/{self.container_name}/{file['blob_path']}"
                urls.append(url)
            elif "file_number" in file:
                url = f"{self.account_url.rstrip('/')}/{self.container_name}/{file['file_number']}"
                urls.append(url)
        return urls

    def get_metadata(self, blob_name: str) -> dict[str, str]:
        """Get metadata for a blob."""
        if not self.container_name:
            raise ValueError("container_name must be set")
        blob_client = self._client.get_blob_client(container=self.container_name, blob=blob_name)
        properties = blob_client.get_blob_properties()
        return properties.get("metadata", {}) or {}

    def set_metadata(self, blob_name: str, metadata: dict[str, str]) -> None:
        """Set metadata for a blob."""
        if not self.container_name:
            raise ValueError("container_name must be set")
        blob_client = self._client.get_blob_client(container=self.container_name, blob=blob_name)
        blob_client.set_blob_metadata(metadata)

    def _normalize_blob_name(self, blob_name: str) -> str:
        """Extract the blob name from a full path."""
        return blob_name.split("/")[-1]

    def mark_as_processed(self, blob_name: str) -> None:
        """Mark a blob as processed by setting metadata."""
        blob_name = self._normalize_blob_name(blob_name)
        self.set_metadata(blob_name, {"processed": "true"})

    def is_processed(self, blob_name: str) -> bool:
        """Check if a blob has been marked as processed."""
        blob_name = self._normalize_blob_name(blob_name)
        try:
            metadata = self.get_metadata(blob_name)
            return metadata.get("processed") == "true"
        except Exception:
            return False
