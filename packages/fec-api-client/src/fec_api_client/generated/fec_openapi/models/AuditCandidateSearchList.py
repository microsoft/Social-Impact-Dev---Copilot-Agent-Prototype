from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .AuditCandidateSearch import AuditCandidateSearch

from ..base.base_model import BaseModel


class AuditCandidateSearchList(BaseModel):
    """
    Strongly-typed model class for AuditCandidateSearchList
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def results(self) -> List['AuditCandidateSearch']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['AuditCandidateSearch']):
        """Set results"""
        self._data["results"] = value
