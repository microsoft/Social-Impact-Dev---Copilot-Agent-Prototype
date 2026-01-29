from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Form2(BaseModel):
    """
    Strongly-typed model class for Form2
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def address_city(self) -> str:
        """Get address_city"""
        return self._data.get("address_city")
    @address_city.setter
    def address_city(self, value: str):
        """Set address_city"""
        self._data["address_city"] = value

    @property
    def address_state(self) -> str:
        """Get address_state"""
        return self._data.get("address_state")
    @address_state.setter
    def address_state(self, value: str):
        """Set address_state"""
        self._data["address_state"] = value

    @property
    def address_str1(self) -> str:
        """Get address_str1"""
        return self._data.get("address_str1")
    @address_str1.setter
    def address_str1(self, value: str):
        """Set address_str1"""
        self._data["address_str1"] = value

    @property
    def address_str2(self) -> str:
        """Get address_str2"""
        return self._data.get("address_str2")
    @address_str2.setter
    def address_str2(self, value: str):
        """Set address_str2"""
        self._data["address_str2"] = value

    @property
    def address_zip(self) -> str:
        """Get address_zip"""
        return self._data.get("address_zip")
    @address_zip.setter
    def address_zip(self, value: str):
        """Set address_zip"""
        self._data["address_zip"] = value

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
    def committee_address_city(self) -> str:
        """Get committee_address_city"""
        return self._data.get("committee_address_city")
    @committee_address_city.setter
    def committee_address_city(self, value: str):
        """Set committee_address_city"""
        self._data["committee_address_city"] = value

    @property
    def committee_address_str1(self) -> str:
        """Get committee_address_str1"""
        return self._data.get("committee_address_str1")
    @committee_address_str1.setter
    def committee_address_str1(self, value: str):
        """Set committee_address_str1"""
        self._data["committee_address_str1"] = value

    @property
    def committee_address_str2(self) -> str:
        """Get committee_address_str2"""
        return self._data.get("committee_address_str2")
    @committee_address_str2.setter
    def committee_address_str2(self, value: str):
        """Set committee_address_str2"""
        self._data["committee_address_str2"] = value

    @property
    def committee_address_zip(self) -> str:
        """Get committee_address_zip"""
        return self._data.get("committee_address_zip")
    @committee_address_zip.setter
    def committee_address_zip(self, value: str):
        """Set committee_address_zip"""
        self._data["committee_address_zip"] = value

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
    def election_state(self) -> str:
        """Get election_state"""
        return self._data.get("election_state")
    @election_state.setter
    def election_state(self, value: str):
        """Set election_state"""
        self._data["election_state"] = value

    @property
    def election_year(self) -> str:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: str):
        """Set election_year"""
        self._data["election_year"] = value

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
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value
