from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class EfilingsAmendments(BaseModel):
    """
    Strongly-typed model class for EfilingsAmendments
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def amendment_chain(self) -> List[int]:
        """Get amendment_chain"""
        return self._data.get("amendment_chain")
    @amendment_chain.setter
    def amendment_chain(self, value: List[int]):
        """Set amendment_chain"""
        self._data["amendment_chain"] = value

    @property
    def depth(self) -> float:
        """Get depth"""
        return self._data.get("depth")
    @depth.setter
    def depth(self, value: float):
        """Set depth"""
        self._data["depth"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def last(self) -> float:
        """Get last"""
        return self._data.get("last")
    @last.setter
    def last(self, value: float):
        """Set last"""
        self._data["last"] = value

    @property
    def longest_chain(self) -> float:
        """Get longest_chain"""
        return self._data.get("longest_chain")
    @longest_chain.setter
    def longest_chain(self, value: float):
        """Set longest_chain"""
        self._data["longest_chain"] = value

    @property
    def most_recent_filing(self) -> float:
        """Get most_recent_filing"""
        return self._data.get("most_recent_filing")
    @most_recent_filing.setter
    def most_recent_filing(self, value: float):
        """Set most_recent_filing"""
        self._data["most_recent_filing"] = value

    @property
    def previous_file_number(self) -> float:
        """Get previous_file_number"""
        return self._data.get("previous_file_number")
    @previous_file_number.setter
    def previous_file_number(self, value: float):
        """Set previous_file_number"""
        self._data["previous_file_number"] = value
