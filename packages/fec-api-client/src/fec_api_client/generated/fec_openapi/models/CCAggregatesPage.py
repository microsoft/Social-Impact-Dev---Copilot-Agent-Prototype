from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CCAggregates import CCAggregates
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class CCAggregatesPage(BaseModel):
    """
    Strongly-typed model class for CCAggregatesPage
    
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
    def results(self) -> List['CCAggregates']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CCAggregates']):
        """Set results"""
        self._data["results"] = value
