from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .ScheduleH4 import ScheduleH4
    from .SeekInfo import SeekInfo

from ..base.base_model import BaseModel


class ScheduleH4Page(BaseModel):
    """
    Strongly-typed model class for ScheduleH4Page
    
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
    def results(self) -> List['ScheduleH4']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['ScheduleH4']):
        """Set results"""
        self._data["results"] = value
