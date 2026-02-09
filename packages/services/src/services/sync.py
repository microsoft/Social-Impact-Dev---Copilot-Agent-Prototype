from __future__ import annotations

import logging
from typing import cast

import httpx
from fec_api_client import FecApiClient, Filings, ReportTypeCode

from .storage import BlobStorageService

logger = logging.getLogger(__name__)


class SyncService:
    """Service for syncing FEC candidate filings to blob storage."""

    def __init__(
        self,
        fec_client: FecApiClient,
        blob_service: BlobStorageService,
        http_client: httpx.Client | None = None,
        candidate_ids: list[str] | None = None,
        report_types: list[ReportTypeCode] | None = None,
    ) -> None:
        self.fec_client = fec_client
        self.blob_service = blob_service
        self.http_client = http_client or httpx.Client(timeout=60.0)
        self.candidate_ids = candidate_ids or []
        self.report_types: list[ReportTypeCode] = report_types or []

    def sync(self) -> dict[str, Filings | None]:
        """Fetch and store the latest filing for each configured candidate.

        Returns:
            Dict mapping candidate_id to their latest report data (or None if not found).
        """
        if not self.candidate_ids:
            logger.warning("No candidate IDs configured")
            return {}

        self.blob_service.ensure_container_exists()
        results: dict[str, Filings | None] = {}

        for candidate_id in self.candidate_ids:
            report = self._fetch_latest(candidate_id)
            results[candidate_id] = report

            if report:
                blob_path = f"reports/{candidate_id}.json"
                self.blob_service.upload_bytes(
                    blob_path,
                    report.to_json().encode(),
                    content_type="application/json",
                )
                logger.info(f"Stored report for {candidate_id}: {blob_path}")

                self._process_linked_files(report)

        return results

    def _fetch_latest(self, candidate_id: str) -> Filings | None:
        """Fetch the latest filing for a single candidate."""
        try:
            response = self.fec_client.get_v1_filings(
                candidate_id=[candidate_id],
                report_type=cast(list[str], self.report_types),
                sort=["-receipt_date"],
                per_page=1,
            )

            if response.status_code != 200:
                logger.error(f"FEC API error for {candidate_id}: {response.status_code}")
                return None

            results = response.json().get("results", [])
            if not results:
                logger.info(f"No filing found for {candidate_id}")
                return None

            return Filings(results[0])

        except Exception as e:
            logger.error(f"Failed to fetch filing for {candidate_id}: {e}")
            return None

    def _process_linked_files(self, filing: Filings) -> int:
        """Download and store CSV and PDF files for a filing if available."""
        file_number = filing.file_number
        if not file_number:
            return 0

        files_uploaded = 0
        base_path = f"files/{file_number}"

        if filing.csv_url:
            csv_path = f"{base_path}/{file_number}.csv"
            if self._download_and_store_file(filing.csv_url, csv_path, "text/csv"):
                files_uploaded += 1

        if filing.pdf_url:
            if self._download_and_store_file(
                filing.pdf_url, f"{base_path}/{file_number}.pdf", "application/pdf"
            ):
                files_uploaded += 1

        return files_uploaded

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
