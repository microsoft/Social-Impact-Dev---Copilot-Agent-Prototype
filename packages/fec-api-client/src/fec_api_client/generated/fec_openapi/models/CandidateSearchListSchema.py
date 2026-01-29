from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CandidateSearchBaseSchema import CandidateSearchBaseSchema

from ..base.base_model import BaseModel


class CandidateSearchListSchema(BaseModel):
    """
    Strongly-typed model class for CandidateSearchListSchema
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def results(self) -> List['CandidateSearchBaseSchema']:
        """Get results"""
        return self._data.get("results")
    @results.setter
    def results(self, value: List['CandidateSearchBaseSchema']):
        """Set results"""
        self._data["results"] = value
