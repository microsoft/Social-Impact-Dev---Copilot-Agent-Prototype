from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CandidateTotalsDetailPresidential import CandidateTotalsDetailPresidential
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class CandidateTotalsDetailPresidentialPage(BaseModel):
    """
    Strongly-typed model class for CandidateTotalsDetailPresidentialPage
    
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
    def results(self) -> List['CandidateTotalsDetailPresidential']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CandidateTotalsDetailPresidential']):
        """Set results"""
        self._data["results"] = value
