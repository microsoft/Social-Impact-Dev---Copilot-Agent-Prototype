from __future__ import annotations

import gc
import json
import logging
from collections.abc import Callable
from urllib.parse import urlparse

import httpx
from fec_api_client import (
    FEC_DOWNLOAD_DOMAINS,
    CandidateDetail,
    CommitteeDetail,
    FecApiClient,
    Filings,
)

from ..instrumentation import Operation, track_operation
from ..storage import BlobStorageService
from .constants import QUARTERLY_REPORT_TYPES
from .format import ParsedQuarterlyCSV, add_headers_to_csv, create_xlsx, parse_fec_csv

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

    def sync_reports(self) -> dict[str, Filings | None]:
        """Fetch and store the latest quarterly report for each configured committee.

        Returns:
            Dict mapping committee_id to their latest Filings (or None if not found).
        """
        if not self.committee_ids:
            logger.warning("No committee IDs configured")
            return {}

        with track_operation(Operation.SYNC_REPORTS) as metrics:
            self.blob_service.ensure_container_exists()
            results: dict[str, Filings | None] = {}
            records_synced = 0

            for committee_id in self.committee_ids:
                filing = self._fetch_latest_report(committee_id)

                if not filing:
                    results[committee_id] = None
                    continue

                base_path = self._get_report_path(committee_id, filing)
                blob_path = f"{base_path}/report.json"

                if self.blob_service.exists(blob_path):
                    logger.info(f"Report already synced, skipping: {blob_path}")
                    results[committee_id] = None
                    continue

                committee = self.get_committee(committee_id)
                if committee and committee.state and not filing.state:
                    filing.state = committee.state

                self.get_candidates(committee_id)

                self._process_filing(base_path, filing)

                self._save_report(blob_path, filing)
                results[committee_id] = filing
                records_synced += 1

                # Free memory before processing next committee (helps on constrained environments)
                gc.collect()

            metrics.record_count = records_synced
            metrics.extra["committees_checked"] = len(self.committee_ids)

        return results

    def _save_report(self, blob_path: str, filing: Filings) -> None:
        """Save report JSON to blob storage with instrumentation."""
        with track_operation(Operation.SAVE_REPORT, committee_id=filing.committee_id):
            self.blob_service.upload_bytes(
                blob_path,
                filing.to_json().encode(),
                content_type="application/json",
            )
            logger.info(f"Stored report: {blob_path}")

    def get_committee(self, committee_id: str) -> CommitteeDetail | None:
        """Get committee details, using cached data if available."""
        blob_path = f"{committee_id}/committee.json"

        cached = self.blob_service.download_bytes(blob_path)
        if cached:
            return CommitteeDetail.from_json(cached.decode("utf-8"))

        try:
            response = self.fec_client.get_v1_committee_committee_id(
                committee_id=committee_id,
                api_key=self.api_key,
            )

            if response.status_code != 200:
                logger.warning(f"Failed to fetch committee {committee_id}: {response.status_code}")
                return None

            results = response.json().get("results", [])
            if not results:
                return None

            committee = CommitteeDetail.from_dict(results[0])

            self.blob_service.upload_bytes(
                blob_path,
                committee.to_json().encode(),
                content_type="application/json",
            )
            logger.info(f"Cached committee details: {blob_path}")

            return committee

        except Exception as e:
            logger.warning(f"Failed to fetch committee {committee_id}: {e}")
            return None

    def get_candidates(self, committee_id: str) -> list[CandidateDetail]:
        """Get candidates for a committee, using cached data if available."""
        blob_path = f"{committee_id}/candidates.json"

        cached = self.blob_service.download_bytes(blob_path)
        if cached:
            data = json.loads(cached.decode("utf-8"))
            return [CandidateDetail.from_dict(c) for c in data]

        committee = self.get_committee(committee_id)
        if not committee or not committee.candidate_ids:
            return []

        candidates: list[CandidateDetail] = []
        for candidate_id in committee.candidate_ids:
            candidate = self._fetch_candidate(candidate_id)
            if candidate:
                candidates.append(candidate)

        if candidates:
            data = [c.to_dict() for c in candidates]
            self.blob_service.upload_bytes(
                blob_path,
                json.dumps(data).encode(),
                content_type="application/json",
            )
            logger.info(f"Cached {len(candidates)} candidates: {blob_path}")

        return candidates

    def _fetch_candidate(self, candidate_id: str) -> CandidateDetail | None:
        """Fetch candidate details from FEC API."""
        try:
            response = self.fec_client.get_v1_candidate_candidate_id(
                candidate_id=candidate_id,
                api_key=self.api_key,
            )

            if response.status_code != 200:
                logger.warning(f"Failed to fetch candidate {candidate_id}: {response.status_code}")
                return None

            results = response.json().get("results", [])
            if not results:
                return None

            return CandidateDetail.from_dict(results[0])

        except Exception as e:
            logger.warning(f"Failed to fetch candidate {candidate_id}: {e}")
            return None

    def _fetch_latest_report(self, committee_id: str) -> Filings | None:
        """Fetch the latest quarterly report for a committee."""
        report_types = self.report_types or list(QUARTERLY_REPORT_TYPES)

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

            return Filings.from_dict(results[0])

        except Exception as e:
            logger.error(f"Failed to fetch report for {committee_id}: {e}")
            return None

    def _get_report_path(self, committee_id: str, filing: Filings) -> str:
        """Build the base path for a report: {committee_id}/{year}-{report_type}."""
        report_year = filing.report_year or "unknown"
        report_type = filing.report_type or "unknown"
        return f"{committee_id}/{report_year}-{report_type}"

    def _process_filing(self, base_path: str, filing: Filings) -> int:
        """Process a single filing, downloading CSV and creating processed versions."""
        files_uploaded = 0
        committee_id = filing.committee_id

        if filing.csv_url:
            # Download CSV with timing
            with track_operation(Operation.DOWNLOAD_CSV, committee_id=committee_id) as dl_metrics:
                csv_content = self._download_file(filing.csv_url)
                dl_metrics.extra["csv_url"] = filing.csv_url
                dl_metrics.extra["size_bytes"] = len(csv_content) if csv_content else 0
                dl_metrics.success = csv_content is not None

            if csv_content:
                filename = self._get_filename_from_url(filing.csv_url)
                base_name = filename.rsplit(".", 1)[0]
                raw_size_mb = len(csv_content) / (1024 * 1024)

                # Parse CSV once and release raw content immediately
                parsed = parse_fec_csv(csv_content)
                del csv_content
                gc.collect()

                # Log parsed data stats
                logger.info(
                    f"[MEMORY] Raw CSV: {raw_size_mb:.1f}MB, "
                    f"rows: {len(parsed.all_rows)}, "
                    f"contributions: {len(parsed.contributions)}, "
                    f"disbursements: {len(parsed.disbursements)}"
                )

                # Format and save CSV (reuse parsed data)
                csv_blob_path = f"{base_path}/{base_name}.csv"
                with track_operation(Operation.FORMAT_AND_SAVE_CSV, committee_id=committee_id):
                    if self._process_and_upload(
                        parsed, csv_blob_path, add_headers_to_csv, "text/csv"
                    ):
                        files_uploaded += 1

                # Create and save XLSX (reuse parsed data)
                xlsx_blob_path = f"{base_path}/{base_name}.xlsx"
                xlsx_mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                with track_operation(Operation.CREATE_AND_SAVE_XLSX, committee_id=committee_id):
                    if self._process_and_upload(
                        parsed, xlsx_blob_path, create_xlsx, xlsx_mime
                    ):
                        files_uploaded += 1

                # Release parsed data from memory
                del parsed
                gc.collect()

        return files_uploaded

    def _process_and_upload(
        self,
        content: bytes | ParsedQuarterlyCSV,
        blob_path: str,
        processor: Callable[[bytes | ParsedQuarterlyCSV], str | bytes],
        content_type: str,
    ) -> bool:
        """Process content and upload to blob storage."""
        try:
            processed = processor(content)
            data = processed.encode("utf-8") if isinstance(processed, str) else processed
            size_mb = len(data) / (1024 * 1024)
            self.blob_service.upload_bytes(blob_path, data, content_type=content_type)
            logger.info(f"Uploaded: {blob_path} ({size_mb:.1f}MB)")
            return True
        except Exception as e:
            logger.warning(f"Failed to process {blob_path}: {e}")
            return False

    def _download_file(self, url: str) -> bytes | None:
        """Download a file from URL and return its content.

        Only downloads from allowlisted FEC domains for SSRF protection.
        """
        # Validate URL domain (SSRF protection)
        try:
            parsed = urlparse(url)
            if parsed.hostname not in FEC_DOWNLOAD_DOMAINS:
                logger.warning(f"Blocked download from untrusted domain: {parsed.hostname}")
                return None
            if parsed.scheme not in ("https", "http"):
                logger.warning(f"Blocked download with invalid scheme: {parsed.scheme}")
                return None
        except Exception as e:
            logger.warning(f"Failed to parse URL {url}: {e}")
            return None

        try:
            response = self.http_client.get(url)
            response.raise_for_status()
            return response.content
        except httpx.HTTPError as e:
            logger.warning(f"Failed to download {url}: {e}")
            return None

    def _get_filename_from_url(self, url: str) -> str:
        """Extract the filename from a URL."""
        return url.rstrip("/").split("/")[-1]
