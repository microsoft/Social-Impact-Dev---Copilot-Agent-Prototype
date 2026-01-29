from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .JFCCommittee import JFCCommittee

from ..base.base_model import BaseModel


class TotalsCommittee(BaseModel):
    """
    Strongly-typed model class for TotalsCommittee
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def affiliated_committee_name(self) -> str:
        """Get affiliated_committee_name"""
        return self._data.get("affiliated_committee_name")
    @affiliated_committee_name.setter
    def affiliated_committee_name(self, value: str):
        """Set affiliated_committee_name"""
        self._data["affiliated_committee_name"] = value

    @property
    def candidate_ids(self) -> List[str]:
        """Get candidate_ids"""
        return self._data.get("candidate_ids")
    @candidate_ids.setter
    def candidate_ids(self, value: List[str]):
        """Set candidate_ids"""
        self._data["candidate_ids"] = value

    @property
    def cash_on_hand_end_period(self) -> float:
        """Get cash_on_hand_end_period"""
        return self._data.get("cash_on_hand_end_period")
    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, value: float):
        """Set cash_on_hand_end_period"""
        self._data["cash_on_hand_end_period"] = value

    @property
    def city(self) -> str:
        """Get city"""
        return self._data.get("city")
    @city.setter
    def city(self, value: str):
        """Set city"""
        self._data["city"] = value

    @property
    def committee_id(self) -> str:
        """Get committee_id"""
        return self._data.get("committee_id")
    @committee_id.setter
    def committee_id(self, value: str):
        """Set committee_id"""
        self._data["committee_id"] = value

    @property
    def committee_type(self) -> str:
        """Get committee_type"""
        return self._data.get("committee_type")
    @committee_type.setter
    def committee_type(self, value: str):
        """Set committee_type"""
        self._data["committee_type"] = value

    @property
    def committee_type_full(self) -> str:
        """Get committee_type_full"""
        return self._data.get("committee_type_full")
    @committee_type_full.setter
    def committee_type_full(self, value: str):
        """Set committee_type_full"""
        self._data["committee_type_full"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def cycles(self) -> List[int]:
        """Get cycles"""
        return self._data.get("cycles")
    @cycles.setter
    def cycles(self, value: List[int]):
        """Set cycles"""
        self._data["cycles"] = value

    @property
    def cycles_has_activity(self) -> List[int]:
        """Get cycles_has_activity"""
        return self._data.get("cycles_has_activity")
    @cycles_has_activity.setter
    def cycles_has_activity(self, value: List[int]):
        """Set cycles_has_activity"""
        self._data["cycles_has_activity"] = value

    @property
    def cycles_has_financial(self) -> List[int]:
        """Get cycles_has_financial"""
        return self._data.get("cycles_has_financial")
    @cycles_has_financial.setter
    def cycles_has_financial(self, value: List[int]):
        """Set cycles_has_financial"""
        self._data["cycles_has_financial"] = value

    @property
    def debts_owed_by_committee(self) -> float:
        """Get debts_owed_by_committee"""
        return self._data.get("debts_owed_by_committee")
    @debts_owed_by_committee.setter
    def debts_owed_by_committee(self, value: float):
        """Set debts_owed_by_committee"""
        self._data["debts_owed_by_committee"] = value

    @property
    def designation(self) -> str:
        """Get designation"""
        return self._data.get("designation")
    @designation.setter
    def designation(self, value: str):
        """Set designation"""
        self._data["designation"] = value

    @property
    def designation_full(self) -> str:
        """Get designation_full"""
        return self._data.get("designation_full")
    @designation_full.setter
    def designation_full(self, value: str):
        """Set designation_full"""
        self._data["designation_full"] = value

    @property
    def disbursements(self) -> float:
        """Get disbursements"""
        return self._data.get("disbursements")
    @disbursements.setter
    def disbursements(self, value: float):
        """Set disbursements"""
        self._data["disbursements"] = value

    @property
    def filing_frequency(self) -> str:
        """Get filing_frequency"""
        return self._data.get("filing_frequency")
    @filing_frequency.setter
    def filing_frequency(self, value: str):
        """Set filing_frequency"""
        self._data["filing_frequency"] = value

    @property
    def first_f1_date(self) -> str:
        """Get first_f1_date"""
        return self._data.get("first_f1_date")
    @first_f1_date.setter
    def first_f1_date(self, value: str):
        """Set first_f1_date"""
        self._data["first_f1_date"] = value

    @property
    def first_file_date(self) -> str:
        """Get first_file_date"""
        return self._data.get("first_file_date")
    @first_file_date.setter
    def first_file_date(self, value: str):
        """Set first_file_date"""
        self._data["first_file_date"] = value

    @property
    def independent_expenditures(self) -> float:
        """Get independent_expenditures"""
        return self._data.get("independent_expenditures")
    @independent_expenditures.setter
    def independent_expenditures(self, value: float):
        """Set independent_expenditures"""
        self._data["independent_expenditures"] = value

    @property
    def is_active(self) -> bool:
        """Get is_active"""
        return self._data.get("is_active")
    @is_active.setter
    def is_active(self, value: bool):
        """Set is_active"""
        self._data["is_active"] = value

    @property
    def jfc_committee(self) -> List['JFCCommittee']:
        """Get jfc_committee"""
        return self._data.get("jfc_committee")
    @jfc_committee.setter
    def jfc_committee(self, value: List['JFCCommittee']):
        """Set jfc_committee"""
        self._data["jfc_committee"] = value

    @property
    def last_cycle_has_activity(self) -> int:
        """Get last_cycle_has_activity"""
        return self._data.get("last_cycle_has_activity")
    @last_cycle_has_activity.setter
    def last_cycle_has_activity(self, value: int):
        """Set last_cycle_has_activity"""
        self._data["last_cycle_has_activity"] = value

    @property
    def last_cycle_has_financial(self) -> int:
        """Get last_cycle_has_financial"""
        return self._data.get("last_cycle_has_financial")
    @last_cycle_has_financial.setter
    def last_cycle_has_financial(self, value: int):
        """Set last_cycle_has_financial"""
        self._data["last_cycle_has_financial"] = value

    @property
    def last_f1_date(self) -> str:
        """Get last_f1_date"""
        return self._data.get("last_f1_date")
    @last_f1_date.setter
    def last_f1_date(self, value: str):
        """Set last_f1_date"""
        self._data["last_f1_date"] = value

    @property
    def last_file_date(self) -> str:
        """Get last_file_date"""
        return self._data.get("last_file_date")
    @last_file_date.setter
    def last_file_date(self, value: str):
        """Set last_file_date"""
        self._data["last_file_date"] = value

    @property
    def name(self) -> str:
        """Get name"""
        return self._data.get("name")
    @name.setter
    def name(self, value: str):
        """Set name"""
        self._data["name"] = value

    @property
    def organization_type(self) -> str:
        """Get organization_type"""
        return self._data.get("organization_type")
    @organization_type.setter
    def organization_type(self, value: str):
        """Set organization_type"""
        self._data["organization_type"] = value

    @property
    def organization_type_full(self) -> str:
        """Get organization_type_full"""
        return self._data.get("organization_type_full")
    @organization_type_full.setter
    def organization_type_full(self, value: str):
        """Set organization_type_full"""
        self._data["organization_type_full"] = value

    @property
    def party(self) -> str:
        """Get party"""
        return self._data.get("party")
    @party.setter
    def party(self, value: str):
        """Set party"""
        self._data["party"] = value

    @property
    def party_full(self) -> str:
        """Get party_full"""
        return self._data.get("party_full")
    @party_full.setter
    def party_full(self, value: str):
        """Set party_full"""
        self._data["party_full"] = value

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
    def street_1(self) -> str:
        """Get street_1"""
        return self._data.get("street_1")
    @street_1.setter
    def street_1(self, value: str):
        """Set street_1"""
        self._data["street_1"] = value

    @property
    def street_2(self) -> str:
        """Get street_2"""
        return self._data.get("street_2")
    @street_2.setter
    def street_2(self, value: str):
        """Set street_2"""
        self._data["street_2"] = value

    @property
    def treasurer_name(self) -> str:
        """Get treasurer_name"""
        return self._data.get("treasurer_name")
    @treasurer_name.setter
    def treasurer_name(self, value: str):
        """Set treasurer_name"""
        self._data["treasurer_name"] = value

    @property
    def zip(self) -> str:
        """Get zip"""
        return self._data.get("zip")
    @zip.setter
    def zip(self, value: str):
        """Set zip"""
        self._data["zip"] = value
