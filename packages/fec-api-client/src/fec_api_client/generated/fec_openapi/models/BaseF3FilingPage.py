from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .BaseF3Filing import BaseF3Filing
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class BaseF3FilingPage(BaseModel):
    """
    Strongly-typed model class for BaseF3FilingPage
    
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
    def results(self) -> List['BaseF3Filing']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['BaseF3Filing']):
        """Set results"""
        self._data["results"] = value
