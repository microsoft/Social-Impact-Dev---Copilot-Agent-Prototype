from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ReportingDates(BaseModel):
    """
    Strongly-typed model class for ReportingDates
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def create_date(self) -> str:
        """Get create_date"""
        return self._data.get("create_date")
    @create_date.setter
    def create_date(self, value: str):
        """Set create_date"""
        self._data["create_date"] = value

    @property
    def due_date(self) -> str:
        """Get due_date"""
        return self._data.get("due_date")
    @due_date.setter
    def due_date(self, value: str):
        """Set due_date"""
        self._data["due_date"] = value

    @property
    def report_type(self) -> str:
        """Get report_type"""
        return self._data.get("report_type")
    @report_type.setter
    def report_type(self, value: str):
        """Set report_type"""
        self._data["report_type"] = value

    @property
    def report_type_full(self) -> str:
        """Get report_type_full"""
        return self._data.get("report_type_full")
    @report_type_full.setter
    def report_type_full(self, value: str):
        """Set report_type_full"""
        self._data["report_type_full"] = value

    @property
    def report_year(self) -> int:
        """Get report_year"""
        return self._data.get("report_year")
    @report_year.setter
    def report_year(self, value: int):
        """Set report_year"""
        self._data["report_year"] = value

    @property
    def update_date(self) -> str:
        """Get update_date"""
        return self._data.get("update_date")
    @update_date.setter
    def update_date(self, value: str):
        """Set update_date"""
        self._data["update_date"] = value
