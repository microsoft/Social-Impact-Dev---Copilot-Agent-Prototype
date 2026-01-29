from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class ElectionSummary(BaseModel):
    """
    Strongly-typed model class for ElectionSummary
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def count(self) -> int:
        """Get count"""
        return self._data.get("count")
    @count.setter
    def count(self, value: int):
        """Set count"""
        self._data["count"] = value

    @property
    def disbursements(self) -> float:
        """Get disbursements"""
        return self._data.get("disbursements")
    @disbursements.setter
    def disbursements(self, value: float):
        """Set disbursements"""
        self._data["disbursements"] = value

    @property
    def independent_expenditures(self) -> float:
        """Get independent_expenditures"""
        return self._data.get("independent_expenditures")
    @independent_expenditures.setter
    def independent_expenditures(self, value: float):
        """Set independent_expenditures"""
        self._data["independent_expenditures"] = value

    @property
    def receipts(self) -> float:
        """Get receipts"""
        return self._data.get("receipts")
    @receipts.setter
    def receipts(self, value: float):
        """Set receipts"""
        self._data["receipts"] = value
