from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeSearch import CommitteeSearch

from ..base.base_model import BaseModel


class CommitteeSearchList(BaseModel):
    """
    Strongly-typed model class for CommitteeSearchList
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def results(self) -> List['CommitteeSearch']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CommitteeSearch']):
        """Set results"""
        self._data["results"] = value
