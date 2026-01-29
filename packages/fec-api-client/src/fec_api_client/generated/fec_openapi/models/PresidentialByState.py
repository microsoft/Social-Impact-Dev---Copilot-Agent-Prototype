from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class PresidentialByState(BaseModel):
    """
    Strongly-typed model class for PresidentialByState
    
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
    def contribution_state(self) -> str:
        """Get contribution_state"""
        return self._data.get("contribution_state")
    @contribution_state.setter
    def contribution_state(self, value: str):
        """Set contribution_state"""
        self._data["contribution_state"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value
