from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class NationalPartyTotals(BaseModel):
    """
    Strongly-typed model class for NationalPartyTotals
    
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
    def committee_name(self) -> str:
        """Get committee_name"""
        return self._data.get("committee_name")
    @committee_name.setter
    def committee_name(self, value: str):
        """Set committee_name"""
        self._data["committee_name"] = value

    @property
    def total_disbursements(self) -> float:
        """Get total_disbursements"""
        return self._data.get("total_disbursements")
    @total_disbursements.setter
    def total_disbursements(self, value: float):
        """Set total_disbursements"""
        self._data["total_disbursements"] = value

    @property
    def total_receipts(self) -> float:
        """Get total_receipts"""
        return self._data.get("total_receipts")
    @total_receipts.setter
    def total_receipts(self, value: float):
        """Set total_receipts"""
        self._data["total_receipts"] = value

    @property
    def two_year_transaction_period(self) -> int:
        """Get two_year_transaction_period"""
        return self._data.get("two_year_transaction_period")
    @two_year_transaction_period.setter
    def two_year_transaction_period(self, value: int):
        """Set two_year_transaction_period"""
        self._data["two_year_transaction_period"] = value
