from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CCTotalsByCandidate(BaseModel):
    """
    Strongly-typed model class for CCTotalsByCandidate
    
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
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def support_oppose_indicator(self) -> str:
        """Get support_oppose_indicator"""
        return self._data.get("support_oppose_indicator")
    @support_oppose_indicator.setter
    def support_oppose_indicator(self, value: str):
        """Set support_oppose_indicator"""
        self._data["support_oppose_indicator"] = value

    @property
    def total(self) -> float:
        """Get total"""
        return self._data.get("total")
    @total.setter
    def total(self, value: float):
        """Set total"""
        self._data["total"] = value
