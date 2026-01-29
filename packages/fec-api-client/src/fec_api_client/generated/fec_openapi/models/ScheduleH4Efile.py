from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory
    from .EFilings import EFilings

from ..base.base_model import BaseModel


class ScheduleH4Efile(BaseModel):
    """
    Strongly-typed model class for ScheduleH4Efile
    
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
    def administrative_voter_drive_activity_indicator(self) -> str:
        """Get administrative_voter_drive_activity_indicator"""
        return self._data.get("administrative_voter_drive_activity_indicator")
    @administrative_voter_drive_activity_indicator.setter
    def administrative_voter_drive_activity_indicator(self, value: str):
        """Set administrative_voter_drive_activity_indicator"""
        self._data["administrative_voter_drive_activity_indicator"] = value

    @property
    def amendment_indicator(self) -> str:
        """Get amendment_indicator"""
        return self._data.get("amendment_indicator")
    @amendment_indicator.setter
    def amendment_indicator(self, value: str):
        """Set amendment_indicator"""
        self._data["amendment_indicator"] = value

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
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

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
    def csv_url(self) -> str:
        """Get csv_url"""
        return self._data.get("csv_url")
    @csv_url.setter
    def csv_url(self, value: str):
        """Set csv_url"""
        self._data["csv_url"] = value

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
    def entity_type(self) -> str:
        """Get entity_type"""
        return self._data.get("entity_type")
    @entity_type.setter
    def entity_type(self, value: str):
        """Set entity_type"""
        self._data["entity_type"] = value

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
    def fec_url(self) -> str:
        """Get fec_url"""
        return self._data.get("fec_url")
    @fec_url.setter
    def fec_url(self, value: str):
        """Set fec_url"""
        self._data["fec_url"] = value

    @property
    def fed_share(self) -> float:
        """Get fed_share"""
        return self._data.get("fed_share")
    @fed_share.setter
    def fed_share(self, value: float):
        """Set fed_share"""
        self._data["fed_share"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def filing(self) -> 'EFilings':
        """Get filing"""
        return self._data.get("filing")
    @filing.setter
    def filing(self, value: 'EFilings'):
        """Set filing"""
        self._data["filing"] = value

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
    def is_notice(self) -> bool:
        """Get is_notice"""
        return self._data.get("is_notice")
    @is_notice.setter
    def is_notice(self, value: bool):
        """Set is_notice"""
        self._data["is_notice"] = value

    @property
    def load_timestamp(self) -> str:
        """Get load_timestamp"""
        return self._data.get("load_timestamp")
    @load_timestamp.setter
    def load_timestamp(self, value: str):
        """Set load_timestamp"""
        self._data["load_timestamp"] = value

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
    def nonfed_share(self) -> float:
        """Get nonfed_share"""
        return self._data.get("nonfed_share")
    @nonfed_share.setter
    def nonfed_share(self, value: float):
        """Set nonfed_share"""
        self._data["nonfed_share"] = value

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
    def related_line_number(self) -> int:
        """Get related_line_number"""
        return self._data.get("related_line_number")
    @related_line_number.setter
    def related_line_number(self, value: int):
        """Set related_line_number"""
        self._data["related_line_number"] = value

    @property
    def report_type(self) -> str:
        """Get report_type"""
        return self._data.get("report_type")
    @report_type.setter
    def report_type(self, value: str):
        """Set report_type"""
        self._data["report_type"] = value

    @property
    def transaction_id(self) -> str:
        """Get transaction_id"""
        return self._data.get("transaction_id")
    @transaction_id.setter
    def transaction_id(self, value: str):
        """Set transaction_id"""
        self._data["transaction_id"] = value
