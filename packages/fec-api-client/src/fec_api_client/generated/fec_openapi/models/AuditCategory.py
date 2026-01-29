from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .AuditCategoryRelation import AuditCategoryRelation

from ..base.base_model import BaseModel


class AuditCategory(BaseModel):
    """
    Strongly-typed model class for AuditCategory
    
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

    @property
    def sub_category_list(self) -> List['AuditCategoryRelation']:
        """Get sub_category_list"""
        return self._data.get("sub_category_list")
    @sub_category_list.setter
    def sub_category_list(self, value: List['AuditCategoryRelation']):
        """Set sub_category_list"""
        self._data["sub_category_list"] = value
