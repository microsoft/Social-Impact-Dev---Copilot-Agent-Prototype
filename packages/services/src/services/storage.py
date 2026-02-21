from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Protocol
from urllib.parse import unquote

from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, ContentSettings


@dataclass
class BlobPathComponents:
    """Parsed components from a blob path like 'C00718866/2024-Q1/report.json'."""

    committee_id: str
    """The FEC committee ID (e.g., 'C00718866')."""

    year_quarter: str
    """The year and quarter (e.g., '2024-Q1')."""

    filename: str
    """The filename (e.g., 'report.json')."""

    @property
    def base_path(self) -> str:
        """The base path without filename (e.g., 'C00718866/2024-Q1')."""
        return f"{self.committee_id}/{self.year_quarter}"


def parse_blob_path(blob_path: str) -> BlobPathComponents | None:
    """Parse a blob path into its components.

    Args:
        blob_path: A blob path like 'C00718866/2024-Q1/report.json'

    Returns:
        BlobPathComponents with committee_id, year_quarter, and filename,
        or None if the path doesn't have enough parts.
    """
    parts = blob_path.split("/")
    if len(parts) < 3:
        return None

    return BlobPathComponents(
        committee_id=parts[0],
        year_quarter=parts[1],
        filename="/".join(parts[2:]),  # Handle nested paths like 'subdir/file.csv'
    )


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

    def parse_blob_path_from_url(self, blob_url: str) -> str | None: ...


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
        if not blob_client.exists():
            return None
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

    def parse_blob_path_from_url(self, blob_url: str) -> str | None:
        """Extract the blob path from an Event Grid blob URL.

        Args:
            blob_url: Full blob URL from Event Grid event data
                (e.g., "https://account.blob.core.windows.net/container/path/to/blob")

        Returns:
            The blob path within the container (e.g., "path/to/blob"), or None if invalid.
        """
        if not self.container_name:
            return None

        # URL decode to handle any encoded characters
        blob_url = unquote(blob_url)

        # Extract the path after the container name
        container_marker = f"/{self.container_name}/"
        if container_marker not in blob_url:
            return None

        return blob_url.split(container_marker, 1)[1]
