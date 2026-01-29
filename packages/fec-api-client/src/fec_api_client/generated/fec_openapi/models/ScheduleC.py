from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory

from ..base.base_model import BaseModel


class ScheduleC(BaseModel):
    """
    Strongly-typed model class for ScheduleC
    
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
    def candidate_office_state_full(self) -> str:
        """Get candidate_office_state_full"""
        return self._data.get("candidate_office_state_full")
    @candidate_office_state_full.setter
    def candidate_office_state_full(self, value: str):
        """Set candidate_office_state_full"""
        self._data["candidate_office_state_full"] = value

    @property
    def candidate_prefix(self) -> str:
        """Get candidate_prefix"""
        return self._data.get("candidate_prefix")
    @candidate_prefix.setter
    def candidate_prefix(self, value: str):
        """Set candidate_prefix"""
        self._data["candidate_prefix"] = value

    @property
    def candidate_suffix(self) -> str:
        """Get candidate_suffix"""
        return self._data.get("candidate_suffix")
    @candidate_suffix.setter
    def candidate_suffix(self, value: str):
        """Set candidate_suffix"""
        self._data["candidate_suffix"] = value

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
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def due_date_terms(self) -> str:
        """Get due_date_terms"""
        return self._data.get("due_date_terms")
    @due_date_terms.setter
    def due_date_terms(self, value: str):
        """Set due_date_terms"""
        self._data["due_date_terms"] = value

    @property
    def election_type(self) -> str:
        """Get election_type"""
        return self._data.get("election_type")
    @election_type.setter
    def election_type(self, value: str):
        """Set election_type"""
        self._data["election_type"] = value

    @property
    def election_type_full(self) -> str:
        """Get election_type_full"""
        return self._data.get("election_type_full")
    @election_type_full.setter
    def election_type_full(self, value: str):
        """Set election_type_full"""
        self._data["election_type_full"] = value

    @property
    def entity_type(self) -> str:
        """Get entity_type"""
        return self._data.get("entity_type")
    @entity_type.setter
    def entity_type(self, value: str):
        """Set entity_type"""
        self._data["entity_type"] = value

    @property
    def entity_type_full(self) -> str:
        """Get entity_type_full"""
        return self._data.get("entity_type_full")
    @entity_type_full.setter
    def entity_type_full(self, value: str):
        """Set entity_type_full"""
        self._data["entity_type_full"] = value

    @property
    def fec_committee_id(self) -> str:
        """Get fec_committee_id"""
        return self._data.get("fec_committee_id")
    @fec_committee_id.setter
    def fec_committee_id(self, value: str):
        """Set fec_committee_id"""
        self._data["fec_committee_id"] = value

    @property
    def fec_election_type_full(self) -> str:
        """Get fec_election_type_full"""
        return self._data.get("fec_election_type_full")
    @fec_election_type_full.setter
    def fec_election_type_full(self, value: str):
        """Set fec_election_type_full"""
        self._data["fec_election_type_full"] = value

    @property
    def fec_election_type_year(self) -> str:
        """Get fec_election_type_year"""
        return self._data.get("fec_election_type_year")
    @fec_election_type_year.setter
    def fec_election_type_year(self, value: str):
        """Set fec_election_type_year"""
        self._data["fec_election_type_year"] = value

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
    def incurred_date(self) -> str:
        """Get incurred_date"""
        return self._data.get("incurred_date")
    @incurred_date.setter
    def incurred_date(self, value: str):
        """Set incurred_date"""
        self._data["incurred_date"] = value

    @property
    def interest_rate_terms(self) -> str:
        """Get interest_rate_terms"""
        return self._data.get("interest_rate_terms")
    @interest_rate_terms.setter
    def interest_rate_terms(self, value: str):
        """Set interest_rate_terms"""
        self._data["interest_rate_terms"] = value

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
    def load_date(self) -> str:
        """Get load_date"""
        return self._data.get("load_date")
    @load_date.setter
    def load_date(self, value: str):
        """Set load_date"""
        self._data["load_date"] = value

    @property
    def loan_balance(self) -> float:
        """Get loan_balance"""
        return self._data.get("loan_balance")
    @loan_balance.setter
    def loan_balance(self, value: float):
        """Set loan_balance"""
        self._data["loan_balance"] = value

    @property
    def loan_source_city(self) -> str:
        """Get loan_source_city"""
        return self._data.get("loan_source_city")
    @loan_source_city.setter
    def loan_source_city(self, value: str):
        """Set loan_source_city"""
        self._data["loan_source_city"] = value

    @property
    def loan_source_first_name(self) -> str:
        """Get loan_source_first_name"""
        return self._data.get("loan_source_first_name")
    @loan_source_first_name.setter
    def loan_source_first_name(self, value: str):
        """Set loan_source_first_name"""
        self._data["loan_source_first_name"] = value

    @property
    def loan_source_last_name(self) -> str:
        """Get loan_source_last_name"""
        return self._data.get("loan_source_last_name")
    @loan_source_last_name.setter
    def loan_source_last_name(self, value: str):
        """Set loan_source_last_name"""
        self._data["loan_source_last_name"] = value

    @property
    def loan_source_middle_name(self) -> str:
        """Get loan_source_middle_name"""
        return self._data.get("loan_source_middle_name")
    @loan_source_middle_name.setter
    def loan_source_middle_name(self, value: str):
        """Set loan_source_middle_name"""
        self._data["loan_source_middle_name"] = value

    @property
    def loan_source_name(self) -> str:
        """Get loan_source_name"""
        return self._data.get("loan_source_name")
    @loan_source_name.setter
    def loan_source_name(self, value: str):
        """Set loan_source_name"""
        self._data["loan_source_name"] = value

    @property
    def loan_source_prefix(self) -> str:
        """Get loan_source_prefix"""
        return self._data.get("loan_source_prefix")
    @loan_source_prefix.setter
    def loan_source_prefix(self, value: str):
        """Set loan_source_prefix"""
        self._data["loan_source_prefix"] = value

    @property
    def loan_source_state(self) -> str:
        """Get loan_source_state"""
        return self._data.get("loan_source_state")
    @loan_source_state.setter
    def loan_source_state(self, value: str):
        """Set loan_source_state"""
        self._data["loan_source_state"] = value

    @property
    def loan_source_street_1(self) -> str:
        """Get loan_source_street_1"""
        return self._data.get("loan_source_street_1")
    @loan_source_street_1.setter
    def loan_source_street_1(self, value: str):
        """Set loan_source_street_1"""
        self._data["loan_source_street_1"] = value

    @property
    def loan_source_street_2(self) -> str:
        """Get loan_source_street_2"""
        return self._data.get("loan_source_street_2")
    @loan_source_street_2.setter
    def loan_source_street_2(self, value: str):
        """Set loan_source_street_2"""
        self._data["loan_source_street_2"] = value

    @property
    def loan_source_suffix(self) -> str:
        """Get loan_source_suffix"""
        return self._data.get("loan_source_suffix")
    @loan_source_suffix.setter
    def loan_source_suffix(self, value: str):
        """Set loan_source_suffix"""
        self._data["loan_source_suffix"] = value

    @property
    def loan_source_zip(self) -> str:
        """Get loan_source_zip"""
        return self._data.get("loan_source_zip")
    @loan_source_zip.setter
    def loan_source_zip(self, value: str):
        """Set loan_source_zip"""
        self._data["loan_source_zip"] = value

    @property
    def memo_code(self) -> str:
        """Get memo_code"""
        return self._data.get("memo_code")
    @memo_code.setter
    def memo_code(self, value: str):
        """Set memo_code"""
        self._data["memo_code"] = value

    @property
    def memo_text(self) -> str:
        """Get memo_text"""
        return self._data.get("memo_text")
    @memo_text.setter
    def memo_text(self, value: str):
        """Set memo_text"""
        self._data["memo_text"] = value

    @property
    def original_loan_amount(self) -> float:
        """Get original_loan_amount"""
        return self._data.get("original_loan_amount")
    @original_loan_amount.setter
    def original_loan_amount(self, value: float):
        """Set original_loan_amount"""
        self._data["original_loan_amount"] = value

    @property
    def original_sub_id(self) -> int:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: int):
        """Set original_sub_id"""
        self._data["original_sub_id"] = value

    @property
    def payment_to_date(self) -> float:
        """Get payment_to_date"""
        return self._data.get("payment_to_date")
    @payment_to_date.setter
    def payment_to_date(self, value: float):
        """Set payment_to_date"""
        self._data["payment_to_date"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def personally_funded(self) -> str:
        """Get personally_funded"""
        return self._data.get("personally_funded")
    @personally_funded.setter
    def personally_funded(self, value: str):
        """Set personally_funded"""
        self._data["personally_funded"] = value

    @property
    def report_type(self) -> str:
        """Get report_type"""
        return self._data.get("report_type")
    @report_type.setter
    def report_type(self, value: str):
        """Set report_type"""
        self._data["report_type"] = value

    @property
    def report_year(self) -> float:
        """Get report_year"""
        return self._data.get("report_year")
    @report_year.setter
    def report_year(self, value: float):
        """Set report_year"""
        self._data["report_year"] = value

    @property
    def schedule_a_line_number(self) -> str:
        """Get schedule_a_line_number"""
        return self._data.get("schedule_a_line_number")
    @schedule_a_line_number.setter
    def schedule_a_line_number(self, value: str):
        """Set schedule_a_line_number"""
        self._data["schedule_a_line_number"] = value

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
    def secured_ind(self) -> str:
        """Get secured_ind"""
        return self._data.get("secured_ind")
    @secured_ind.setter
    def secured_ind(self, value: str):
        """Set secured_ind"""
        self._data["secured_ind"] = value

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
