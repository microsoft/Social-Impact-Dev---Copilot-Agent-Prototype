from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .JFCCommittee import JFCCommittee

from ..base.base_model import BaseModel


class CommitteeDetail(BaseModel):
    """
    Strongly-typed model class for CommitteeDetail
    
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
    def custodian_city(self) -> str:
        """Get custodian_city"""
        return self._data.get("custodian_city")
    @custodian_city.setter
    def custodian_city(self, value: str):
        """Set custodian_city"""
        self._data["custodian_city"] = value

    @property
    def custodian_name_1(self) -> str:
        """Get custodian_name_1"""
        return self._data.get("custodian_name_1")
    @custodian_name_1.setter
    def custodian_name_1(self, value: str):
        """Set custodian_name_1"""
        self._data["custodian_name_1"] = value

    @property
    def custodian_name_2(self) -> str:
        """Get custodian_name_2"""
        return self._data.get("custodian_name_2")
    @custodian_name_2.setter
    def custodian_name_2(self, value: str):
        """Set custodian_name_2"""
        self._data["custodian_name_2"] = value

    @property
    def custodian_name_full(self) -> str:
        """Get custodian_name_full"""
        return self._data.get("custodian_name_full")
    @custodian_name_full.setter
    def custodian_name_full(self, value: str):
        """Set custodian_name_full"""
        self._data["custodian_name_full"] = value

    @property
    def custodian_name_middle(self) -> str:
        """Get custodian_name_middle"""
        return self._data.get("custodian_name_middle")
    @custodian_name_middle.setter
    def custodian_name_middle(self, value: str):
        """Set custodian_name_middle"""
        self._data["custodian_name_middle"] = value

    @property
    def custodian_name_prefix(self) -> str:
        """Get custodian_name_prefix"""
        return self._data.get("custodian_name_prefix")
    @custodian_name_prefix.setter
    def custodian_name_prefix(self, value: str):
        """Set custodian_name_prefix"""
        self._data["custodian_name_prefix"] = value

    @property
    def custodian_name_suffix(self) -> str:
        """Get custodian_name_suffix"""
        return self._data.get("custodian_name_suffix")
    @custodian_name_suffix.setter
    def custodian_name_suffix(self, value: str):
        """Set custodian_name_suffix"""
        self._data["custodian_name_suffix"] = value

    @property
    def custodian_name_title(self) -> str:
        """Get custodian_name_title"""
        return self._data.get("custodian_name_title")
    @custodian_name_title.setter
    def custodian_name_title(self, value: str):
        """Set custodian_name_title"""
        self._data["custodian_name_title"] = value

    @property
    def custodian_phone(self) -> str:
        """Get custodian_phone"""
        return self._data.get("custodian_phone")
    @custodian_phone.setter
    def custodian_phone(self, value: str):
        """Set custodian_phone"""
        self._data["custodian_phone"] = value

    @property
    def custodian_state(self) -> str:
        """Get custodian_state"""
        return self._data.get("custodian_state")
    @custodian_state.setter
    def custodian_state(self, value: str):
        """Set custodian_state"""
        self._data["custodian_state"] = value

    @property
    def custodian_street_1(self) -> str:
        """Get custodian_street_1"""
        return self._data.get("custodian_street_1")
    @custodian_street_1.setter
    def custodian_street_1(self, value: str):
        """Set custodian_street_1"""
        self._data["custodian_street_1"] = value

    @property
    def custodian_street_2(self) -> str:
        """Get custodian_street_2"""
        return self._data.get("custodian_street_2")
    @custodian_street_2.setter
    def custodian_street_2(self, value: str):
        """Set custodian_street_2"""
        self._data["custodian_street_2"] = value

    @property
    def custodian_zip(self) -> str:
        """Get custodian_zip"""
        return self._data.get("custodian_zip")
    @custodian_zip.setter
    def custodian_zip(self, value: str):
        """Set custodian_zip"""
        self._data["custodian_zip"] = value

    @property
    def cycles(self) -> List[int]:
        """Get cycles"""
        return self._data.get("cycles")
    @cycles.setter
    def cycles(self, value: List[int]):
        """Set cycles"""
        self._data["cycles"] = value

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
    def email(self) -> str:
        """Get email"""
        return self._data.get("email")
    @email.setter
    def email(self, value: str):
        """Set email"""
        self._data["email"] = value

    @property
    def fax(self) -> str:
        """Get fax"""
        return self._data.get("fax")
    @fax.setter
    def fax(self, value: str):
        """Set fax"""
        self._data["fax"] = value

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
    def form_type(self) -> str:
        """Get form_type"""
        return self._data.get("form_type")
    @form_type.setter
    def form_type(self, value: str):
        """Set form_type"""
        self._data["form_type"] = value

    @property
    def jfc_committee(self) -> List['JFCCommittee']:
        """Get jfc_committee"""
        return self._data.get("jfc_committee")
    @jfc_committee.setter
    def jfc_committee(self, value: List['JFCCommittee']):
        """Set jfc_committee"""
        self._data["jfc_committee"] = value

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
    def leadership_pac(self) -> str:
        """Get leadership_pac"""
        return self._data.get("leadership_pac")
    @leadership_pac.setter
    def leadership_pac(self, value: str):
        """Set leadership_pac"""
        self._data["leadership_pac"] = value

    @property
    def lobbyist_registrant_pac(self) -> str:
        """Get lobbyist_registrant_pac"""
        return self._data.get("lobbyist_registrant_pac")
    @lobbyist_registrant_pac.setter
    def lobbyist_registrant_pac(self, value: str):
        """Set lobbyist_registrant_pac"""
        self._data["lobbyist_registrant_pac"] = value

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
    def party_type(self) -> str:
        """Get party_type"""
        return self._data.get("party_type")
    @party_type.setter
    def party_type(self, value: str):
        """Set party_type"""
        self._data["party_type"] = value

    @property
    def party_type_full(self) -> str:
        """Get party_type_full"""
        return self._data.get("party_type_full")
    @party_type_full.setter
    def party_type_full(self, value: str):
        """Set party_type_full"""
        self._data["party_type_full"] = value

    @property
    def sponsor_candidate_ids(self) -> List[str]:
        """Get sponsor_candidate_ids"""
        return self._data.get("sponsor_candidate_ids")
    @sponsor_candidate_ids.setter
    def sponsor_candidate_ids(self, value: List[str]):
        """Set sponsor_candidate_ids"""
        self._data["sponsor_candidate_ids"] = value

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
    def treasurer_city(self) -> str:
        """Get treasurer_city"""
        return self._data.get("treasurer_city")
    @treasurer_city.setter
    def treasurer_city(self, value: str):
        """Set treasurer_city"""
        self._data["treasurer_city"] = value

    @property
    def treasurer_name(self) -> str:
        """Get treasurer_name"""
        return self._data.get("treasurer_name")
    @treasurer_name.setter
    def treasurer_name(self, value: str):
        """Set treasurer_name"""
        self._data["treasurer_name"] = value

    @property
    def treasurer_name_1(self) -> str:
        """Get treasurer_name_1"""
        return self._data.get("treasurer_name_1")
    @treasurer_name_1.setter
    def treasurer_name_1(self, value: str):
        """Set treasurer_name_1"""
        self._data["treasurer_name_1"] = value

    @property
    def treasurer_name_2(self) -> str:
        """Get treasurer_name_2"""
        return self._data.get("treasurer_name_2")
    @treasurer_name_2.setter
    def treasurer_name_2(self, value: str):
        """Set treasurer_name_2"""
        self._data["treasurer_name_2"] = value

    @property
    def treasurer_name_middle(self) -> str:
        """Get treasurer_name_middle"""
        return self._data.get("treasurer_name_middle")
    @treasurer_name_middle.setter
    def treasurer_name_middle(self, value: str):
        """Set treasurer_name_middle"""
        self._data["treasurer_name_middle"] = value

    @property
    def treasurer_name_prefix(self) -> str:
        """Get treasurer_name_prefix"""
        return self._data.get("treasurer_name_prefix")
    @treasurer_name_prefix.setter
    def treasurer_name_prefix(self, value: str):
        """Set treasurer_name_prefix"""
        self._data["treasurer_name_prefix"] = value

    @property
    def treasurer_name_suffix(self) -> str:
        """Get treasurer_name_suffix"""
        return self._data.get("treasurer_name_suffix")
    @treasurer_name_suffix.setter
    def treasurer_name_suffix(self, value: str):
        """Set treasurer_name_suffix"""
        self._data["treasurer_name_suffix"] = value

    @property
    def treasurer_name_title(self) -> str:
        """Get treasurer_name_title"""
        return self._data.get("treasurer_name_title")
    @treasurer_name_title.setter
    def treasurer_name_title(self, value: str):
        """Set treasurer_name_title"""
        self._data["treasurer_name_title"] = value

    @property
    def treasurer_phone(self) -> str:
        """Get treasurer_phone"""
        return self._data.get("treasurer_phone")
    @treasurer_phone.setter
    def treasurer_phone(self, value: str):
        """Set treasurer_phone"""
        self._data["treasurer_phone"] = value

    @property
    def treasurer_state(self) -> str:
        """Get treasurer_state"""
        return self._data.get("treasurer_state")
    @treasurer_state.setter
    def treasurer_state(self, value: str):
        """Set treasurer_state"""
        self._data["treasurer_state"] = value

    @property
    def treasurer_street_1(self) -> str:
        """Get treasurer_street_1"""
        return self._data.get("treasurer_street_1")
    @treasurer_street_1.setter
    def treasurer_street_1(self, value: str):
        """Set treasurer_street_1"""
        self._data["treasurer_street_1"] = value

    @property
    def treasurer_street_2(self) -> str:
        """Get treasurer_street_2"""
        return self._data.get("treasurer_street_2")
    @treasurer_street_2.setter
    def treasurer_street_2(self, value: str):
        """Set treasurer_street_2"""
        self._data["treasurer_street_2"] = value

    @property
    def treasurer_zip(self) -> str:
        """Get treasurer_zip"""
        return self._data.get("treasurer_zip")
    @treasurer_zip.setter
    def treasurer_zip(self, value: str):
        """Set treasurer_zip"""
        self._data["treasurer_zip"] = value

    @property
    def website(self) -> str:
        """Get website"""
        return self._data.get("website")
    @website.setter
    def website(self, value: str):
        """Set website"""
        self._data["website"] = value

    @property
    def zip(self) -> str:
        """Get zip"""
        return self._data.get("zip")
    @zip.setter
    def zip(self, value: str):
        """Set zip"""
        self._data["zip"] = value
