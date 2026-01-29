from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory

from ..base.base_model import BaseModel


class ScheduleD(BaseModel):
    """
    Strongly-typed model class for ScheduleD
    
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
    def amount_incurred_period(self) -> float:
        """Get amount_incurred_period"""
        return self._data.get("amount_incurred_period")
    @amount_incurred_period.setter
    def amount_incurred_period(self, value: float):
        """Set amount_incurred_period"""
        self._data["amount_incurred_period"] = value

    @property
    def committee(self) -> 'CommitteeHistory':
        """Get committee"""
        return self._data.get("committee")
    @committee.setter
    def committee(self, value: 'CommitteeHistory'):
        """Set committee"""
        self._data["committee"] = value

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
    def creditor_debtor_city(self) -> str:
        """Get creditor_debtor_city"""
        return self._data.get("creditor_debtor_city")
    @creditor_debtor_city.setter
    def creditor_debtor_city(self, value: str):
        """Set creditor_debtor_city"""
        self._data["creditor_debtor_city"] = value

    @property
    def creditor_debtor_first_name(self) -> str:
        """Get creditor_debtor_first_name"""
        return self._data.get("creditor_debtor_first_name")
    @creditor_debtor_first_name.setter
    def creditor_debtor_first_name(self, value: str):
        """Set creditor_debtor_first_name"""
        self._data["creditor_debtor_first_name"] = value

    @property
    def creditor_debtor_last_name(self) -> str:
        """Get creditor_debtor_last_name"""
        return self._data.get("creditor_debtor_last_name")
    @creditor_debtor_last_name.setter
    def creditor_debtor_last_name(self, value: str):
        """Set creditor_debtor_last_name"""
        self._data["creditor_debtor_last_name"] = value

    @property
    def creditor_debtor_middle_name(self) -> str:
        """Get creditor_debtor_middle_name"""
        return self._data.get("creditor_debtor_middle_name")
    @creditor_debtor_middle_name.setter
    def creditor_debtor_middle_name(self, value: str):
        """Set creditor_debtor_middle_name"""
        self._data["creditor_debtor_middle_name"] = value

    @property
    def creditor_debtor_name(self) -> str:
        """Get creditor_debtor_name"""
        return self._data.get("creditor_debtor_name")
    @creditor_debtor_name.setter
    def creditor_debtor_name(self, value: str):
        """Set creditor_debtor_name"""
        self._data["creditor_debtor_name"] = value

    @property
    def creditor_debtor_prefix(self) -> str:
        """Get creditor_debtor_prefix"""
        return self._data.get("creditor_debtor_prefix")
    @creditor_debtor_prefix.setter
    def creditor_debtor_prefix(self, value: str):
        """Set creditor_debtor_prefix"""
        self._data["creditor_debtor_prefix"] = value

    @property
    def creditor_debtor_state(self) -> str:
        """Get creditor_debtor_state"""
        return self._data.get("creditor_debtor_state")
    @creditor_debtor_state.setter
    def creditor_debtor_state(self, value: str):
        """Set creditor_debtor_state"""
        self._data["creditor_debtor_state"] = value

    @property
    def creditor_debtor_street1(self) -> str:
        """Get creditor_debtor_street1"""
        return self._data.get("creditor_debtor_street1")
    @creditor_debtor_street1.setter
    def creditor_debtor_street1(self, value: str):
        """Set creditor_debtor_street1"""
        self._data["creditor_debtor_street1"] = value

    @property
    def creditor_debtor_street2(self) -> str:
        """Get creditor_debtor_street2"""
        return self._data.get("creditor_debtor_street2")
    @creditor_debtor_street2.setter
    def creditor_debtor_street2(self, value: str):
        """Set creditor_debtor_street2"""
        self._data["creditor_debtor_street2"] = value

    @property
    def creditor_debtor_suffix(self) -> str:
        """Get creditor_debtor_suffix"""
        return self._data.get("creditor_debtor_suffix")
    @creditor_debtor_suffix.setter
    def creditor_debtor_suffix(self, value: str):
        """Set creditor_debtor_suffix"""
        self._data["creditor_debtor_suffix"] = value

    @property
    def election_cycle(self) -> int:
        """Get election_cycle"""
        return self._data.get("election_cycle")
    @election_cycle.setter
    def election_cycle(self, value: int):
        """Set election_cycle"""
        self._data["election_cycle"] = value

    @property
    def entity_type(self) -> str:
        """Get entity_type"""
        return self._data.get("entity_type")
    @entity_type.setter
    def entity_type(self, value: str):
        """Set entity_type"""
        self._data["entity_type"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def filing_form(self) -> str:
        """Get filing_form"""
        return self._data.get("filing_form")
    @filing_form.setter
    def filing_form(self, value: str):
        """Set filing_form"""
        self._data["filing_form"] = value

    @property
    def form_line_number(self) -> str:
        """Get form_line_number"""
        return self._data.get("form_line_number")
    @form_line_number.setter
    def form_line_number(self, value: str):
        """Set form_line_number"""
        self._data["form_line_number"] = value

    @property
    def image_number(self) -> str:
        """Get image_number"""
        return self._data.get("image_number")
    @image_number.setter
    def image_number(self, value: str):
        """Set image_number"""
        self._data["image_number"] = value

    @property
    def line_number(self) -> str:
        """Get line_number"""
        return self._data.get("line_number")
    @line_number.setter
    def line_number(self, value: str):
        """Set line_number"""
        self._data["line_number"] = value

    @property
    def link_id(self) -> int:
        """Get link_id"""
        return self._data.get("link_id")
    @link_id.setter
    def link_id(self, value: int):
        """Set link_id"""
        self._data["link_id"] = value

    @property
    def nature_of_debt(self) -> str:
        """Get nature_of_debt"""
        return self._data.get("nature_of_debt")
    @nature_of_debt.setter
    def nature_of_debt(self, value: str):
        """Set nature_of_debt"""
        self._data["nature_of_debt"] = value

    @property
    def original_sub_id(self) -> int:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: int):
        """Set original_sub_id"""
        self._data["original_sub_id"] = value

    @property
    def outstanding_balance_beginning_of_period(self) -> float:
        """Get outstanding_balance_beginning_of_period"""
        return self._data.get("outstanding_balance_beginning_of_period")
    @outstanding_balance_beginning_of_period.setter
    def outstanding_balance_beginning_of_period(self, value: float):
        """Set outstanding_balance_beginning_of_period"""
        self._data["outstanding_balance_beginning_of_period"] = value

    @property
    def outstanding_balance_close_of_period(self) -> float:
        """Get outstanding_balance_close_of_period"""
        return self._data.get("outstanding_balance_close_of_period")
    @outstanding_balance_close_of_period.setter
    def outstanding_balance_close_of_period(self, value: float):
        """Set outstanding_balance_close_of_period"""
        self._data["outstanding_balance_close_of_period"] = value

    @property
    def payment_period(self) -> float:
        """Get payment_period"""
        return self._data.get("payment_period")
    @payment_period.setter
    def payment_period(self, value: float):
        """Set payment_period"""
        self._data["payment_period"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

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
    def sub_id(self) -> str:
        """Get sub_id"""
        return self._data.get("sub_id")
    @sub_id.setter
    def sub_id(self, value: str):
        """Set sub_id"""
        self._data["sub_id"] = value

    @property
    def transaction_id(self) -> str:
        """Get transaction_id"""
        return self._data.get("transaction_id")
    @transaction_id.setter
    def transaction_id(self, value: str):
        """Set transaction_id"""
        self._data["transaction_id"] = value
