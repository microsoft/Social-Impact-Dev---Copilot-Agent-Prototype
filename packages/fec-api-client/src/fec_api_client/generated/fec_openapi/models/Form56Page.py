from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .Form56 import Form56
    from .SeekInfo import SeekInfo

from ..base.base_model import BaseModel


class Form56Page(BaseModel):
    """
    Strongly-typed model class for Form56Page
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def pagination(self) -> 'SeekInfo':
        """Get pagination"""
        return self._data.get("pagination")
    @pagination.setter
    def pagination(self, value: 'SeekInfo'):
        """Set pagination"""
        self._data["pagination"] = value

    @property
    def results(self) -> List['Form56']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['Form56']):
        """Set results"""
        self._data["results"] = value
