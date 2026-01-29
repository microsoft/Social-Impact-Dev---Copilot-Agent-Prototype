from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class EntityReceiptDisbursementTotals(BaseModel):
    """
    Strongly-typed model class for EntityReceiptDisbursementTotals
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def cumulative_candidate_disbursements(self) -> float:
        """Get cumulative_candidate_disbursements"""
        return self._data.get("cumulative_candidate_disbursements")
    @cumulative_candidate_disbursements.setter
    def cumulative_candidate_disbursements(self, value: float):
        """Set cumulative_candidate_disbursements"""
        self._data["cumulative_candidate_disbursements"] = value

    @property
    def cumulative_candidate_receipts(self) -> float:
        """Get cumulative_candidate_receipts"""
        return self._data.get("cumulative_candidate_receipts")
    @cumulative_candidate_receipts.setter
    def cumulative_candidate_receipts(self, value: float):
        """Set cumulative_candidate_receipts"""
        self._data["cumulative_candidate_receipts"] = value

    @property
    def cumulative_pac_disbursements(self) -> float:
        """Get cumulative_pac_disbursements"""
        return self._data.get("cumulative_pac_disbursements")
    @cumulative_pac_disbursements.setter
    def cumulative_pac_disbursements(self, value: float):
        """Set cumulative_pac_disbursements"""
        self._data["cumulative_pac_disbursements"] = value

    @property
    def cumulative_pac_receipts(self) -> float:
        """Get cumulative_pac_receipts"""
        return self._data.get("cumulative_pac_receipts")
    @cumulative_pac_receipts.setter
    def cumulative_pac_receipts(self, value: float):
        """Set cumulative_pac_receipts"""
        self._data["cumulative_pac_receipts"] = value

    @property
    def cumulative_party_disbursements(self) -> float:
        """Get cumulative_party_disbursements"""
        return self._data.get("cumulative_party_disbursements")
    @cumulative_party_disbursements.setter
    def cumulative_party_disbursements(self, value: float):
        """Set cumulative_party_disbursements"""
        self._data["cumulative_party_disbursements"] = value

    @property
    def cumulative_party_receipts(self) -> float:
        """Get cumulative_party_receipts"""
        return self._data.get("cumulative_party_receipts")
    @cumulative_party_receipts.setter
    def cumulative_party_receipts(self, value: float):
        """Set cumulative_party_receipts"""
        self._data["cumulative_party_receipts"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def end_date(self) -> str:
        """Get end_date"""
        return self._data.get("end_date")
    @end_date.setter
    def end_date(self, value: str):
        """Set end_date"""
        self._data["end_date"] = value
