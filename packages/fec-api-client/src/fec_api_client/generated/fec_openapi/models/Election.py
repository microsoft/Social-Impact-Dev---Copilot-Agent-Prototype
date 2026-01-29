from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Election(BaseModel):
    """
    Strongly-typed model class for Election
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def candidate_election_year(self) -> int:
        """Get candidate_election_year"""
        return self._data.get("candidate_election_year")
    @candidate_election_year.setter
    def candidate_election_year(self, value: int):
        """Set candidate_election_year"""
        self._data["candidate_election_year"] = value

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
    def candidate_pcc_id(self) -> str:
        """Get candidate_pcc_id"""
        return self._data.get("candidate_pcc_id")
    @candidate_pcc_id.setter
    def candidate_pcc_id(self, value: str):
        """Set candidate_pcc_id"""
        self._data["candidate_pcc_id"] = value

    @property
    def candidate_pcc_name(self) -> str:
        """Get candidate_pcc_name"""
        return self._data.get("candidate_pcc_name")
    @candidate_pcc_name.setter
    def candidate_pcc_name(self, value: str):
        """Set candidate_pcc_name"""
        self._data["candidate_pcc_name"] = value

    @property
    def cash_on_hand_end_period(self) -> float:
        """Get cash_on_hand_end_period"""
        return self._data.get("cash_on_hand_end_period")
    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, value: float):
        """Set cash_on_hand_end_period"""
        self._data["cash_on_hand_end_period"] = value

    @property
    def committee_ids(self) -> List[str]:
        """Get committee_ids"""
        return self._data.get("committee_ids")
    @committee_ids.setter
    def committee_ids(self, value: List[str]):
        """Set committee_ids"""
        self._data["committee_ids"] = value

    @property
    def coverage_end_date(self) -> str:
        """Get coverage_end_date"""
        return self._data.get("coverage_end_date")
    @coverage_end_date.setter
    def coverage_end_date(self, value: str):
        """Set coverage_end_date"""
        self._data["coverage_end_date"] = value

    @property
    def incumbent_challenge_full(self) -> str:
        """Get incumbent_challenge_full"""
        return self._data.get("incumbent_challenge_full")
    @incumbent_challenge_full.setter
    def incumbent_challenge_full(self, value: str):
        """Set incumbent_challenge_full"""
        self._data["incumbent_challenge_full"] = value

    @property
    def party_full(self) -> str:
        """Get party_full"""
        return self._data.get("party_full")
    @party_full.setter
    def party_full(self, value: str):
        """Set party_full"""
        self._data["party_full"] = value

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
