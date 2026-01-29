from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .AuditCaseCategoryRelation import AuditCaseCategoryRelation

from ..base.base_model import BaseModel


class AuditCase(BaseModel):
    """
    Strongly-typed model class for AuditCase
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def audit_case_id(self) -> str:
        """Get audit_case_id"""
        return self._data.get("audit_case_id")
    @audit_case_id.setter
    def audit_case_id(self, value: str):
        """Set audit_case_id"""
        self._data["audit_case_id"] = value

    @property
    def audit_id(self) -> int:
        """Get audit_id"""
        return self._data.get("audit_id")
    @audit_id.setter
    def audit_id(self, value: int):
        """Set audit_id"""
        self._data["audit_id"] = value

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

    @property
    def candidate_name(self) -> str:
        """Get candidate_name"""
        return self._data.get("candidate_name")
    @candidate_name.setter
    def candidate_name(self, value: str):
        """Set candidate_name"""
        self._data["candidate_name"] = value

    @property
    def committee_description(self) -> str:
        """Get committee_description"""
        return self._data.get("committee_description")
    @committee_description.setter
    def committee_description(self, value: str):
        """Set committee_description"""
        self._data["committee_description"] = value

    @property
    def committee_designation(self) -> str:
        """Get committee_designation"""
        return self._data.get("committee_designation")
    @committee_designation.setter
    def committee_designation(self, value: str):
        """Set committee_designation"""
        self._data["committee_designation"] = value

    @property
    def committee_id(self) -> str:
        """Get committee_id"""
        return self._data.get("committee_id")
    @committee_id.setter
    def committee_id(self, value: str):
        """Set committee_id"""
        self._data["committee_id"] = value

    @property
    def committee_name(self) -> str:
        """Get committee_name"""
        return self._data.get("committee_name")
    @committee_name.setter
    def committee_name(self, value: str):
        """Set committee_name"""
        self._data["committee_name"] = value

    @property
    def committee_type(self) -> str:
        """Get committee_type"""
        return self._data.get("committee_type")
    @committee_type.setter
    def committee_type(self, value: str):
        """Set committee_type"""
        self._data["committee_type"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def far_release_date(self) -> str:
        """Get far_release_date"""
        return self._data.get("far_release_date")
    @far_release_date.setter
    def far_release_date(self, value: str):
        """Set far_release_date"""
        self._data["far_release_date"] = value

    @property
    def link_to_report(self) -> str:
        """Get link_to_report"""
        return self._data.get("link_to_report")
    @link_to_report.setter
    def link_to_report(self, value: str):
        """Set link_to_report"""
        self._data["link_to_report"] = value

    @property
    def primary_category_list(self) -> List['AuditCaseCategoryRelation']:
        """Get primary_category_list"""
        return self._data.get("primary_category_list")
    @primary_category_list.setter
    def primary_category_list(self, value: List['AuditCaseCategoryRelation']):
        """Set primary_category_list"""
        self._data["primary_category_list"] = value
