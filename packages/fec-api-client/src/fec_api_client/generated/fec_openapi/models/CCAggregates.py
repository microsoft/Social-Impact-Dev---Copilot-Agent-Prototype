from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CCAggregates(BaseModel):
    """
    Strongly-typed model class for CCAggregates
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def candidate(self) -> str:
        """Get candidate"""
        return self._data.get("candidate")
    @candidate.setter
    def candidate(self, value: str):
        """Set candidate"""
        self._data["candidate"] = value

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

    @property
    def candidate_name(self) -> str:
        """Get candidate_name"""
        return self._data.get("candidate_name")
    @candidate_name.setter
    def candidate_name(self, value: str):
        """Set candidate_name"""
        self._data["candidate_name"] = value

    @property
    def committee(self) -> str:
        """Get committee"""
        return self._data.get("committee")
    @committee.setter
    def committee(self, value: str):
        """Set committee"""
        self._data["committee"] = value

    @property
    def committee_id(self) -> str:
        """Get committee_id"""
        return self._data.get("committee_id")
    @committee_id.setter
    def committee_id(self, value: str):
        """Set committee_id"""
        self._data["committee_id"] = value

    @property
    def committee_name(self) -> str:
        """Get committee_name"""
        return self._data.get("committee_name")
    @committee_name.setter
    def committee_name(self, value: str):
        """Set committee_name"""
        self._data["committee_name"] = value

    @property
    def count(self) -> int:
        """Get count"""
        return self._data.get("count")
    @count.setter
    def count(self, value: int):
        """Set count"""
        self._data["count"] = value

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
