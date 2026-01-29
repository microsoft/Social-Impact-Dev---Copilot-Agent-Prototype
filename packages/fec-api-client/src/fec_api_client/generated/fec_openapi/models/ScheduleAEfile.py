from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory
    from .EFilings import EFilings

from ..base.base_model import BaseModel


class ScheduleAEfile(BaseModel):
    """
    Strongly-typed model class for ScheduleAEfile
    
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
    def contribution_receipt_amount(self) -> float:
        """Get contribution_receipt_amount"""
        return self._data.get("contribution_receipt_amount")
    @contribution_receipt_amount.setter
    def contribution_receipt_amount(self, value: float):
        """Set contribution_receipt_amount"""
        self._data["contribution_receipt_amount"] = value

    @property
    def contribution_receipt_date(self) -> str:
        """Get contribution_receipt_date"""
        return self._data.get("contribution_receipt_date")
    @contribution_receipt_date.setter
    def contribution_receipt_date(self, value: str):
        """Set contribution_receipt_date"""
        self._data["contribution_receipt_date"] = value

    @property
    def contributor_aggregate_ytd(self) -> float:
        """Get contributor_aggregate_ytd"""
        return self._data.get("contributor_aggregate_ytd")
    @contributor_aggregate_ytd.setter
    def contributor_aggregate_ytd(self, value: float):
        """Set contributor_aggregate_ytd"""
        self._data["contributor_aggregate_ytd"] = value

    @property
    def contributor_city(self) -> str:
        """Get contributor_city"""
        return self._data.get("contributor_city")
    @contributor_city.setter
    def contributor_city(self, value: str):
        """Set contributor_city"""
        self._data["contributor_city"] = value

    @property
    def contributor_employer(self) -> str:
        """Get contributor_employer"""
        return self._data.get("contributor_employer")
    @contributor_employer.setter
    def contributor_employer(self, value: str):
        """Set contributor_employer"""
        self._data["contributor_employer"] = value

    @property
    def contributor_first_name(self) -> str:
        """Get contributor_first_name"""
        return self._data.get("contributor_first_name")
    @contributor_first_name.setter
    def contributor_first_name(self, value: str):
        """Set contributor_first_name"""
        self._data["contributor_first_name"] = value

    @property
    def contributor_last_name(self) -> str:
        """Get contributor_last_name"""
        return self._data.get("contributor_last_name")
    @contributor_last_name.setter
    def contributor_last_name(self, value: str):
        """Set contributor_last_name"""
        self._data["contributor_last_name"] = value

    @property
    def contributor_middle_name(self) -> str:
        """Get contributor_middle_name"""
        return self._data.get("contributor_middle_name")
    @contributor_middle_name.setter
    def contributor_middle_name(self, value: str):
        """Set contributor_middle_name"""
        self._data["contributor_middle_name"] = value

    @property
    def contributor_name(self) -> str:
        """Get contributor_name"""
        return self._data.get("contributor_name")
    @contributor_name.setter
    def contributor_name(self, value: str):
        """Set contributor_name"""
        self._data["contributor_name"] = value

    @property
    def contributor_occupation(self) -> str:
        """Get contributor_occupation"""
        return self._data.get("contributor_occupation")
    @contributor_occupation.setter
    def contributor_occupation(self, value: str):
        """Set contributor_occupation"""
        self._data["contributor_occupation"] = value

    @property
    def contributor_prefix(self) -> str:
        """Get contributor_prefix"""
        return self._data.get("contributor_prefix")
    @contributor_prefix.setter
    def contributor_prefix(self, value: str):
        """Set contributor_prefix"""
        self._data["contributor_prefix"] = value

    @property
    def contributor_state(self) -> str:
        """Get contributor_state"""
        return self._data.get("contributor_state")
    @contributor_state.setter
    def contributor_state(self, value: str):
        """Set contributor_state"""
        self._data["contributor_state"] = value

    @property
    def contributor_suffix(self) -> str:
        """Get contributor_suffix"""
        return self._data.get("contributor_suffix")
    @contributor_suffix.setter
    def contributor_suffix(self, value: str):
        """Set contributor_suffix"""
        self._data["contributor_suffix"] = value

    @property
    def contributor_zip(self) -> str:
        """Get contributor_zip"""
        return self._data.get("contributor_zip")
    @contributor_zip.setter
    def contributor_zip(self, value: str):
        """Set contributor_zip"""
        self._data["contributor_zip"] = value

    @property
    def csv_url(self) -> str:
        """Get csv_url"""
        return self._data.get("csv_url")
    @csv_url.setter
    def csv_url(self, value: str):
        """Set csv_url"""
        self._data["csv_url"] = value

    @property
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def entity_type(self) -> str:
        """Get entity_type"""
        return self._data.get("entity_type")
    @entity_type.setter
    def entity_type(self, value: str):
        """Set entity_type"""
        self._data["entity_type"] = value

    @property
    def fec_election_type_desc(self) -> str:
        """Get fec_election_type_desc"""
        return self._data.get("fec_election_type_desc")
    @fec_election_type_desc.setter
    def fec_election_type_desc(self, value: str):
        """Set fec_election_type_desc"""
        self._data["fec_election_type_desc"] = value

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
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def pgo(self) -> str:
        """Get pgo"""
        return self._data.get("pgo")
    @pgo.setter
    def pgo(self, value: str):
        """Set pgo"""
        self._data["pgo"] = value

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
