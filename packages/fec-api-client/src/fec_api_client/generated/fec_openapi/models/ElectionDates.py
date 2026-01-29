from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ElectionDates(BaseModel):
    """
    Strongly-typed model class for ElectionDates
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def active_election(self) -> bool:
        """Get active_election"""
        return self._data.get("active_election")
    @active_election.setter
    def active_election(self, value: bool):
        """Set active_election"""
        self._data["active_election"] = value

    @property
    def create_date(self) -> str:
        """Get create_date"""
        return self._data.get("create_date")
    @create_date.setter
    def create_date(self, value: str):
        """Set create_date"""
        self._data["create_date"] = value

    @property
    def election_date(self) -> str:
        """Get election_date"""
        return self._data.get("election_date")
    @election_date.setter
    def election_date(self, value: str):
        """Set election_date"""
        self._data["election_date"] = value

    @property
    def election_district(self) -> str:
        """Get election_district"""
        return self._data.get("election_district")
    @election_district.setter
    def election_district(self, value: str):
        """Set election_district"""
        self._data["election_district"] = value

    @property
    def election_notes(self) -> str:
        """Get election_notes"""
        return self._data.get("election_notes")
    @election_notes.setter
    def election_notes(self, value: str):
        """Set election_notes"""
        self._data["election_notes"] = value

    @property
    def election_party(self) -> str:
        """Get election_party"""
        return self._data.get("election_party")
    @election_party.setter
    def election_party(self, value: str):
        """Set election_party"""
        self._data["election_party"] = value

    @property
    def election_state(self) -> str:
        """Get election_state"""
        return self._data.get("election_state")
    @election_state.setter
    def election_state(self, value: str):
        """Set election_state"""
        self._data["election_state"] = value

    @property
    def election_type_full(self) -> str:
        """Get election_type_full"""
        return self._data.get("election_type_full")
    @election_type_full.setter
    def election_type_full(self, value: str):
        """Set election_type_full"""
        self._data["election_type_full"] = value

    @property
    def election_type_id(self) -> str:
        """Get election_type_id"""
        return self._data.get("election_type_id")
    @election_type_id.setter
    def election_type_id(self, value: str):
        """Set election_type_id"""
        self._data["election_type_id"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def office_sought(self) -> str:
        """Get office_sought"""
        return self._data.get("office_sought")
    @office_sought.setter
    def office_sought(self, value: str):
        """Set office_sought"""
        self._data["office_sought"] = value

    @property
    def primary_general_date(self) -> str:
        """Get primary_general_date"""
        return self._data.get("primary_general_date")
    @primary_general_date.setter
    def primary_general_date(self, value: str):
        """Set primary_general_date"""
        self._data["primary_general_date"] = value

    @property
    def update_date(self) -> str:
        """Get update_date"""
        return self._data.get("update_date")
    @update_date.setter
    def update_date(self, value: str):
        """Set update_date"""
        self._data["update_date"] = value
