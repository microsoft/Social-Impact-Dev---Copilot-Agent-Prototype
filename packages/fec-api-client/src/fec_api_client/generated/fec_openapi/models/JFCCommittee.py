from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class JFCCommittee(BaseModel):
    """
    Strongly-typed model class for JFCCommittee
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def joint_committee_id(self) -> str:
        """Get joint_committee_id"""
        return self._data.get("joint_committee_id")
    @joint_committee_id.setter
    def joint_committee_id(self, value: str):
        """Set joint_committee_id"""
        self._data["joint_committee_id"] = value

    @property
    def joint_committee_name(self) -> str:
        """Get joint_committee_name"""
        return self._data.get("joint_committee_name")
    @joint_committee_name.setter
    def joint_committee_name(self, value: str):
        """Set joint_committee_name"""
        self._data["joint_committee_name"] = value
