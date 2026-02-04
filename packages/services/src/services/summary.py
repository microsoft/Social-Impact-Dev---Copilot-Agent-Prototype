from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from typing import Protocol

from openai import AzureOpenAI

logger = logging.getLogger(__name__)


@dataclass
class SummaryResult:
    """Result of generating a summary."""

    success: bool
    summary: str | None = None
    error: str | None = None


class SummaryService(Protocol):
    """Protocol for AI summary generation services."""

    def generate_summary(self, filings: list[dict]) -> SummaryResult: ...


class AzureOpenAISummaryService:
    """Azure OpenAI-based summary generation service."""

    DEFAULT_SYSTEM_PROMPT = (
        "You are a helpful assistant that summarizes FEC "
        "(Federal Election Commission) filings.\n"
        "When given a list of filings, provide a clear and concise summary that highlights:\n"
        "- The total number of filings\n"
        "- Key filing types (e.g., quarterly reports, 24/48 hour reports)\n"
        "- Notable committees or candidates\n"
        "- Any significant financial information if available\n\n"
        "Keep your summary professional and factual."
    )

    def __init__(
        self,
        endpoint: str | None = None,
        api_key: str | None = None,
        deployment: str | None = None,
        api_version: str = "2024-02-15-preview",
        system_prompt: str | None = None,
    ) -> None:
        self.endpoint = endpoint or os.getenv("AZURE_OPENAI_ENDPOINT")
        self.api_key = api_key or os.getenv("AZURE_OPENAI_API_KEY")
        self.deployment = deployment or os.getenv("AZURE_OPENAI_DEPLOYMENT")
        self.system_prompt = system_prompt or self.DEFAULT_SYSTEM_PROMPT

        if not self.endpoint:
            raise ValueError("endpoint or AZURE_OPENAI_ENDPOINT must be provided")
        if not self.api_key:
            raise ValueError("api_key or AZURE_OPENAI_API_KEY must be provided")
        if not self.deployment:
            raise ValueError("deployment or AZURE_OPENAI_DEPLOYMENT must be provided")

        self._client = AzureOpenAI(
            azure_endpoint=self.endpoint,
            api_key=self.api_key,
            api_version=api_version,
        )

    def generate_summary(self, filings: list[dict]) -> SummaryResult:
        """Generate a summary of the given filings.

        Args:
            filings: List of filing dictionaries containing filing metadata.

        Returns:
            SummaryResult with the generated summary or error.
        """
        if not filings:
            return SummaryResult(
                success=True,
                summary="No new filings to summarize.",
            )

        filings_text = self._format_filings(filings)

        try:
            response = self._client.chat.completions.create(
                model=self.deployment,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {
                        "role": "user",
                        "content": f"Please summarize the following FEC filings:\n\n{filings_text}",
                    },
                ],
                max_tokens=1000,
                temperature=0.3,
            )

            summary = response.choices[0].message.content
            if not summary:
                return SummaryResult(success=False, error="Empty response from model")

            logger.info(f"Generated summary for {len(filings)} filings")
            return SummaryResult(success=True, summary=summary)

        except Exception as e:
            logger.error(f"Failed to generate summary: {e}")
            return SummaryResult(success=False, error=str(e))

    def _format_filings(self, filings: list[dict]) -> str:
        """Format filings list into a readable text format."""
        lines = []
        for i, filing in enumerate(filings, 1):
            parts = [f"{i}. "]
            if "committee_name" in filing:
                parts.append(f"Committee: {filing['committee_name']}")
            if "form_type" in filing:
                parts.append(f"Form: {filing['form_type']}")
            if "receipt_date" in filing:
                parts.append(f"Date: {filing['receipt_date']}")
            if "document_description" in filing:
                parts.append(f"Description: {filing['document_description']}")
            lines.append(" | ".join(parts))
        return "\n".join(lines)
