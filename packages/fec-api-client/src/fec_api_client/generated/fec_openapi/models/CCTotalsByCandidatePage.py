from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CCTotalsByCandidate import CCTotalsByCandidate
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class CCTotalsByCandidatePage(BaseModel):
    """
    Strongly-typed model class for CCTotalsByCandidatePage
    
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
    def results(self) -> List['CCTotalsByCandidate']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CCTotalsByCandidate']):
        """Set results"""
        self._data["results"] = value
