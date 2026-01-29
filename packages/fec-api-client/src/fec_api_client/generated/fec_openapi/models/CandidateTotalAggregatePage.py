from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CandidateTotalAggregate import CandidateTotalAggregate
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class CandidateTotalAggregatePage(BaseModel):
    """
    Strongly-typed model class for CandidateTotalAggregatePage
    
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
    def results(self) -> List['CandidateTotalAggregate']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CandidateTotalAggregate']):
        """Set results"""
        self._data["results"] = value
