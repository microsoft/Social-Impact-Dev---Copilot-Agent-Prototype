from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class AuditPrimaryCategory(BaseModel):
    """
    Strongly-typed model class for AuditPrimaryCategory
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def primary_category_id(self) -> str:
        """Get primary_category_id"""
        return self._data.get("primary_category_id")
    @primary_category_id.setter
    def primary_category_id(self, value: str):
        """Set primary_category_id"""
        self._data["primary_category_id"] = value

    @property
    def primary_category_name(self) -> str:
        """Get primary_category_name"""
        return self._data.get("primary_category_name")
    @primary_category_name.setter
    def primary_category_name(self, value: str):
        """Set primary_category_name"""
        self._data["primary_category_name"] = value
