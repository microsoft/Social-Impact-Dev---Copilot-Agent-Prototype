from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ReportType(BaseModel):
    """
    Strongly-typed model class for ReportType
    
    Generated from OpenAPI/Swagger specification
    """

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
