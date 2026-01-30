from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import UTC, datetime

import httpx

from .storage import BlobStorageService

logger = logging.getLogger(__name__)

METADATA_BLOB_PATH = "metadata/last_check.json"


@dataclass
class SyncResult:
    """Result of a filing sync operation."""

    last_sync_date: str
    filings_processed: int
    files_uploaded: int


class FileSyncService:
    """Service for syncing FEC filings to blob storage."""

    def __init__(
        self,
        fec_client,
        blob_service: BlobStorageService,
        http_client: httpx.Client | None = None,
    ) -> None:
        self.fec_client = fec_client
        self.blob_service = blob_service
        self.http_client = http_client or httpx.Client(timeout=60.0)

    def get_last_sync(self) -> str | None:
        """Get the last sync date from metadata, or None if never synced."""
        try:
            data = self.blob_service.download_bytes(METADATA_BLOB_PATH)
            if data:
                import json

                metadata = json.loads(data)
                return metadata.get("last_checked_date")
        except Exception as e:
            logger.info(f"No existing metadata found: {e}")
        return None

    def sync(self, since_date: str | None = None) -> SyncResult:
        """
        Sync filings from FEC API to blob storage.

        Args:
            since_date: Only fetch filings received on or after this date (YYYY-MM-DD).
                       If None, uses the last sync date from metadata.

        Returns:
            SyncResult with summary of the operation.
        """
        self.blob_service.ensure_container_exists()

        if since_date is None:
            since_date = self.get_last_sync()

        logger.info(f"Syncing filings since: {since_date}")

        filings = self._fetch_all_filings(since_date)
        logger.info(f"Found {len(filings)} filings to process")

        files_uploaded = 0
        for filing in filings:
            files_uploaded += self._process_filing(filing)

        today = datetime.now(UTC).strftime("%Y-%m-%d")
        self._save_metadata(today, len(filings))

        logger.info(f"Sync complete: {len(filings)} filings, {files_uploaded} files uploaded")

        return SyncResult(
            last_sync_date=today,
            filings_processed=len(filings),
            files_uploaded=files_uploaded,
        )

    def _fetch_all_filings(self, min_receipt_date: str | None = None) -> list[dict]:
        """Fetch all filings from FEC API, handling pagination."""
        all_results: list[dict] = []
        page = 1
        per_page = 100

        while True:
            response = self.fec_client.get_v1_filings(
                min_receipt_date=min_receipt_date,
                page=page,
                per_page=per_page,
            )

            if response.status_code != 200:
                logger.error(f"FEC API error: {response.status_code} - {response.text}")
                break

            data = response.json()
            results = data.get("results", [])
            all_results.extend(results)

            pagination = data.get("pagination", {})
            total_pages = pagination.get("pages", 1)

            logger.info(f"Fetched page {page}/{total_pages}, got {len(results)} filings")

            if page >= total_pages:
                break
            page += 1

        return all_results

    def _download_and_store_file(
        self,
        url: str,
        blob_path: str,
        content_type: str,
    ) -> bool:
        """Download a file from URL and store in blob storage if not exists."""
        if self.blob_service.exists(blob_path):
            logger.debug(f"Blob already exists: {blob_path}")
            return False

        try:
            response = self.http_client.get(url)
            response.raise_for_status()
            self.blob_service.upload_bytes(
                blob_path,
                response.content,
                content_type=content_type,
            )
            logger.info(f"Uploaded: {blob_path}")
            return True
        except httpx.HTTPError as e:
            logger.warning(f"Failed to download {url}: {e}")
            return False

    def _process_filing(self, filing: dict) -> int:
        """Process a single filing, downloading CSV and PDF if available."""
        file_number = filing.get("file_number")
        if not file_number:
            return 0

        files_uploaded = 0
        base_path = f"filings/{file_number}"

        csv_url = filing.get("csv_url")
        if csv_url:
            if self._download_and_store_file(csv_url, f"{base_path}/{file_number}.csv", "text/csv"):
                files_uploaded += 1

        pdf_url = filing.get("pdf_url")
        if pdf_url:
            if self._download_and_store_file(
                pdf_url, f"{base_path}/{file_number}.pdf", "application/pdf"
            ):
                files_uploaded += 1

        return files_uploaded

    def _save_metadata(self, last_checked_date: str, filings_processed: int) -> None:
        """Save sync metadata to blob storage."""
        import json

        metadata = {
            "last_checked_date": last_checked_date,
            "last_run_timestamp": datetime.now(UTC).isoformat(),
            "filings_processed": filings_processed,
        }
        self.blob_service.upload_bytes(
            METADATA_BLOB_PATH,
            json.dumps(metadata).encode(),
            content_type="application/json",
        )
