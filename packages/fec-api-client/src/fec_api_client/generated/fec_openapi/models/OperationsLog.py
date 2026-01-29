from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class OperationsLog(BaseModel):
    """
    Strongly-typed model class for OperationsLog
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def amendment_indicator(self) -> str:
        """Get amendment_indicator"""
        return self._data.get("amendment_indicator")
    @amendment_indicator.setter
    def amendment_indicator(self, value: str):
        """Set amendment_indicator"""
        self._data["amendment_indicator"] = value

    @property
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

    @property
    def candidate_committee_id(self) -> str:
        """Get candidate_committee_id"""
        return self._data.get("candidate_committee_id")
    @candidate_committee_id.setter
    def candidate_committee_id(self, value: str):
        """Set candidate_committee_id"""
        self._data["candidate_committee_id"] = value

    @property
    def coverage_end_date(self) -> str:
        """Get coverage_end_date"""
        return self._data.get("coverage_end_date")
    @coverage_end_date.setter
    def coverage_end_date(self, value: str):
        """Set coverage_end_date"""
        self._data["coverage_end_date"] = value

    @property
    def coverage_start_date(self) -> str:
        """Get coverage_start_date"""
        return self._data.get("coverage_start_date")
    @coverage_start_date.setter
    def coverage_start_date(self, value: str):
        """Set coverage_start_date"""
        self._data["coverage_start_date"] = value

    @property
    def ending_image_number(self) -> str:
        """Get ending_image_number"""
        return self._data.get("ending_image_number")
    @ending_image_number.setter
    def ending_image_number(self, value: str):
        """Set ending_image_number"""
        self._data["ending_image_number"] = value

    @property
    def form_type(self) -> str:
        """Get form_type"""
        return self._data.get("form_type")
    @form_type.setter
    def form_type(self, value: str):
        """Set form_type"""
        self._data["form_type"] = value

    @property
    def receipt_date(self) -> str:
        """Get receipt_date"""
        return self._data.get("receipt_date")
    @receipt_date.setter
    def receipt_date(self, value: str):
        """Set receipt_date"""
        self._data["receipt_date"] = value

    @property
    def report_type(self) -> str:
        """Get report_type"""
        return self._data.get("report_type")
    @report_type.setter
    def report_type(self, value: str):
        """Set report_type"""
        self._data["report_type"] = value

    @property
    def report_year(self) -> int:
        """Get report_year"""
        return self._data.get("report_year")
    @report_year.setter
    def report_year(self, value: int):
        """Set report_year"""
        self._data["report_year"] = value

    @property
    def status_num(self) -> int:
        """Get status_num"""
        return self._data.get("status_num")
    @status_num.setter
    def status_num(self, value: int):
        """Set status_num"""
        self._data["status_num"] = value

    @property
    def sub_id(self) -> int:
        """Get sub_id"""
        return self._data.get("sub_id")
    @sub_id.setter
    def sub_id(self, value: int):
        """Set sub_id"""
        self._data["sub_id"] = value

    @property
    def summary_data_complete_date(self) -> str:
        """Get summary_data_complete_date"""
        return self._data.get("summary_data_complete_date")
    @summary_data_complete_date.setter
    def summary_data_complete_date(self, value: str):
        """Set summary_data_complete_date"""
        self._data["summary_data_complete_date"] = value

    @property
    def summary_data_verification_date(self) -> str:
        """Get summary_data_verification_date"""
        return self._data.get("summary_data_verification_date")
    @summary_data_verification_date.setter
    def summary_data_verification_date(self, value: str):
        """Set summary_data_verification_date"""
        self._data["summary_data_verification_date"] = value

    @property
    def transaction_data_complete_date(self) -> str:
        """Get transaction_data_complete_date"""
        return self._data.get("transaction_data_complete_date")
    @transaction_data_complete_date.setter
    def transaction_data_complete_date(self, value: str):
        """Set transaction_data_complete_date"""
        self._data["transaction_data_complete_date"] = value
