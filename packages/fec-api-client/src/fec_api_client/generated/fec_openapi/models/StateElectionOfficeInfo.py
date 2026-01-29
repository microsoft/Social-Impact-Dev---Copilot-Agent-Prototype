from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class StateElectionOfficeInfo(BaseModel):
    """
    Strongly-typed model class for StateElectionOfficeInfo
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def address_line1(self) -> str:
        """Get address_line1"""
        return self._data.get("address_line1")
    @address_line1.setter
    def address_line1(self, value: str):
        """Set address_line1"""
        self._data["address_line1"] = value

    @property
    def address_line2(self) -> str:
        """Get address_line2"""
        return self._data.get("address_line2")
    @address_line2.setter
    def address_line2(self, value: str):
        """Set address_line2"""
        self._data["address_line2"] = value

    @property
    def city(self) -> str:
        """Get city"""
        return self._data.get("city")
    @city.setter
    def city(self, value: str):
        """Set city"""
        self._data["city"] = value

    @property
    def email(self) -> str:
        """Get email"""
        return self._data.get("email")
    @email.setter
    def email(self, value: str):
        """Set email"""
        self._data["email"] = value

    @property
    def fax_number(self) -> str:
        """Get fax_number"""
        return self._data.get("fax_number")
    @fax_number.setter
    def fax_number(self, value: str):
        """Set fax_number"""
        self._data["fax_number"] = value

    @property
    def mailing_address1(self) -> str:
        """Get mailing_address1"""
        return self._data.get("mailing_address1")
    @mailing_address1.setter
    def mailing_address1(self, value: str):
        """Set mailing_address1"""
        self._data["mailing_address1"] = value

    @property
    def mailing_address2(self) -> str:
        """Get mailing_address2"""
        return self._data.get("mailing_address2")
    @mailing_address2.setter
    def mailing_address2(self, value: str):
        """Set mailing_address2"""
        self._data["mailing_address2"] = value

    @property
    def mailing_city(self) -> str:
        """Get mailing_city"""
        return self._data.get("mailing_city")
    @mailing_city.setter
    def mailing_city(self, value: str):
        """Set mailing_city"""
        self._data["mailing_city"] = value

    @property
    def mailing_state(self) -> str:
        """Get mailing_state"""
        return self._data.get("mailing_state")
    @mailing_state.setter
    def mailing_state(self, value: str):
        """Set mailing_state"""
        self._data["mailing_state"] = value

    @property
    def mailing_zipcode(self) -> str:
        """Get mailing_zipcode"""
        return self._data.get("mailing_zipcode")
    @mailing_zipcode.setter
    def mailing_zipcode(self, value: str):
        """Set mailing_zipcode"""
        self._data["mailing_zipcode"] = value

    @property
    def office_name(self) -> str:
        """Get office_name"""
        return self._data.get("office_name")
    @office_name.setter
    def office_name(self, value: str):
        """Set office_name"""
        self._data["office_name"] = value

    @property
    def office_type(self) -> str:
        """Get office_type"""
        return self._data.get("office_type")
    @office_type.setter
    def office_type(self, value: str):
        """Set office_type"""
        self._data["office_type"] = value

    @property
    def primary_phone_number(self) -> str:
        """Get primary_phone_number"""
        return self._data.get("primary_phone_number")
    @primary_phone_number.setter
    def primary_phone_number(self, value: str):
        """Set primary_phone_number"""
        self._data["primary_phone_number"] = value

    @property
    def secondary_phone_number(self) -> str:
        """Get secondary_phone_number"""
        return self._data.get("secondary_phone_number")
    @secondary_phone_number.setter
    def secondary_phone_number(self, value: str):
        """Set secondary_phone_number"""
        self._data["secondary_phone_number"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

    @property
    def state_full_name(self) -> str:
        """Get state_full_name"""
        return self._data.get("state_full_name")
    @state_full_name.setter
    def state_full_name(self, value: str):
        """Set state_full_name"""
        self._data["state_full_name"] = value

    @property
    def website_url1(self) -> str:
        """Get website_url1"""
        return self._data.get("website_url1")
    @website_url1.setter
    def website_url1(self, value: str):
        """Set website_url1"""
        self._data["website_url1"] = value

    @property
    def website_url2(self) -> str:
        """Get website_url2"""
        return self._data.get("website_url2")
    @website_url2.setter
    def website_url2(self, value: str):
        """Set website_url2"""
        self._data["website_url2"] = value

    @property
    def zip_code(self) -> str:
        """Get zip_code"""
        return self._data.get("zip_code")
    @zip_code.setter
    def zip_code(self, value: str):
        """Set zip_code"""
        self._data["zip_code"] = value
