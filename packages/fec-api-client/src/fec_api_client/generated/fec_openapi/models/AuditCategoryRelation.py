from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class AuditCategoryRelation(BaseModel):
    """
    Strongly-typed model class for AuditCategoryRelation
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def sub_category_id(self) -> str:
        """Get sub_category_id"""
        return self._data.get("sub_category_id")
    @sub_category_id.setter
    def sub_category_id(self, value: str):
        """Set sub_category_id"""
        self._data["sub_category_id"] = value

    @property
    def sub_category_name(self) -> str:
        """Get sub_category_name"""
        return self._data.get("sub_category_name")
    @sub_category_name.setter
    def sub_category_name(self, value: str):
        """Set sub_category_name"""
        self._data["sub_category_name"] = value
