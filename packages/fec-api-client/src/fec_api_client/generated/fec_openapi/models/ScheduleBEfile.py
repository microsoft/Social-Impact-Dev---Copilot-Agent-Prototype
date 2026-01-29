from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory
    from .EFilings import EFilings

from ..base.base_model import BaseModel


class ScheduleBEfile(BaseModel):
    """
    Strongly-typed model class for ScheduleBEfile
    
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
    def beneficiary_committee_name(self) -> str:
        """Get beneficiary_committee_name"""
        return self._data.get("beneficiary_committee_name")
    @beneficiary_committee_name.setter
    def beneficiary_committee_name(self, value: str):
        """Set beneficiary_committee_name"""
        self._data["beneficiary_committee_name"] = value

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
    def disbursement_amount(self) -> float:
        """Get disbursement_amount"""
        return self._data.get("disbursement_amount")
    @disbursement_amount.setter
    def disbursement_amount(self, value: float):
        """Set disbursement_amount"""
        self._data["disbursement_amount"] = value

    @property
    def disbursement_date(self) -> str:
        """Get disbursement_date"""
        return self._data.get("disbursement_date")
    @disbursement_date.setter
    def disbursement_date(self, value: str):
        """Set disbursement_date"""
        self._data["disbursement_date"] = value

    @property
    def disbursement_description(self) -> str:
        """Get disbursement_description"""
        return self._data.get("disbursement_description")
    @disbursement_description.setter
    def disbursement_description(self, value: str):
        """Set disbursement_description"""
        self._data["disbursement_description"] = value

    @property
    def disbursement_type(self) -> str:
        """Get disbursement_type"""
        return self._data.get("disbursement_type")
    @disbursement_type.setter
    def disbursement_type(self, value: str):
        """Set disbursement_type"""
        self._data["disbursement_type"] = value

    @property
    def entity_type(self) -> str:
        """Get entity_type"""
        return self._data.get("entity_type")
    @entity_type.setter
    def entity_type(self, value: str):
        """Set entity_type"""
        self._data["entity_type"] = value

    @property
    def fec_url(self) -> str:
        """Get fec_url"""
        return self._data.get("fec_url")
    @fec_url.setter
    def fec_url(self, value: str):
        """Set fec_url"""
        self._data["fec_url"] = value

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
    def line_number(self) -> str:
        """Get line_number"""
        return self._data.get("line_number")
    @line_number.setter
    def line_number(self, value: str):
        """Set line_number"""
        self._data["line_number"] = value

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
    def recipient_city(self) -> str:
        """Get recipient_city"""
        return self._data.get("recipient_city")
    @recipient_city.setter
    def recipient_city(self, value: str):
        """Set recipient_city"""
        self._data["recipient_city"] = value

    @property
    def recipient_name(self) -> str:
        """Get recipient_name"""
        return self._data.get("recipient_name")
    @recipient_name.setter
    def recipient_name(self, value: str):
        """Set recipient_name"""
        self._data["recipient_name"] = value

    @property
    def recipient_prefix(self) -> str:
        """Get recipient_prefix"""
        return self._data.get("recipient_prefix")
    @recipient_prefix.setter
    def recipient_prefix(self, value: str):
        """Set recipient_prefix"""
        self._data["recipient_prefix"] = value

    @property
    def recipient_state(self) -> str:
        """Get recipient_state"""
        return self._data.get("recipient_state")
    @recipient_state.setter
    def recipient_state(self, value: str):
        """Set recipient_state"""
        self._data["recipient_state"] = value

    @property
    def recipient_suffix(self) -> str:
        """Get recipient_suffix"""
        return self._data.get("recipient_suffix")
    @recipient_suffix.setter
    def recipient_suffix(self, value: str):
        """Set recipient_suffix"""
        self._data["recipient_suffix"] = value

    @property
    def recipient_zip(self) -> str:
        """Get recipient_zip"""
        return self._data.get("recipient_zip")
    @recipient_zip.setter
    def recipient_zip(self, value: str):
        """Set recipient_zip"""
        self._data["recipient_zip"] = value

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
    def semi_annual_bundled_refund(self) -> int:
        """Get semi_annual_bundled_refund"""
        return self._data.get("semi_annual_bundled_refund")
    @semi_annual_bundled_refund.setter
    def semi_annual_bundled_refund(self, value: int):
        """Set semi_annual_bundled_refund"""
        self._data["semi_annual_bundled_refund"] = value

    @property
    def transaction_id(self) -> str:
        """Get transaction_id"""
        return self._data.get("transaction_id")
    @transaction_id.setter
    def transaction_id(self, value: str):
        """Set transaction_id"""
        self._data["transaction_id"] = value
