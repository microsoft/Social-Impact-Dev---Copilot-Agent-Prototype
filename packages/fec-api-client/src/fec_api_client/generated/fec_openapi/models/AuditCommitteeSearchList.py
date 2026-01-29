from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .AuditCommitteeSearch import AuditCommitteeSearch

from ..base.base_model import BaseModel


class AuditCommitteeSearchList(BaseModel):
    """
    Strongly-typed model class for AuditCommitteeSearchList
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def results(self) -> List['AuditCommitteeSearch']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['AuditCommitteeSearch']):
        """Set results"""
        self._data["results"] = value
