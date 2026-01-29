from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ScheduleBByPurpose(BaseModel):
    """
    Strongly-typed model class for ScheduleBByPurpose
    
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
    def memo_count(self) -> int:
        """Get memo_count"""
        return self._data.get("memo_count")
    @memo_count.setter
    def memo_count(self, value: int):
        """Set memo_count"""
        self._data["memo_count"] = value

    @property
    def memo_total(self) -> float:
        """Get memo_total"""
        return self._data.get("memo_total")
    @memo_total.setter
    def memo_total(self, value: float):
        """Set memo_total"""
        self._data["memo_total"] = value

    @property
    def purpose(self) -> str:
        """Get purpose"""
        return self._data.get("purpose")
    @purpose.setter
    def purpose(self, value: str):
        """Set purpose"""
        self._data["purpose"] = value

    @property
    def total(self) -> float:
        """Get total"""
        return self._data.get("total")
    @total.setter
    def total(self, value: float):
        """Set total"""
        self._data["total"] = value
