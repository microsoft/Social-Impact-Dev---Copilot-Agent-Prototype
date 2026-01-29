from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .OffsetInfo import OffsetInfo
    from .ScheduleEEfile import ScheduleEEfile

from ..base.base_model import BaseModel


class ScheduleEEfilePage(BaseModel):
    """
    Strongly-typed model class for ScheduleEEfilePage
    
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
    def results(self) -> List['ScheduleEEfile']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['ScheduleEEfile']):
        """Set results"""
        self._data["results"] = value
