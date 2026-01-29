from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CommunicationCost(BaseModel):
    """
    Strongly-typed model class for CommunicationCost
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def action_code(self) -> str:
        """Get action_code"""
        return self._data.get("action_code")
    @action_code.setter
    def action_code(self, value: str):
        """Set action_code"""
        self._data["action_code"] = value

    @property
    def action_code_full(self) -> str:
        """Get action_code_full"""
        return self._data.get("action_code_full")
    @action_code_full.setter
    def action_code_full(self, value: str):
        """Set action_code_full"""
        self._data["action_code_full"] = value

    @property
    def candidate_first_name(self) -> str:
        """Get candidate_first_name"""
        return self._data.get("candidate_first_name")
    @candidate_first_name.setter
    def candidate_first_name(self, value: str):
        """Set candidate_first_name"""
        self._data["candidate_first_name"] = value

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

    @property
    def candidate_last_name(self) -> str:
        """Get candidate_last_name"""
        return self._data.get("candidate_last_name")
    @candidate_last_name.setter
    def candidate_last_name(self, value: str):
        """Set candidate_last_name"""
        self._data["candidate_last_name"] = value

    @property
    def candidate_middle_name(self) -> str:
        """Get candidate_middle_name"""
        return self._data.get("candidate_middle_name")
    @candidate_middle_name.setter
    def candidate_middle_name(self, value: str):
        """Set candidate_middle_name"""
        self._data["candidate_middle_name"] = value

    @property
    def candidate_name(self) -> str:
        """Get candidate_name"""
        return self._data.get("candidate_name")
    @candidate_name.setter
    def candidate_name(self, value: str):
        """Set candidate_name"""
        self._data["candidate_name"] = value

    @property
    def candidate_office(self) -> str:
        """Get candidate_office"""
        return self._data.get("candidate_office")
    @candidate_office.setter
    def candidate_office(self, value: str):
        """Set candidate_office"""
        self._data["candidate_office"] = value

    @property
    def candidate_office_district(self) -> str:
        """Get candidate_office_district"""
        return self._data.get("candidate_office_district")
    @candidate_office_district.setter
    def candidate_office_district(self, value: str):
        """Set candidate_office_district"""
        self._data["candidate_office_district"] = value

    @property
    def candidate_office_full(self) -> str:
        """Get candidate_office_full"""
        return self._data.get("candidate_office_full")
    @candidate_office_full.setter
    def candidate_office_full(self, value: str):
        """Set candidate_office_full"""
        self._data["candidate_office_full"] = value

    @property
    def candidate_office_state(self) -> str:
        """Get candidate_office_state"""
        return self._data.get("candidate_office_state")
    @candidate_office_state.setter
    def candidate_office_state(self, value: str):
        """Set candidate_office_state"""
        self._data["candidate_office_state"] = value

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
    def communication_class(self) -> str:
        """Get communication_class"""
        return self._data.get("communication_class")
    @communication_class.setter
    def communication_class(self, value: str):
        """Set communication_class"""
        self._data["communication_class"] = value

    @property
    def communication_type(self) -> str:
        """Get communication_type"""
        return self._data.get("communication_type")
    @communication_type.setter
    def communication_type(self, value: str):
        """Set communication_type"""
        self._data["communication_type"] = value

    @property
    def communication_type_full(self) -> str:
        """Get communication_type_full"""
        return self._data.get("communication_type_full")
    @communication_type_full.setter
    def communication_type_full(self, value: str):
        """Set communication_type_full"""
        self._data["communication_type_full"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def form_type_code(self) -> str:
        """Get form_type_code"""
        return self._data.get("form_type_code")
    @form_type_code.setter
    def form_type_code(self, value: str):
        """Set form_type_code"""
        self._data["form_type_code"] = value

    @property
    def image_number(self) -> str:
        """Get image_number"""
        return self._data.get("image_number")
    @image_number.setter
    def image_number(self, value: str):
        """Set image_number"""
        self._data["image_number"] = value

    @property
    def original_sub_id(self) -> int:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: int):
        """Set original_sub_id"""
        self._data["original_sub_id"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def primary_general_indicator(self) -> str:
        """Get primary_general_indicator"""
        return self._data.get("primary_general_indicator")
    @primary_general_indicator.setter
    def primary_general_indicator(self, value: str):
        """Set primary_general_indicator"""
        self._data["primary_general_indicator"] = value

    @property
    def primary_general_indicator_description(self) -> str:
        """Get primary_general_indicator_description"""
        return self._data.get("primary_general_indicator_description")
    @primary_general_indicator_description.setter
    def primary_general_indicator_description(self, value: str):
        """Set primary_general_indicator_description"""
        self._data["primary_general_indicator_description"] = value

    @property
    def purpose(self) -> str:
        """Get purpose"""
        return self._data.get("purpose")
    @purpose.setter
    def purpose(self, value: str):
        """Set purpose"""
        self._data["purpose"] = value

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
    def schedule_type(self) -> str:
        """Get schedule_type"""
        return self._data.get("schedule_type")
    @schedule_type.setter
    def schedule_type(self, value: str):
        """Set schedule_type"""
        self._data["schedule_type"] = value

    @property
    def schedule_type_full(self) -> str:
        """Get schedule_type_full"""
        return self._data.get("schedule_type_full")
    @schedule_type_full.setter
    def schedule_type_full(self, value: str):
        """Set schedule_type_full"""
        self._data["schedule_type_full"] = value

    @property
    def state_full(self) -> str:
        """Get state_full"""
        return self._data.get("state_full")
    @state_full.setter
    def state_full(self, value: str):
        """Set state_full"""
        self._data["state_full"] = value

    @property
    def sub_id(self) -> int:
        """Get sub_id"""
        return self._data.get("sub_id")
    @sub_id.setter
    def sub_id(self, value: int):
        """Set sub_id"""
        self._data["sub_id"] = value

    @property
    def support_oppose_indicator(self) -> str:
        """Get support_oppose_indicator"""
        return self._data.get("support_oppose_indicator")
    @support_oppose_indicator.setter
    def support_oppose_indicator(self, value: str):
        """Set support_oppose_indicator"""
        self._data["support_oppose_indicator"] = value

    @property
    def tran_id(self) -> str:
        """Get tran_id"""
        return self._data.get("tran_id")
    @tran_id.setter
    def tran_id(self, value: str):
        """Set tran_id"""
        self._data["tran_id"] = value

    @property
    def transaction_amount(self) -> float:
        """Get transaction_amount"""
        return self._data.get("transaction_amount")
    @transaction_amount.setter
    def transaction_amount(self, value: float):
        """Set transaction_amount"""
        self._data["transaction_amount"] = value

    @property
    def transaction_date(self) -> str:
        """Get transaction_date"""
        return self._data.get("transaction_date")
    @transaction_date.setter
    def transaction_date(self, value: str):
        """Set transaction_date"""
        self._data["transaction_date"] = value

    @property
    def transaction_type(self) -> str:
        """Get transaction_type"""
        return self._data.get("transaction_type")
    @transaction_type.setter
    def transaction_type(self, value: str):
        """Set transaction_type"""
        self._data["transaction_type"] = value
