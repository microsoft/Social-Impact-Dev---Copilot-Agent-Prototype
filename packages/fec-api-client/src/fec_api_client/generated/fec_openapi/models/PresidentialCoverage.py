from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class PresidentialCoverage(BaseModel):
    """
    Strongly-typed model class for PresidentialCoverage
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

    @property
    def coverage_end_date(self) -> str:
        """Get coverage_end_date"""
        return self._data.get("coverage_end_date")
    @coverage_end_date.setter
    def coverage_end_date(self, value: str):
        """Set coverage_end_date"""
        self._data["coverage_end_date"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value
