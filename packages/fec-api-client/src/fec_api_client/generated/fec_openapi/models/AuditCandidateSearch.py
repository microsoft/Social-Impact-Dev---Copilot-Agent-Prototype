from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class AuditCandidateSearch(BaseModel):
    """
    Strongly-typed model class for AuditCandidateSearch
    
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
    def name(self) -> str:
        """Get name"""
        return self._data.get("name")
    @name.setter
    def name(self, value: str):
        """Set name"""
        self._data["name"] = value
