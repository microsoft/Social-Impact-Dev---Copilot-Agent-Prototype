from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .IETotalsByCandidate import IETotalsByCandidate
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class IETotalsByCandidatePage(BaseModel):
    """
    Strongly-typed model class for IETotalsByCandidatePage
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def pagination(self) -> 'OffsetInfo':
        """Get pagination"""
        return self._data.get("pagination")
    @pagination.setter
    def pagination(self, value: 'OffsetInfo'):
        """Set pagination"""
        self._data["pagination"] = value

    @property
    def results(self) -> List['IETotalsByCandidate']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['IETotalsByCandidate']):
        """Set results"""
        self._data["results"] = value
