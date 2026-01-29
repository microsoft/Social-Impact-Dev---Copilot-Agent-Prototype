from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CommitteeSearch(BaseModel):
    """
    Strongly-typed model class for CommitteeSearch
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def id(self) -> str:
        """Get id"""
        return self._data.get("id")
    @id.setter
    def id(self, value: str):
        """Set id"""
        self._data["id"] = value

    @property
    def is_active(self) -> bool:
        """Get is_active"""
        return self._data.get("is_active")
    @is_active.setter
    def is_active(self, value: bool):
        """Set is_active"""
        self._data["is_active"] = value

    @property
    def name(self) -> str:
        """Get name"""
        return self._data.get("name")
    @name.setter
    def name(self, value: str):
        """Set name"""
        self._data["name"] = value
