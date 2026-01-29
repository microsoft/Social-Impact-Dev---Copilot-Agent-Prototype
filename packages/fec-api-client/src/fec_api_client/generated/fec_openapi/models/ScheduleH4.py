from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory

from ..base.base_model import BaseModel


class ScheduleH4(BaseModel):
    """
    Strongly-typed model class for ScheduleH4
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def activity_or_event(self) -> str:
        """Get activity_or_event"""
        return self._data.get("activity_or_event")
    @activity_or_event.setter
    def activity_or_event(self, value: str):
        """Set activity_or_event"""
        self._data["activity_or_event"] = value

    @property
    def administrative_activity_indicator(self) -> str:
        """Get administrative_activity_indicator"""
        return self._data.get("administrative_activity_indicator")
    @administrative_activity_indicator.setter
    def administrative_activity_indicator(self, value: str):
        """Set administrative_activity_indicator"""
        self._data["administrative_activity_indicator"] = value

    @property
    def administrative_voter_drive_activity_indicator(self) -> str:
        """Get administrative_voter_drive_activity_indicator"""
        return self._data.get("administrative_voter_drive_activity_indicator")
    @administrative_voter_drive_activity_indicator.setter
    def administrative_voter_drive_activity_indicator(self, value: str):
        """Set administrative_voter_drive_activity_indicator"""
        self._data["administrative_voter_drive_activity_indicator"] = value

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
    def direct_candidate_support_activity_indicator(self) -> str:
        """Get direct_candidate_support_activity_indicator"""
        return self._data.get("direct_candidate_support_activity_indicator")
    @direct_candidate_support_activity_indicator.setter
    def direct_candidate_support_activity_indicator(self, value: str):
        """Set direct_candidate_support_activity_indicator"""
        self._data["direct_candidate_support_activity_indicator"] = value

    @property
    def disbursement_amount(self) -> float:
        """Get disbursement_amount"""
        return self._data.get("disbursement_amount")
    @disbursement_amount.setter
    def disbursement_amount(self, value: float):
        """Set disbursement_amount"""
        self._data["disbursement_amount"] = value

    @property
    def disbursement_purpose(self) -> str:
        """Get disbursement_purpose"""
        return self._data.get("disbursement_purpose")
    @disbursement_purpose.setter
    def disbursement_purpose(self, value: str):
        """Set disbursement_purpose"""
        self._data["disbursement_purpose"] = value

    @property
    def event_amount_year_to_date(self) -> float:
        """Get event_amount_year_to_date"""
        return self._data.get("event_amount_year_to_date")
    @event_amount_year_to_date.setter
    def event_amount_year_to_date(self, value: float):
        """Set event_amount_year_to_date"""
        self._data["event_amount_year_to_date"] = value

    @property
    def event_purpose_date(self) -> str:
        """Get event_purpose_date"""
        return self._data.get("event_purpose_date")
    @event_purpose_date.setter
    def event_purpose_date(self, value: str):
        """Set event_purpose_date"""
        self._data["event_purpose_date"] = value

    @property
    def exempt_activity_indicator(self) -> str:
        """Get exempt_activity_indicator"""
        return self._data.get("exempt_activity_indicator")
    @exempt_activity_indicator.setter
    def exempt_activity_indicator(self, value: str):
        """Set exempt_activity_indicator"""
        self._data["exempt_activity_indicator"] = value

    @property
    def federal_share(self) -> float:
        """Get federal_share"""
        return self._data.get("federal_share")
    @federal_share.setter
    def federal_share(self, value: float):
        """Set federal_share"""
        self._data["federal_share"] = value

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
    def fundraising_activity_indicator(self) -> str:
        """Get fundraising_activity_indicator"""
        return self._data.get("fundraising_activity_indicator")
    @fundraising_activity_indicator.setter
    def fundraising_activity_indicator(self, value: str):
        """Set fundraising_activity_indicator"""
        self._data["fundraising_activity_indicator"] = value

    @property
    def general_voter_drive_activity_indicator(self) -> str:
        """Get general_voter_drive_activity_indicator"""
        return self._data.get("general_voter_drive_activity_indicator")
    @general_voter_drive_activity_indicator.setter
    def general_voter_drive_activity_indicator(self, value: str):
        """Set general_voter_drive_activity_indicator"""
        self._data["general_voter_drive_activity_indicator"] = value

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
    def nonfederal_share(self) -> float:
        """Get nonfederal_share"""
        return self._data.get("nonfederal_share")
    @nonfederal_share.setter
    def nonfederal_share(self, value: float):
        """Set nonfederal_share"""
        self._data["nonfederal_share"] = value

    @property
    def original_sub_id(self) -> str:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: str):
        """Set original_sub_id"""
        self._data["original_sub_id"] = value

    @property
    def payee_city(self) -> str:
        """Get payee_city"""
        return self._data.get("payee_city")
    @payee_city.setter
    def payee_city(self, value: str):
        """Set payee_city"""
        self._data["payee_city"] = value

    @property
    def payee_name(self) -> str:
        """Get payee_name"""
        return self._data.get("payee_name")
    @payee_name.setter
    def payee_name(self, value: str):
        """Set payee_name"""
        self._data["payee_name"] = value

    @property
    def payee_state(self) -> str:
        """Get payee_state"""
        return self._data.get("payee_state")
    @payee_state.setter
    def payee_state(self, value: str):
        """Set payee_state"""
        self._data["payee_state"] = value

    @property
    def payee_street_1(self) -> str:
        """Get payee_street_1"""
        return self._data.get("payee_street_1")
    @payee_street_1.setter
    def payee_street_1(self, value: str):
        """Set payee_street_1"""
        self._data["payee_street_1"] = value

    @property
    def payee_street_2(self) -> str:
        """Get payee_street_2"""
        return self._data.get("payee_street_2")
    @payee_street_2.setter
    def payee_street_2(self, value: str):
        """Set payee_street_2"""
        self._data["payee_street_2"] = value

    @property
    def payee_zip(self) -> str:
        """Get payee_zip"""
        return self._data.get("payee_zip")
    @payee_zip.setter
    def payee_zip(self, value: str):
        """Set payee_zip"""
        self._data["payee_zip"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def public_comm_indicator(self) -> str:
        """Get public_comm_indicator"""
        return self._data.get("public_comm_indicator")
    @public_comm_indicator.setter
    def public_comm_indicator(self, value: str):
        """Set public_comm_indicator"""
        self._data["public_comm_indicator"] = value

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
    def spender_committee_designation(self) -> str:
        """Get spender_committee_designation"""
        return self._data.get("spender_committee_designation")
    @spender_committee_designation.setter
    def spender_committee_designation(self, value: str):
        """Set spender_committee_designation"""
        self._data["spender_committee_designation"] = value

    @property
    def spender_committee_name(self) -> str:
        """Get spender_committee_name"""
        return self._data.get("spender_committee_name")
    @spender_committee_name.setter
    def spender_committee_name(self, value: str):
        """Set spender_committee_name"""
        self._data["spender_committee_name"] = value

    @property
    def spender_committee_type(self) -> str:
        """Get spender_committee_type"""
        return self._data.get("spender_committee_type")
    @spender_committee_type.setter
    def spender_committee_type(self, value: str):
        """Set spender_committee_type"""
        self._data["spender_committee_type"] = value

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
