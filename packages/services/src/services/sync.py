from __future__ import annotations

import json
import logging

import httpx
from fec_api_client import FecApiClient

from .constants import QUARTERLY_REPORT_TYPES
from .storage import BlobStorageService

logger = logging.getLogger(__name__)


class SyncService:
    """Service for syncing FEC committee reports to blob storage."""

    def __init__(
        self,
        fec_client: FecApiClient,
        blob_service: BlobStorageService,
        http_client: httpx.Client | None = None,
        committee_ids: list[str] | None = None,
        report_types: list[str] | None = None,
        api_key: str | None = None,
    ) -> None:
        self.fec_client = fec_client
        self.blob_service = blob_service
        self.http_client = http_client or httpx.Client(timeout=60.0)
        self.committee_ids = committee_ids
        self.report_types = report_types
        self.api_key = api_key

    def sync_reports(self) -> dict[str, dict | None]:
        """Fetch and store the latest quarterly report for each configured committee.

        Returns:
            Dict mapping committee_id to their latest report data (or None if not found).
        """
        if not self.committee_ids:
            logger.warning("No committee IDs configured")
            return {}

        self.blob_service.ensure_container_exists()
        results: dict[str, dict | None] = {}

        for committee_id in self.committee_ids:
            report = self._fetch_latest_report(committee_id)
            results[committee_id] = report

            if report:
                blob_path = f"reports/{committee_id}.json"
                self.blob_service.upload_bytes(
                    blob_path,
                    json.dumps(report).encode(),
                    content_type="application/json",
                )
                logger.info(f"Stored report for {committee_id}: {blob_path}")

                self._process_filing(report)

        return results

    def _fetch_latest_report(self, committee_id: str) -> dict | None:
        """Fetch the latest quarterly report for a committee."""
        report_types = self.report_types or QUARTERLY_REPORT_TYPES

        try:
            response = self.fec_client.get_v1_filings(
                committee_id=[committee_id],
                report_type=report_types,
                sort=["-receipt_date"],
                per_page=1,
                api_key=self.api_key,
            )

            if response.status_code != 200:
                logger.error(f"FEC API error for {committee_id}: {response.status_code}")
                return None

            results = response.json().get("results", [])
            if not results:
                logger.info(f"No quarterly report found for {committee_id}")
                return None

            return results[0]

        except Exception as e:
            logger.error(f"Failed to fetch report for {committee_id}: {e}")
            return None

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
