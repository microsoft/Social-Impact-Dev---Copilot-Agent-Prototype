from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CalendarDate(BaseModel):
    """
    Strongly-typed model class for CalendarDate
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def all_day(self) -> bool:
        """Get all_day"""
        return self._data.get("all_day")
    @all_day.setter
    def all_day(self, value: bool):
        """Set all_day"""
        self._data["all_day"] = value

    @property
    def calendar_category_id(self) -> int:
        """Get calendar_category_id"""
        return self._data.get("calendar_category_id")
    @calendar_category_id.setter
    def calendar_category_id(self, value: int):
        """Set calendar_category_id"""
        self._data["calendar_category_id"] = value

    @property
    def category(self) -> str:
        """Get category"""
        return self._data.get("category")
    @category.setter
    def category(self, value: str):
        """Set category"""
        self._data["category"] = value

    @property
    def description(self) -> str:
        """Get description"""
        return self._data.get("description")
    @description.setter
    def description(self, value: str):
        """Set description"""
        self._data["description"] = value

    @property
    def end_date(self) -> str:
        """Get end_date"""
        return self._data.get("end_date")
    @end_date.setter
    def end_date(self, value: str):
        """Set end_date"""
        self._data["end_date"] = value

    @property
    def event_id(self) -> int:
        """Get event_id"""
        return self._data.get("event_id")
    @event_id.setter
    def event_id(self, value: int):
        """Set event_id"""
        self._data["event_id"] = value

    @property
    def location(self) -> str:
        """Get location"""
        return self._data.get("location")
    @location.setter
    def location(self, value: str):
        """Set location"""
        self._data["location"] = value

    @property
    def start_date(self) -> str:
        """Get start_date"""
        return self._data.get("start_date")
    @start_date.setter
    def start_date(self, value: str):
        """Set start_date"""
        self._data["start_date"] = value

    @property
    def state(self) -> List[str]:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: List[str]):
        """Set state"""
        self._data["state"] = value

    @property
    def summary(self) -> str:
        """Get summary"""
        return self._data.get("summary")
    @summary.setter
    def summary(self, value: str):
        """Set summary"""
        self._data["summary"] = value

    @property
    def url(self) -> str:
        """Get url"""
        return self._data.get("url")
    @url.setter
    def url(self, value: str):
        """Set url"""
        self._data["url"] = value
