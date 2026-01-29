from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CandidateFlags(BaseModel):
    """
    Strongly-typed model class for CandidateFlags
    
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
    def federal_funds_flag(self) -> bool:
        """Get federal_funds_flag"""
        return self._data.get("federal_funds_flag")
    @federal_funds_flag.setter
    def federal_funds_flag(self, value: bool):
        """Set federal_funds_flag"""
        self._data["federal_funds_flag"] = value

    @property
    def has_raised_funds(self) -> bool:
        """Get has_raised_funds"""
        return self._data.get("has_raised_funds")
    @has_raised_funds.setter
    def has_raised_funds(self, value: bool):
        """Set has_raised_funds"""
        self._data["has_raised_funds"] = value
