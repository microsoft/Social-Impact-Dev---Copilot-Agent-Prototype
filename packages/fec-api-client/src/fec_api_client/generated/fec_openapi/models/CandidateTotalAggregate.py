from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CandidateTotalAggregate(BaseModel):
    """
    Strongly-typed model class for CandidateTotalAggregate
    
    Generated from OpenAPI/Swagger specification
    """

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
    def total_cash_on_hand_end_period(self) -> float:
        """Get total_cash_on_hand_end_period"""
        return self._data.get("total_cash_on_hand_end_period")
    @total_cash_on_hand_end_period.setter
    def total_cash_on_hand_end_period(self, value: float):
        """Set total_cash_on_hand_end_period"""
        self._data["total_cash_on_hand_end_period"] = value

    @property
    def total_debts_owed_by_committee(self) -> float:
        """Get total_debts_owed_by_committee"""
        return self._data.get("total_debts_owed_by_committee")
    @total_debts_owed_by_committee.setter
    def total_debts_owed_by_committee(self, value: float):
        """Set total_debts_owed_by_committee"""
        self._data["total_debts_owed_by_committee"] = value

    @property
    def total_disbursements(self) -> float:
        """Get total_disbursements"""
        return self._data.get("total_disbursements")
    @total_disbursements.setter
    def total_disbursements(self, value: float):
        """Set total_disbursements"""
        self._data["total_disbursements"] = value

    @property
    def total_individual_itemized_contributions(self) -> float:
        """Get total_individual_itemized_contributions"""
        return self._data.get("total_individual_itemized_contributions")
    @total_individual_itemized_contributions.setter
    def total_individual_itemized_contributions(self, value: float):
        """Set total_individual_itemized_contributions"""
        self._data["total_individual_itemized_contributions"] = value

    @property
    def total_other_political_committee_contributions(self) -> float:
        """Get total_other_political_committee_contributions"""
        return self._data.get("total_other_political_committee_contributions")
    @total_other_political_committee_contributions.setter
    def total_other_political_committee_contributions(self, value: float):
        """Set total_other_political_committee_contributions"""
        self._data["total_other_political_committee_contributions"] = value

    @property
    def total_receipts(self) -> float:
        """Get total_receipts"""
        return self._data.get("total_receipts")
    @total_receipts.setter
    def total_receipts(self, value: float):
        """Set total_receipts"""
        self._data["total_receipts"] = value

    @property
    def total_transfers_from_other_authorized_committee(self) -> float:
        """Get total_transfers_from_other_authorized_committee"""
        return self._data.get("total_transfers_from_other_authorized_committee")
    @total_transfers_from_other_authorized_committee.setter
    def total_transfers_from_other_authorized_committee(self, value: float):
        """Set total_transfers_from_other_authorized_committee"""
        self._data["total_transfers_from_other_authorized_committee"] = value
