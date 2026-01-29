from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class InauguralDonations(BaseModel):
    """
    Strongly-typed model class for InauguralDonations
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def committee_id(self) -> str:
        """Get committee_id"""
        return self._data.get("committee_id")
    @committee_id.setter
    def committee_id(self, value: str):
        """Set committee_id"""
        self._data["committee_id"] = value

    @property
    def contributor_name(self) -> str:
        """Get contributor_name"""
        return self._data.get("contributor_name")
    @contributor_name.setter
    def contributor_name(self, value: str):
        """Set contributor_name"""
        self._data["contributor_name"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def total_donation(self) -> float:
        """Get total_donation"""
        return self._data.get("total_donation")
    @total_donation.setter
    def total_donation(self, value: float):
        """Set total_donation"""
        self._data["total_donation"] = value
