from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .ScheduleE import ScheduleE
    from .SeekInfo import SeekInfo

from ..base.base_model import BaseModel


class ScheduleEPage(BaseModel):
    """
    Strongly-typed model class for ScheduleEPage
    
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
    def results(self) -> List['ScheduleE']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['ScheduleE']):
        """Set results"""
        self._data["results"] = value
