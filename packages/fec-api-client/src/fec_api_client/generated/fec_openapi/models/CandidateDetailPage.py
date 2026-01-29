from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CandidateDetail import CandidateDetail
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class CandidateDetailPage(BaseModel):
    """
    Strongly-typed model class for CandidateDetailPage
    
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
    def results(self) -> List['CandidateDetail']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CandidateDetail']):
        """Set results"""
        self._data["results"] = value
