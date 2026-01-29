from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class PresidentialByCandidate(BaseModel):
    """
    Strongly-typed model class for PresidentialByCandidate
    
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
    def candidate_last_name(self) -> str:
        """Get candidate_last_name"""
        return self._data.get("candidate_last_name")
    @candidate_last_name.setter
    def candidate_last_name(self, value: str):
        """Set candidate_last_name"""
        self._data["candidate_last_name"] = value

    @property
    def candidate_party_affiliation(self) -> str:
        """Get candidate_party_affiliation"""
        return self._data.get("candidate_party_affiliation")
    @candidate_party_affiliation.setter
    def candidate_party_affiliation(self, value: str):
        """Set candidate_party_affiliation"""
        self._data["candidate_party_affiliation"] = value

    @property
    def contributor_state(self) -> str:
        """Get contributor_state"""
        return self._data.get("contributor_state")
    @contributor_state.setter
    def contributor_state(self, value: str):
        """Set contributor_state"""
        self._data["contributor_state"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def net_receipts(self) -> float:
        """Get net_receipts"""
        return self._data.get("net_receipts")
    @net_receipts.setter
    def net_receipts(self, value: float):
        """Set net_receipts"""
        self._data["net_receipts"] = value

    @property
    def rounded_net_receipts(self) -> float:
        """Get rounded_net_receipts"""
        return self._data.get("rounded_net_receipts")
    @rounded_net_receipts.setter
    def rounded_net_receipts(self, value: float):
        """Set rounded_net_receipts"""
        self._data["rounded_net_receipts"] = value
