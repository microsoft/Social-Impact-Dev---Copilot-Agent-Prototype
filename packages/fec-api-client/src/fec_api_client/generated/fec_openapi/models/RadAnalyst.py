from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class RadAnalyst(BaseModel):
    """
    Strongly-typed model class for RadAnalyst
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def analyst_id(self) -> float:
        """Get analyst_id"""
        return self._data.get("analyst_id")
    @analyst_id.setter
    def analyst_id(self, value: float):
        """Set analyst_id"""
        self._data["analyst_id"] = value

    @property
    def analyst_short_id(self) -> float:
        """Get analyst_short_id"""
        return self._data.get("analyst_short_id")
    @analyst_short_id.setter
    def analyst_short_id(self, value: float):
        """Set analyst_short_id"""
        self._data["analyst_short_id"] = value

    @property
    def assignment_update_date(self) -> str:
        """Get assignment_update_date"""
        return self._data.get("assignment_update_date")
    @assignment_update_date.setter
    def assignment_update_date(self, value: str):
        """Set assignment_update_date"""
        self._data["assignment_update_date"] = value

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
    def email(self) -> str:
        """Get email"""
        return self._data.get("email")
    @email.setter
    def email(self, value: str):
        """Set email"""
        self._data["email"] = value

    @property
    def first_name(self) -> str:
        """Get first_name"""
        return self._data.get("first_name")
    @first_name.setter
    def first_name(self, value: str):
        """Set first_name"""
        self._data["first_name"] = value

    @property
    def last_name(self) -> str:
        """Get last_name"""
        return self._data.get("last_name")
    @last_name.setter
    def last_name(self, value: str):
        """Set last_name"""
        self._data["last_name"] = value

    @property
    def rad_branch(self) -> str:
        """Get rad_branch"""
        return self._data.get("rad_branch")
    @rad_branch.setter
    def rad_branch(self, value: str):
        """Set rad_branch"""
        self._data["rad_branch"] = value

    @property
    def telephone_ext(self) -> float:
        """Get telephone_ext"""
        return self._data.get("telephone_ext")
    @telephone_ext.setter
    def telephone_ext(self, value: float):
        """Set telephone_ext"""
        self._data["telephone_ext"] = value

    @property
    def title(self) -> str:
        """Get title"""
        return self._data.get("title")
    @title.setter
    def title(self, value: str):
        """Set title"""
        self._data["title"] = value
