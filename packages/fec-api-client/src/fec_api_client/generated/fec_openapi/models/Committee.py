from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .PacSponsorCandidate import PacSponsorCandidate

from ..base.base_model import BaseModel


class Committee(BaseModel):
    """
    Strongly-typed model class for Committee
    
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
    def sponsor_candidate_ids(self) -> List[str]:
        """Get sponsor_candidate_ids"""
        return self._data.get("sponsor_candidate_ids")
    @sponsor_candidate_ids.setter
    def sponsor_candidate_ids(self, value: List[str]):
        """Set sponsor_candidate_ids"""
        self._data["sponsor_candidate_ids"] = value

    @property
    def sponsor_candidate_list(self) -> List['PacSponsorCandidate']:
        """Get sponsor_candidate_list"""
        return self._data.get("sponsor_candidate_list")
    @sponsor_candidate_list.setter
    def sponsor_candidate_list(self, value: List['PacSponsorCandidate']):
        """Set sponsor_candidate_list"""
        self._data["sponsor_candidate_list"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

    @property
    def treasurer_name(self) -> str:
        """Get treasurer_name"""
        return self._data.get("treasurer_name")
    @treasurer_name.setter
    def treasurer_name(self, value: str):
        """Set treasurer_name"""
        self._data["treasurer_name"] = value
