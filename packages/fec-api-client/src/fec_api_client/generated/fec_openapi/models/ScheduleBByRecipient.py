from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ScheduleBByRecipient(BaseModel):
    """
    Strongly-typed model class for ScheduleBByRecipient
    
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
    def committee_total_disbursements(self) -> float:
        """Get committee_total_disbursements"""
        return self._data.get("committee_total_disbursements")
    @committee_total_disbursements.setter
    def committee_total_disbursements(self, value: float):
        """Set committee_total_disbursements"""
        self._data["committee_total_disbursements"] = value

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
    def recipient_disbursement_percent(self) -> float:
        """Get recipient_disbursement_percent"""
        return self._data.get("recipient_disbursement_percent")
    @recipient_disbursement_percent.setter
    def recipient_disbursement_percent(self, value: float):
        """Set recipient_disbursement_percent"""
        self._data["recipient_disbursement_percent"] = value

    @property
    def recipient_name(self) -> str:
        """Get recipient_name"""
        return self._data.get("recipient_name")
    @recipient_name.setter
    def recipient_name(self, value: str):
        """Set recipient_name"""
        self._data["recipient_name"] = value

    @property
    def total(self) -> float:
        """Get total"""
        return self._data.get("total")
    @total.setter
    def total(self, value: float):
        """Set total"""
        self._data["total"] = value
