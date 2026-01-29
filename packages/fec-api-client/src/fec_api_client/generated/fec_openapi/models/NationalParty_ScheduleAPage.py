from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .NationalParty_ScheduleA import NationalParty_ScheduleA
    from .OffsetInfo import OffsetInfo

from ..base.base_model import BaseModel


class NationalParty_ScheduleAPage(BaseModel):
    """
    Strongly-typed model class for NationalParty_ScheduleAPage
    
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
    def results(self) -> List['NationalParty_ScheduleA']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['NationalParty_ScheduleA']):
        """Set results"""
        self._data["results"] = value
