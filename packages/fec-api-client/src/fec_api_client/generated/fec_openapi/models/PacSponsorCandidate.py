from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class PacSponsorCandidate(BaseModel):
    """
    Strongly-typed model class for PacSponsorCandidate
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def sponsor_candidate_id(self) -> str:
        """Get sponsor_candidate_id"""
        return self._data.get("sponsor_candidate_id")
    @sponsor_candidate_id.setter
    def sponsor_candidate_id(self, value: str):
        """Set sponsor_candidate_id"""
        self._data["sponsor_candidate_id"] = value

    @property
    def sponsor_candidate_name(self) -> str:
        """Get sponsor_candidate_name"""
        return self._data.get("sponsor_candidate_name")
    @sponsor_candidate_name.setter
    def sponsor_candidate_name(self, value: str):
        """Set sponsor_candidate_name"""
        self._data["sponsor_candidate_name"] = value
