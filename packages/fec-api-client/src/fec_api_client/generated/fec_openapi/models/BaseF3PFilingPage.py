from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .BaseF3PFiling import BaseF3PFiling
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class BaseF3PFilingPage(BaseModel):
    """
    Strongly-typed model class for BaseF3PFilingPage
    
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
    def results(self) -> List['BaseF3PFiling']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['BaseF3PFiling']):
        """Set results"""
        self._data["results"] = value
