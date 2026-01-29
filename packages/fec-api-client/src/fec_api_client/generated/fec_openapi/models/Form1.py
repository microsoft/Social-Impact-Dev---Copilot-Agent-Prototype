from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Form1(BaseModel):
    """
    Strongly-typed model class for Form1
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def affiliated_candidate_id(self) -> str:
        """Get affiliated_candidate_id"""
        return self._data.get("affiliated_candidate_id")
    @affiliated_candidate_id.setter
    def affiliated_candidate_id(self, value: str):
        """Set affiliated_candidate_id"""
        self._data["affiliated_candidate_id"] = value

    @property
    def affiliated_committee_city(self) -> str:
        """Get affiliated_committee_city"""
        return self._data.get("affiliated_committee_city")
    @affiliated_committee_city.setter
    def affiliated_committee_city(self, value: str):
        """Set affiliated_committee_city"""
        self._data["affiliated_committee_city"] = value

    @property
    def affiliated_committee_id(self) -> str:
        """Get affiliated_committee_id"""
        return self._data.get("affiliated_committee_id")
    @affiliated_committee_id.setter
    def affiliated_committee_id(self, value: str):
        """Set affiliated_committee_id"""
        self._data["affiliated_committee_id"] = value

    @property
    def affiliated_committee_name(self) -> str:
        """Get affiliated_committee_name"""
        return self._data.get("affiliated_committee_name")
    @affiliated_committee_name.setter
    def affiliated_committee_name(self, value: str):
        """Set affiliated_committee_name"""
        self._data["affiliated_committee_name"] = value

    @property
    def affiliated_committee_state(self) -> str:
        """Get affiliated_committee_state"""
        return self._data.get("affiliated_committee_state")
    @affiliated_committee_state.setter
    def affiliated_committee_state(self, value: str):
        """Set affiliated_committee_state"""
        self._data["affiliated_committee_state"] = value

    @property
    def affiliated_committee_str1(self) -> str:
        """Get affiliated_committee_str1"""
        return self._data.get("affiliated_committee_str1")
    @affiliated_committee_str1.setter
    def affiliated_committee_str1(self, value: str):
        """Set affiliated_committee_str1"""
        self._data["affiliated_committee_str1"] = value

    @property
    def affiliated_committee_str2(self) -> str:
        """Get affiliated_committee_str2"""
        return self._data.get("affiliated_committee_str2")
    @affiliated_committee_str2.setter
    def affiliated_committee_str2(self, value: str):
        """Set affiliated_committee_str2"""
        self._data["affiliated_committee_str2"] = value

    @property
    def affiliated_committee_zip(self) -> str:
        """Get affiliated_committee_zip"""
        return self._data.get("affiliated_committee_zip")
    @affiliated_committee_zip.setter
    def affiliated_committee_zip(self, value: str):
        """Set affiliated_committee_zip"""
        self._data["affiliated_committee_zip"] = value

    @property
    def affiliated_relationship_code(self) -> str:
        """Get affiliated_relationship_code"""
        return self._data.get("affiliated_relationship_code")
    @affiliated_relationship_code.setter
    def affiliated_relationship_code(self, value: str):
        """Set affiliated_relationship_code"""
        self._data["affiliated_relationship_code"] = value

    @property
    def candidate_district(self) -> str:
        """Get candidate_district"""
        return self._data.get("candidate_district")
    @candidate_district.setter
    def candidate_district(self, value: str):
        """Set candidate_district"""
        self._data["candidate_district"] = value

    @property
    def candidate_first_name(self) -> str:
        """Get candidate_first_name"""
        return self._data.get("candidate_first_name")
    @candidate_first_name.setter
    def candidate_first_name(self, value: str):
        """Set candidate_first_name"""
        self._data["candidate_first_name"] = value

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
    def candidate_middle_name(self) -> str:
        """Get candidate_middle_name"""
        return self._data.get("candidate_middle_name")
    @candidate_middle_name.setter
    def candidate_middle_name(self, value: str):
        """Set candidate_middle_name"""
        self._data["candidate_middle_name"] = value

    @property
    def candidate_name(self) -> str:
        """Get candidate_name"""
        return self._data.get("candidate_name")
    @candidate_name.setter
    def candidate_name(self, value: str):
        """Set candidate_name"""
        self._data["candidate_name"] = value

    @property
    def candidate_office(self) -> str:
        """Get candidate_office"""
        return self._data.get("candidate_office")
    @candidate_office.setter
    def candidate_office(self, value: str):
        """Set candidate_office"""
        self._data["candidate_office"] = value

    @property
    def candidate_party(self) -> str:
        """Get candidate_party"""
        return self._data.get("candidate_party")
    @candidate_party.setter
    def candidate_party(self, value: str):
        """Set candidate_party"""
        self._data["candidate_party"] = value

    @property
    def city(self) -> str:
        """Get city"""
        return self._data.get("city")
    @city.setter
    def city(self, value: str):
        """Set city"""
        self._data["city"] = value

    @property
    def committee_city(self) -> str:
        """Get committee_city"""
        return self._data.get("committee_city")
    @committee_city.setter
    def committee_city(self, value: str):
        """Set committee_city"""
        self._data["committee_city"] = value

    @property
    def committee_id(self) -> str:
        """Get committee_id"""
        return self._data.get("committee_id")
    @committee_id.setter
    def committee_id(self, value: str):
        """Set committee_id"""
        self._data["committee_id"] = value

    @property
    def committee_name(self) -> str:
        """Get committee_name"""
        return self._data.get("committee_name")
    @committee_name.setter
    def committee_name(self, value: str):
        """Set committee_name"""
        self._data["committee_name"] = value

    @property
    def committee_state(self) -> str:
        """Get committee_state"""
        return self._data.get("committee_state")
    @committee_state.setter
    def committee_state(self, value: str):
        """Set committee_state"""
        self._data["committee_state"] = value

    @property
    def committee_str1(self) -> str:
        """Get committee_str1"""
        return self._data.get("committee_str1")
    @committee_str1.setter
    def committee_str1(self, value: str):
        """Set committee_str1"""
        self._data["committee_str1"] = value

    @property
    def committee_str2(self) -> str:
        """Get committee_str2"""
        return self._data.get("committee_str2")
    @committee_str2.setter
    def committee_str2(self, value: str):
        """Set committee_str2"""
        self._data["committee_str2"] = value

    @property
    def committee_type(self) -> str:
        """Get committee_type"""
        return self._data.get("committee_type")
    @committee_type.setter
    def committee_type(self, value: str):
        """Set committee_type"""
        self._data["committee_type"] = value

    @property
    def committee_zip(self) -> str:
        """Get committee_zip"""
        return self._data.get("committee_zip")
    @committee_zip.setter
    def committee_zip(self, value: str):
        """Set committee_zip"""
        self._data["committee_zip"] = value

    @property
    def election_state(self) -> str:
        """Get election_state"""
        return self._data.get("election_state")
    @election_state.setter
    def election_state(self, value: str):
        """Set election_state"""
        self._data["election_state"] = value

    @property
    def email(self) -> str:
        """Get email"""
        return self._data.get("email")
    @email.setter
    def email(self, value: str):
        """Set email"""
        self._data["email"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def image_number(self) -> str:
        """Get image_number"""
        return self._data.get("image_number")
    @image_number.setter
    def image_number(self, value: str):
        """Set image_number"""
        self._data["image_number"] = value

    @property
    def load_timestamp(self) -> str:
        """Get load_timestamp"""
        return self._data.get("load_timestamp")
    @load_timestamp.setter
    def load_timestamp(self, value: str):
        """Set load_timestamp"""
        self._data["load_timestamp"] = value

    @property
    def organization_type(self) -> str:
        """Get organization_type"""
        return self._data.get("organization_type")
    @organization_type.setter
    def organization_type(self, value: str):
        """Set organization_type"""
        self._data["organization_type"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

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
    def treasurer_first_name(self) -> str:
        """Get treasurer_first_name"""
        return self._data.get("treasurer_first_name")
    @treasurer_first_name.setter
    def treasurer_first_name(self, value: str):
        """Set treasurer_first_name"""
        self._data["treasurer_first_name"] = value

    @property
    def treasurer_last_name(self) -> str:
        """Get treasurer_last_name"""
        return self._data.get("treasurer_last_name")
    @treasurer_last_name.setter
    def treasurer_last_name(self, value: str):
        """Set treasurer_last_name"""
        self._data["treasurer_last_name"] = value

    @property
    def treasurer_middle_name(self) -> str:
        """Get treasurer_middle_name"""
        return self._data.get("treasurer_middle_name")
    @treasurer_middle_name.setter
    def treasurer_middle_name(self, value: str):
        """Set treasurer_middle_name"""
        self._data["treasurer_middle_name"] = value

    @property
    def treasurer_state(self) -> str:
        """Get treasurer_state"""
        return self._data.get("treasurer_state")
    @treasurer_state.setter
    def treasurer_state(self, value: str):
        """Set treasurer_state"""
        self._data["treasurer_state"] = value

    @property
    def treasurer_str1(self) -> str:
        """Get treasurer_str1"""
        return self._data.get("treasurer_str1")
    @treasurer_str1.setter
    def treasurer_str1(self, value: str):
        """Set treasurer_str1"""
        self._data["treasurer_str1"] = value

    @property
    def treasurer_str2(self) -> str:
        """Get treasurer_str2"""
        return self._data.get("treasurer_str2")
    @treasurer_str2.setter
    def treasurer_str2(self, value: str):
        """Set treasurer_str2"""
        self._data["treasurer_str2"] = value

    @property
    def treasurer_zip(self) -> str:
        """Get treasurer_zip"""
        return self._data.get("treasurer_zip")
    @treasurer_zip.setter
    def treasurer_zip(self, value: str):
        """Set treasurer_zip"""
        self._data["treasurer_zip"] = value

    @property
    def zip(self) -> str:
        """Get zip"""
        return self._data.get("zip")
    @zip.setter
    def zip(self, value: str):
        """Set zip"""
        self._data["zip"] = value
