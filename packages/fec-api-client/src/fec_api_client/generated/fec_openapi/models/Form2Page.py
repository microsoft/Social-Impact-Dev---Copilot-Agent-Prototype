from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .Form2 import Form2
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class Form2Page(BaseModel):
    """
    Strongly-typed model class for Form2Page
    
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
    def results(self) -> List['Form2']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['Form2']):
        """Set results"""
        self._data["results"] = value
