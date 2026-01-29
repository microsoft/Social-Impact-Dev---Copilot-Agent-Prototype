from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ElectionSearch(BaseModel):
    """
    Strongly-typed model class for ElectionSearch
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def candidate_status(self) -> str:
        """Get candidate_status"""
        return self._data.get("candidate_status")
    @candidate_status.setter
    def candidate_status(self, value: str):
        """Set candidate_status"""
        self._data["candidate_status"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def district(self) -> str:
        """Get district"""
        return self._data.get("district")
    @district.setter
    def district(self, value: str):
        """Set district"""
        self._data["district"] = value

    @property
    def incumbent_id(self) -> str:
        """Get incumbent_id"""
        return self._data.get("incumbent_id")
    @incumbent_id.setter
    def incumbent_id(self, value: str):
        """Set incumbent_id"""
        self._data["incumbent_id"] = value

    @property
    def incumbent_name(self) -> str:
        """Get incumbent_name"""
        return self._data.get("incumbent_name")
    @incumbent_name.setter
    def incumbent_name(self, value: str):
        """Set incumbent_name"""
        self._data["incumbent_name"] = value

    @property
    def office(self) -> str:
        """Get office"""
        return self._data.get("office")
    @office.setter
    def office(self, value: str):
        """Set office"""
        self._data["office"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value
