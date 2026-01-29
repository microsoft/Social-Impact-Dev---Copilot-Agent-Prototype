from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .CommitteeHistory import CommitteeHistory

from ..base.base_model import BaseModel


class ScheduleA(BaseModel):
    """
    Strongly-typed model class for ScheduleA
    
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
    def amendment_indicator_desc(self) -> str:
        """Get amendment_indicator_desc"""
        return self._data.get("amendment_indicator_desc")
    @amendment_indicator_desc.setter
    def amendment_indicator_desc(self, value: str):
        """Set amendment_indicator_desc"""
        self._data["amendment_indicator_desc"] = value

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
    def contributor(self) -> 'CommitteeHistory':
        """Get contributor"""
        return self._data.get("contributor")
    @contributor.setter
    def contributor(self, value: 'CommitteeHistory'):
        """Set contributor"""
        self._data["contributor"] = value

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
    def contributor_id(self) -> str:
        """Get contributor_id"""
        return self._data.get("contributor_id")
    @contributor_id.setter
    def contributor_id(self, value: str):
        """Set contributor_id"""
        self._data["contributor_id"] = value

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
    def contributor_street_1(self) -> str:
        """Get contributor_street_1"""
        return self._data.get("contributor_street_1")
    @contributor_street_1.setter
    def contributor_street_1(self, value: str):
        """Set contributor_street_1"""
        self._data["contributor_street_1"] = value

    @property
    def contributor_street_2(self) -> str:
        """Get contributor_street_2"""
        return self._data.get("contributor_street_2")
    @contributor_street_2.setter
    def contributor_street_2(self, value: str):
        """Set contributor_street_2"""
        self._data["contributor_street_2"] = value

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
    def donor_committee_name(self) -> str:
        """Get donor_committee_name"""
        return self._data.get("donor_committee_name")
    @donor_committee_name.setter
    def donor_committee_name(self, value: str):
        """Set donor_committee_name"""
        self._data["donor_committee_name"] = value

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
    def entity_type_desc(self) -> str:
        """Get entity_type_desc"""
        return self._data.get("entity_type_desc")
    @entity_type_desc.setter
    def entity_type_desc(self, value: str):
        """Set entity_type_desc"""
        self._data["entity_type_desc"] = value

    @property
    def fec_election_type_desc(self) -> str:
        """Get fec_election_type_desc"""
        return self._data.get("fec_election_type_desc")
    @fec_election_type_desc.setter
    def fec_election_type_desc(self, value: str):
        """Set fec_election_type_desc"""
        self._data["fec_election_type_desc"] = value

    @property
    def fec_election_year(self) -> str:
        """Get fec_election_year"""
        return self._data.get("fec_election_year")
    @fec_election_year.setter
    def fec_election_year(self, value: str):
        """Set fec_election_year"""
        self._data["fec_election_year"] = value

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
    def image_number(self) -> str:
        """Get image_number"""
        return self._data.get("image_number")
    @image_number.setter
    def image_number(self, value: str):
        """Set image_number"""
        self._data["image_number"] = value

    @property
    def increased_limit(self) -> str:
        """Get increased_limit"""
        return self._data.get("increased_limit")
    @increased_limit.setter
    def increased_limit(self, value: str):
        """Set increased_limit"""
        self._data["increased_limit"] = value

    @property
    def is_individual(self) -> bool:
        """Get is_individual"""
        return self._data.get("is_individual")
    @is_individual.setter
    def is_individual(self, value: bool):
        """Set is_individual"""
        self._data["is_individual"] = value

    @property
    def line_number(self) -> str:
        """Get line_number"""
        return self._data.get("line_number")
    @line_number.setter
    def line_number(self, value: str):
        """Set line_number"""
        self._data["line_number"] = value

    @property
    def line_number_label(self) -> str:
        """Get line_number_label"""
        return self._data.get("line_number_label")
    @line_number_label.setter
    def line_number_label(self, value: str):
        """Set line_number_label"""
        self._data["line_number_label"] = value

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
    def memoed_subtotal(self) -> bool:
        """Get memoed_subtotal"""
        return self._data.get("memoed_subtotal")
    @memoed_subtotal.setter
    def memoed_subtotal(self, value: bool):
        """Set memoed_subtotal"""
        self._data["memoed_subtotal"] = value

    @property
    def national_committee_nonfederal_account(self) -> str:
        """Get national_committee_nonfederal_account"""
        return self._data.get("national_committee_nonfederal_account")
    @national_committee_nonfederal_account.setter
    def national_committee_nonfederal_account(self, value: str):
        """Set national_committee_nonfederal_account"""
        self._data["national_committee_nonfederal_account"] = value

    @property
    def original_sub_id(self) -> str:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: str):
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
    def receipt_type(self) -> str:
        """Get receipt_type"""
        return self._data.get("receipt_type")
    @receipt_type.setter
    def receipt_type(self, value: str):
        """Set receipt_type"""
        self._data["receipt_type"] = value

    @property
    def receipt_type_desc(self) -> str:
        """Get receipt_type_desc"""
        return self._data.get("receipt_type_desc")
    @receipt_type_desc.setter
    def receipt_type_desc(self, value: str):
        """Set receipt_type_desc"""
        self._data["receipt_type_desc"] = value

    @property
    def receipt_type_full(self) -> str:
        """Get receipt_type_full"""
        return self._data.get("receipt_type_full")
    @receipt_type_full.setter
    def receipt_type_full(self, value: str):
        """Set receipt_type_full"""
        self._data["receipt_type_full"] = value

    @property
    def recipient_committee_designation(self) -> str:
        """Get recipient_committee_designation"""
        return self._data.get("recipient_committee_designation")
    @recipient_committee_designation.setter
    def recipient_committee_designation(self, value: str):
        """Set recipient_committee_designation"""
        self._data["recipient_committee_designation"] = value

    @property
    def recipient_committee_org_type(self) -> str:
        """Get recipient_committee_org_type"""
        return self._data.get("recipient_committee_org_type")
    @recipient_committee_org_type.setter
    def recipient_committee_org_type(self, value: str):
        """Set recipient_committee_org_type"""
        self._data["recipient_committee_org_type"] = value

    @property
    def recipient_committee_type(self) -> str:
        """Get recipient_committee_type"""
        return self._data.get("recipient_committee_type")
    @recipient_committee_type.setter
    def recipient_committee_type(self, value: str):
        """Set recipient_committee_type"""
        self._data["recipient_committee_type"] = value

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

    @property
    def two_year_transaction_period(self) -> int:
        """Get two_year_transaction_period"""
        return self._data.get("two_year_transaction_period")
    @two_year_transaction_period.setter
    def two_year_transaction_period(self, value: int):
        """Set two_year_transaction_period"""
        self._data["two_year_transaction_period"] = value

    @property
    def unused_contbr_id(self) -> str:
        """Get unused_contbr_id"""
        return self._data.get("unused_contbr_id")
    @unused_contbr_id.setter
    def unused_contbr_id(self, value: str):
        """Set unused_contbr_id"""
        self._data["unused_contbr_id"] = value
