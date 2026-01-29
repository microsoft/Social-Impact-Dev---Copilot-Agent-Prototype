from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CandidateTotal(BaseModel):
    """
    Strongly-typed model class for CandidateTotal
    
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
    def candidate_inactive(self) -> bool:
        """Get candidate_inactive"""
        return self._data.get("candidate_inactive")
    @candidate_inactive.setter
    def candidate_inactive(self, value: bool):
        """Set candidate_inactive"""
        self._data["candidate_inactive"] = value

    @property
    def cash_on_hand_end_period(self) -> float:
        """Get cash_on_hand_end_period"""
        return self._data.get("cash_on_hand_end_period")
    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, value: float):
        """Set cash_on_hand_end_period"""
        self._data["cash_on_hand_end_period"] = value

    @property
    def coverage_end_date(self) -> str:
        """Get coverage_end_date"""
        return self._data.get("coverage_end_date")
    @coverage_end_date.setter
    def coverage_end_date(self, value: str):
        """Set coverage_end_date"""
        self._data["coverage_end_date"] = value

    @property
    def coverage_start_date(self) -> str:
        """Get coverage_start_date"""
        return self._data.get("coverage_start_date")
    @coverage_start_date.setter
    def coverage_start_date(self, value: str):
        """Set coverage_start_date"""
        self._data["coverage_start_date"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def debts_owed_by_committee(self) -> float:
        """Get debts_owed_by_committee"""
        return self._data.get("debts_owed_by_committee")
    @debts_owed_by_committee.setter
    def debts_owed_by_committee(self, value: float):
        """Set debts_owed_by_committee"""
        self._data["debts_owed_by_committee"] = value

    @property
    def disbursements(self) -> float:
        """Get disbursements"""
        return self._data.get("disbursements")
    @disbursements.setter
    def disbursements(self, value: float):
        """Set disbursements"""
        self._data["disbursements"] = value

    @property
    def district(self) -> str:
        """Get district"""
        return self._data.get("district")
    @district.setter
    def district(self, value: str):
        """Set district"""
        self._data["district"] = value

    @property
    def district_number(self) -> int:
        """Get district_number"""
        return self._data.get("district_number")
    @district_number.setter
    def district_number(self, value: int):
        """Set district_number"""
        self._data["district_number"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def federal_funds_flag(self) -> bool:
        """Get federal_funds_flag"""
        return self._data.get("federal_funds_flag")
    @federal_funds_flag.setter
    def federal_funds_flag(self, value: bool):
        """Set federal_funds_flag"""
        self._data["federal_funds_flag"] = value

    @property
    def has_raised_funds(self) -> bool:
        """Get has_raised_funds"""
        return self._data.get("has_raised_funds")
    @has_raised_funds.setter
    def has_raised_funds(self, value: bool):
        """Set has_raised_funds"""
        self._data["has_raised_funds"] = value

    @property
    def individual_itemized_contributions(self) -> float:
        """Get individual_itemized_contributions"""
        return self._data.get("individual_itemized_contributions")
    @individual_itemized_contributions.setter
    def individual_itemized_contributions(self, value: float):
        """Set individual_itemized_contributions"""
        self._data["individual_itemized_contributions"] = value

    @property
    def is_election(self) -> bool:
        """Get is_election"""
        return self._data.get("is_election")
    @is_election.setter
    def is_election(self, value: bool):
        """Set is_election"""
        self._data["is_election"] = value

    @property
    def office(self) -> str:
        """Get office"""
        return self._data.get("office")
    @office.setter
    def office(self, value: str):
        """Set office"""
        self._data["office"] = value

    @property
    def other_political_committee_contributions(self) -> float:
        """Get other_political_committee_contributions"""
        return self._data.get("other_political_committee_contributions")
    @other_political_committee_contributions.setter
    def other_political_committee_contributions(self, value: float):
        """Set other_political_committee_contributions"""
        self._data["other_political_committee_contributions"] = value

    @property
    def party(self) -> str:
        """Get party"""
        return self._data.get("party")
    @party.setter
    def party(self, value: str):
        """Set party"""
        self._data["party"] = value

    @property
    def receipts(self) -> float:
        """Get receipts"""
        return self._data.get("receipts")
    @receipts.setter
    def receipts(self, value: float):
        """Set receipts"""
        self._data["receipts"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

    @property
    def state_full(self) -> str:
        """Get state_full"""
        return self._data.get("state_full")
    @state_full.setter
    def state_full(self, value: str):
        """Set state_full"""
        self._data["state_full"] = value

    @property
    def transfers_from_other_authorized_committee(self) -> float:
        """Get transfers_from_other_authorized_committee"""
        return self._data.get("transfers_from_other_authorized_committee")
    @transfers_from_other_authorized_committee.setter
    def transfers_from_other_authorized_committee(self, value: float):
        """Set transfers_from_other_authorized_committee"""
        self._data["transfers_from_other_authorized_committee"] = value
