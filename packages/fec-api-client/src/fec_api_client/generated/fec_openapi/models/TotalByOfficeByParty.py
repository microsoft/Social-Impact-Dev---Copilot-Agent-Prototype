from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class TotalByOfficeByParty(BaseModel):
    """
    Strongly-typed model class for TotalByOfficeByParty
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def office(self) -> str:
        """Get office"""
        return self._data.get("office")
    @office.setter
    def office(self, value: str):
        """Set office"""
        self._data["office"] = value

    @property
    def party(self) -> str:
        """Get party"""
        return self._data.get("party")
    @party.setter
    def party(self, value: str):
        """Set party"""
        self._data["party"] = value

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
