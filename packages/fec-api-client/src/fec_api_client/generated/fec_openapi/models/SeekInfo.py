from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class SeekInfo(BaseModel):
    """
    Strongly-typed model class for SeekInfo
    
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
    def is_count_exact(self) -> bool:
        """Get is_count_exact"""
        return self._data.get("is_count_exact")
    @is_count_exact.setter
    def is_count_exact(self, value: bool):
        """Set is_count_exact"""
        self._data["is_count_exact"] = value

    @property
    def last_indexes(self) -> str:
        """Get last_indexes"""
        return self._data.get("last_indexes")
    @last_indexes.setter
    def last_indexes(self, value: str):
        """Set last_indexes"""
        self._data["last_indexes"] = value

    @property
    def pages(self) -> int:
        """Get pages"""
        return self._data.get("pages")
    @pages.setter
    def pages(self, value: int):
        """Set pages"""
        self._data["pages"] = value

    @property
    def per_page(self) -> int:
        """Get per_page"""
        return self._data.get("per_page")
    @per_page.setter
    def per_page(self, value: int):
        """Set per_page"""
        self._data["per_page"] = value
