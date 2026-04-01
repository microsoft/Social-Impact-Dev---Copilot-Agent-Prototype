"""Base types for FEC form CSV processing."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, Protocol, runtime_checkable

from .constants import HeaderDef

# Standard section names across form types
SectionName = Literal["Summary", "Contributions", "Disbursements", "Header"]


@dataclass
class Section:
    """A section of FEC data with headers and rows."""

    name: SectionName
    headers: list[str]
    columns: list[HeaderDef]
    rows: list[list[str]]


@runtime_checkable
class FormCSV(Protocol):
    """Protocol for parsed FEC form CSVs.

    All form-specific CSV classes (F3CSV, F3XCSV, etc.) implement this protocol
    to enable generic processing in format utilities.
    """

    @property
    def form_type(self) -> str:
        """The base form type code (e.g., 'F3', 'F3X')."""
        ...

    @property
    def version(self) -> str:
        """FEC e-filing format version."""
        ...

    @property
    def header(self) -> list[str]:
        """HDR record containing file metadata."""
        ...

    @property
    def all_rows(self) -> list[list[str]]:
        """All rows in original order for raw export."""
        ...

    def get_sections(self) -> list[Section]:
        """Get all sections with their headers and column definitions."""
        ...

    def get_header_section(self) -> Section | None:
        """Get the HDR section if present."""
        ...

    def get_section_rows(self, name: SectionName) -> list[list[str]]:
        """Get rows for a named section."""
        ...
