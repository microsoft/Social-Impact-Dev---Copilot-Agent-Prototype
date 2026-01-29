from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class PresidentialBySize(BaseModel):
    """
    Strongly-typed model class for PresidentialBySize
    
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
    def contribution_receipt_amount(self) -> float:
        """Get contribution_receipt_amount"""
        return self._data.get("contribution_receipt_amount")
    @contribution_receipt_amount.setter
    def contribution_receipt_amount(self, value: float):
        """Set contribution_receipt_amount"""
        self._data["contribution_receipt_amount"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def size(self) -> int:
        """Get size"""
        return self._data.get("size")
    @size.setter
    def size(self, value: int):
        """Set size"""
        self._data["size"] = value

    @property
    def size_range_id(self) -> int:
        """Get size_range_id"""
        return self._data.get("size_range_id")
    @size_range_id.setter
    def size_range_id(self, value: int):
        """Set size_range_id"""
        self._data["size_range_id"] = value
