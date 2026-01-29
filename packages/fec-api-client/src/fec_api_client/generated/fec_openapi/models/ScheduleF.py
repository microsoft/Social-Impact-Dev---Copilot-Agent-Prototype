from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory

from ..base.base_model import BaseModel


class ScheduleF(BaseModel):
    """
    Strongly-typed model class for ScheduleF
    
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
    def aggregate_general_election_expenditure(self) -> str:
        """Get aggregate_general_election_expenditure"""
        return self._data.get("aggregate_general_election_expenditure")
    @aggregate_general_election_expenditure.setter
    def aggregate_general_election_expenditure(self, value: str):
        """Set aggregate_general_election_expenditure"""
        self._data["aggregate_general_election_expenditure"] = value

    @property
    def back_reference_schedule_name(self) -> str:
        """Get back_reference_schedule_name"""
        return self._data.get("back_reference_schedule_name")
    @back_reference_schedule_name.setter
    def back_reference_schedule_name(self, value: str):
        """Set back_reference_schedule_name"""
        self._data["back_reference_schedule_name"] = value

    @property
    def back_reference_transaction_id(self) -> str:
        """Get back_reference_transaction_id"""
        return self._data.get("back_reference_transaction_id")
    @back_reference_transaction_id.setter
    def back_reference_transaction_id(self, value: str):
        """Set back_reference_transaction_id"""
        self._data["back_reference_transaction_id"] = value

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
    def catolog_code(self) -> str:
        """Get catolog_code"""
        return self._data.get("catolog_code")
    @catolog_code.setter
    def catolog_code(self, value: str):
        """Set catolog_code"""
        self._data["catolog_code"] = value

    @property
    def catolog_code_full(self) -> str:
        """Get catolog_code_full"""
        return self._data.get("catolog_code_full")
    @catolog_code_full.setter
    def catolog_code_full(self, value: str):
        """Set catolog_code_full"""
        self._data["catolog_code_full"] = value

    @property
    def committee(self) -> 'CommitteeHistory':
        """Get committee"""
        return self._data.get("committee")
    @committee.setter
    def committee(self, value: 'CommitteeHistory'):
        """Set committee"""
        self._data["committee"] = value

    @property
    def committee_designated_coordinated_expenditure_indicator(self) -> str:
        """Get committee_designated_coordinated_expenditure_indicator"""
        return self._data.get("committee_designated_coordinated_expenditure_indicator")
    @committee_designated_coordinated_expenditure_indicator.setter
    def committee_designated_coordinated_expenditure_indicator(self, value: str):
        """Set committee_designated_coordinated_expenditure_indicator"""
        self._data["committee_designated_coordinated_expenditure_indicator"] = value

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
    def conduit_committee_city(self) -> str:
        """Get conduit_committee_city"""
        return self._data.get("conduit_committee_city")
    @conduit_committee_city.setter
    def conduit_committee_city(self, value: str):
        """Set conduit_committee_city"""
        self._data["conduit_committee_city"] = value

    @property
    def conduit_committee_id(self) -> str:
        """Get conduit_committee_id"""
        return self._data.get("conduit_committee_id")
    @conduit_committee_id.setter
    def conduit_committee_id(self, value: str):
        """Set conduit_committee_id"""
        self._data["conduit_committee_id"] = value

    @property
    def conduit_committee_name(self) -> str:
        """Get conduit_committee_name"""
        return self._data.get("conduit_committee_name")
    @conduit_committee_name.setter
    def conduit_committee_name(self, value: str):
        """Set conduit_committee_name"""
        self._data["conduit_committee_name"] = value

    @property
    def conduit_committee_state(self) -> str:
        """Get conduit_committee_state"""
        return self._data.get("conduit_committee_state")
    @conduit_committee_state.setter
    def conduit_committee_state(self, value: str):
        """Set conduit_committee_state"""
        self._data["conduit_committee_state"] = value

    @property
    def conduit_committee_street1(self) -> str:
        """Get conduit_committee_street1"""
        return self._data.get("conduit_committee_street1")
    @conduit_committee_street1.setter
    def conduit_committee_street1(self, value: str):
        """Set conduit_committee_street1"""
        self._data["conduit_committee_street1"] = value

    @property
    def conduit_committee_street2(self) -> str:
        """Get conduit_committee_street2"""
        return self._data.get("conduit_committee_street2")
    @conduit_committee_street2.setter
    def conduit_committee_street2(self, value: str):
        """Set conduit_committee_street2"""
        self._data["conduit_committee_street2"] = value

    @property
    def conduit_committee_zip(self) -> str:
        """Get conduit_committee_zip"""
        return self._data.get("conduit_committee_zip")
    @conduit_committee_zip.setter
    def conduit_committee_zip(self, value: str):
        """Set conduit_committee_zip"""
        self._data["conduit_committee_zip"] = value

    @property
    def designated_committee_id(self) -> str:
        """Get designated_committee_id"""
        return self._data.get("designated_committee_id")
    @designated_committee_id.setter
    def designated_committee_id(self, value: str):
        """Set designated_committee_id"""
        self._data["designated_committee_id"] = value

    @property
    def designated_committee_name(self) -> str:
        """Get designated_committee_name"""
        return self._data.get("designated_committee_name")
    @designated_committee_name.setter
    def designated_committee_name(self, value: str):
        """Set designated_committee_name"""
        self._data["designated_committee_name"] = value

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
    def entity_type_desc(self) -> str:
        """Get entity_type_desc"""
        return self._data.get("entity_type_desc")
    @entity_type_desc.setter
    def entity_type_desc(self, value: str):
        """Set entity_type_desc"""
        self._data["entity_type_desc"] = value

    @property
    def expenditure_amount(self) -> int:
        """Get expenditure_amount"""
        return self._data.get("expenditure_amount")
    @expenditure_amount.setter
    def expenditure_amount(self, value: int):
        """Set expenditure_amount"""
        self._data["expenditure_amount"] = value

    @property
    def expenditure_date(self) -> str:
        """Get expenditure_date"""
        return self._data.get("expenditure_date")
    @expenditure_date.setter
    def expenditure_date(self, value: str):
        """Set expenditure_date"""
        self._data["expenditure_date"] = value

    @property
    def expenditure_purpose_full(self) -> str:
        """Get expenditure_purpose_full"""
        return self._data.get("expenditure_purpose_full")
    @expenditure_purpose_full.setter
    def expenditure_purpose_full(self, value: str):
        """Set expenditure_purpose_full"""
        self._data["expenditure_purpose_full"] = value

    @property
    def expenditure_type(self) -> str:
        """Get expenditure_type"""
        return self._data.get("expenditure_type")
    @expenditure_type.setter
    def expenditure_type(self, value: str):
        """Set expenditure_type"""
        self._data["expenditure_type"] = value

    @property
    def expenditure_type_full(self) -> str:
        """Get expenditure_type_full"""
        return self._data.get("expenditure_type_full")
    @expenditure_type_full.setter
    def expenditure_type_full(self, value: str):
        """Set expenditure_type_full"""
        self._data["expenditure_type_full"] = value

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
    def load_date(self) -> str:
        """Get load_date"""
        return self._data.get("load_date")
    @load_date.setter
    def load_date(self, value: str):
        """Set load_date"""
        self._data["load_date"] = value

    @property
    def memo_code(self) -> str:
        """Get memo_code"""
        return self._data.get("memo_code")
    @memo_code.setter
    def memo_code(self, value: str):
        """Set memo_code"""
        self._data["memo_code"] = value

    @property
    def memo_code_full(self) -> str:
        """Get memo_code_full"""
        return self._data.get("memo_code_full")
    @memo_code_full.setter
    def memo_code_full(self, value: str):
        """Set memo_code_full"""
        self._data["memo_code_full"] = value

    @property
    def memo_text(self) -> str:
        """Get memo_text"""
        return self._data.get("memo_text")
    @memo_text.setter
    def memo_text(self, value: str):
        """Set memo_text"""
        self._data["memo_text"] = value

    @property
    def original_sub_id(self) -> int:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: int):
        """Set original_sub_id"""
        self._data["original_sub_id"] = value

    @property
    def payee_first_name(self) -> str:
        """Get payee_first_name"""
        return self._data.get("payee_first_name")
    @payee_first_name.setter
    def payee_first_name(self, value: str):
        """Set payee_first_name"""
        self._data["payee_first_name"] = value

    @property
    def payee_last_name(self) -> str:
        """Get payee_last_name"""
        return self._data.get("payee_last_name")
    @payee_last_name.setter
    def payee_last_name(self, value: str):
        """Set payee_last_name"""
        self._data["payee_last_name"] = value

    @property
    def payee_middle_name(self) -> str:
        """Get payee_middle_name"""
        return self._data.get("payee_middle_name")
    @payee_middle_name.setter
    def payee_middle_name(self, value: str):
        """Set payee_middle_name"""
        self._data["payee_middle_name"] = value

    @property
    def payee_name(self) -> str:
        """Get payee_name"""
        return self._data.get("payee_name")
    @payee_name.setter
    def payee_name(self, value: str):
        """Set payee_name"""
        self._data["payee_name"] = value

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
    def report_year(self) -> float:
        """Get report_year"""
        return self._data.get("report_year")
    @report_year.setter
    def report_year(self, value: float):
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
    def subordinate_committee(self) -> 'CommitteeHistory':
        """Get subordinate_committee"""
        return self._data.get("subordinate_committee")
    @subordinate_committee.setter
    def subordinate_committee(self, value: 'CommitteeHistory'):
        """Set subordinate_committee"""
        self._data["subordinate_committee"] = value

    @property
    def subordinate_committee_id(self) -> str:
        """Get subordinate_committee_id"""
        return self._data.get("subordinate_committee_id")
    @subordinate_committee_id.setter
    def subordinate_committee_id(self, value: str):
        """Set subordinate_committee_id"""
        self._data["subordinate_committee_id"] = value

    @property
    def transaction_id(self) -> str:
        """Get transaction_id"""
        return self._data.get("transaction_id")
    @transaction_id.setter
    def transaction_id(self, value: str):
        """Set transaction_id"""
        self._data["transaction_id"] = value

    @property
    def unlimited_spending_flag(self) -> str:
        """Get unlimited_spending_flag"""
        return self._data.get("unlimited_spending_flag")
    @unlimited_spending_flag.setter
    def unlimited_spending_flag(self, value: str):
        """Set unlimited_spending_flag"""
        self._data["unlimited_spending_flag"] = value

    @property
    def unlimited_spending_flag_full(self) -> str:
        """Get unlimited_spending_flag_full"""
        return self._data.get("unlimited_spending_flag_full")
    @unlimited_spending_flag_full.setter
    def unlimited_spending_flag_full(self, value: str):
        """Set unlimited_spending_flag_full"""
        self._data["unlimited_spending_flag_full"] = value
