from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CommitteeReportsPacParty(BaseModel):
    """
    Strongly-typed model class for CommitteeReportsPacParty
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def all_loans_received_period(self) -> float:
        """Get all_loans_received_period"""
        return self._data.get("all_loans_received_period")
    @all_loans_received_period.setter
    def all_loans_received_period(self, value: float):
        """Set all_loans_received_period"""
        self._data["all_loans_received_period"] = value

    @property
    def all_loans_received_ytd(self) -> float:
        """Get all_loans_received_ytd"""
        return self._data.get("all_loans_received_ytd")
    @all_loans_received_ytd.setter
    def all_loans_received_ytd(self, value: float):
        """Set all_loans_received_ytd"""
        self._data["all_loans_received_ytd"] = value

    @property
    def allocated_federal_election_levin_share_period(self) -> float:
        """Get allocated_federal_election_levin_share_period"""
        return self._data.get("allocated_federal_election_levin_share_period")
    @allocated_federal_election_levin_share_period.setter
    def allocated_federal_election_levin_share_period(self, value: float):
        """Set allocated_federal_election_levin_share_period"""
        self._data["allocated_federal_election_levin_share_period"] = value

    @property
    def amendment_chain(self) -> List[float]:
        """Get amendment_chain"""
        return self._data.get("amendment_chain")
    @amendment_chain.setter
    def amendment_chain(self, value: List[float]):
        """Set amendment_chain"""
        self._data["amendment_chain"] = value

    @property
    def amendment_indicator(self) -> str:
        """Get amendment_indicator"""
        return self._data.get("amendment_indicator")
    @amendment_indicator.setter
    def amendment_indicator(self, value: str):
        """Set amendment_indicator"""
        self._data["amendment_indicator"] = value

    @property
    def amendment_indicator_full(self) -> str:
        """Get amendment_indicator_full"""
        return self._data.get("amendment_indicator_full")
    @amendment_indicator_full.setter
    def amendment_indicator_full(self, value: str):
        """Set amendment_indicator_full"""
        self._data["amendment_indicator_full"] = value

    @property
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

    @property
    def calendar_ytd(self) -> int:
        """Get calendar_ytd"""
        return self._data.get("calendar_ytd")
    @calendar_ytd.setter
    def calendar_ytd(self, value: int):
        """Set calendar_ytd"""
        self._data["calendar_ytd"] = value

    @property
    def cash_on_hand_beginning_calendar_ytd(self) -> float:
        """Get cash_on_hand_beginning_calendar_ytd"""
        return self._data.get("cash_on_hand_beginning_calendar_ytd")
    @cash_on_hand_beginning_calendar_ytd.setter
    def cash_on_hand_beginning_calendar_ytd(self, value: float):
        """Set cash_on_hand_beginning_calendar_ytd"""
        self._data["cash_on_hand_beginning_calendar_ytd"] = value

    @property
    def cash_on_hand_beginning_period(self) -> float:
        """Get cash_on_hand_beginning_period"""
        return self._data.get("cash_on_hand_beginning_period")
    @cash_on_hand_beginning_period.setter
    def cash_on_hand_beginning_period(self, value: float):
        """Set cash_on_hand_beginning_period"""
        self._data["cash_on_hand_beginning_period"] = value

    @property
    def cash_on_hand_close_ytd(self) -> float:
        """Get cash_on_hand_close_ytd"""
        return self._data.get("cash_on_hand_close_ytd")
    @cash_on_hand_close_ytd.setter
    def cash_on_hand_close_ytd(self, value: float):
        """Set cash_on_hand_close_ytd"""
        self._data["cash_on_hand_close_ytd"] = value

    @property
    def cash_on_hand_end_period(self) -> float:
        """Get cash_on_hand_end_period"""
        return self._data.get("cash_on_hand_end_period")
    @cash_on_hand_end_period.setter
    def cash_on_hand_end_period(self, value: float):
        """Set cash_on_hand_end_period"""
        self._data["cash_on_hand_end_period"] = value

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
    def coordinated_expenditures_by_party_committee_period(self) -> float:
        """Get coordinated_expenditures_by_party_committee_period"""
        return self._data.get("coordinated_expenditures_by_party_committee_period")
    @coordinated_expenditures_by_party_committee_period.setter
    def coordinated_expenditures_by_party_committee_period(self, value: float):
        """Set coordinated_expenditures_by_party_committee_period"""
        self._data["coordinated_expenditures_by_party_committee_period"] = value

    @property
    def coordinated_expenditures_by_party_committee_ytd(self) -> float:
        """Get coordinated_expenditures_by_party_committee_ytd"""
        return self._data.get("coordinated_expenditures_by_party_committee_ytd")
    @coordinated_expenditures_by_party_committee_ytd.setter
    def coordinated_expenditures_by_party_committee_ytd(self, value: float):
        """Set coordinated_expenditures_by_party_committee_ytd"""
        self._data["coordinated_expenditures_by_party_committee_ytd"] = value

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
    def debts_owed_by_committee(self) -> float:
        """Get debts_owed_by_committee"""
        return self._data.get("debts_owed_by_committee")
    @debts_owed_by_committee.setter
    def debts_owed_by_committee(self, value: float):
        """Set debts_owed_by_committee"""
        self._data["debts_owed_by_committee"] = value

    @property
    def debts_owed_to_committee(self) -> float:
        """Get debts_owed_to_committee"""
        return self._data.get("debts_owed_to_committee")
    @debts_owed_to_committee.setter
    def debts_owed_to_committee(self, value: float):
        """Set debts_owed_to_committee"""
        self._data["debts_owed_to_committee"] = value

    @property
    def document_description(self) -> str:
        """Get document_description"""
        return self._data.get("document_description")
    @document_description.setter
    def document_description(self, value: str):
        """Set document_description"""
        self._data["document_description"] = value

    @property
    def end_image_number(self) -> str:
        """Get end_image_number"""
        return self._data.get("end_image_number")
    @end_image_number.setter
    def end_image_number(self, value: str):
        """Set end_image_number"""
        self._data["end_image_number"] = value

    @property
    def fec_file_id(self) -> str:
        """Get fec_file_id"""
        return self._data.get("fec_file_id")
    @fec_file_id.setter
    def fec_file_id(self, value: str):
        """Set fec_file_id"""
        self._data["fec_file_id"] = value

    @property
    def fec_url(self) -> str:
        """Get fec_url"""
        return self._data.get("fec_url")
    @fec_url.setter
    def fec_url(self, value: str):
        """Set fec_url"""
        self._data["fec_url"] = value

    @property
    def fed_candidate_committee_contribution_refunds_ytd(self) -> float:
        """Get fed_candidate_committee_contribution_refunds_ytd"""
        return self._data.get("fed_candidate_committee_contribution_refunds_ytd")
    @fed_candidate_committee_contribution_refunds_ytd.setter
    def fed_candidate_committee_contribution_refunds_ytd(self, value: float):
        """Set fed_candidate_committee_contribution_refunds_ytd"""
        self._data["fed_candidate_committee_contribution_refunds_ytd"] = value

    @property
    def fed_candidate_committee_contributions_period(self) -> float:
        """Get fed_candidate_committee_contributions_period"""
        return self._data.get("fed_candidate_committee_contributions_period")
    @fed_candidate_committee_contributions_period.setter
    def fed_candidate_committee_contributions_period(self, value: float):
        """Set fed_candidate_committee_contributions_period"""
        self._data["fed_candidate_committee_contributions_period"] = value

    @property
    def fed_candidate_committee_contributions_ytd(self) -> float:
        """Get fed_candidate_committee_contributions_ytd"""
        return self._data.get("fed_candidate_committee_contributions_ytd")
    @fed_candidate_committee_contributions_ytd.setter
    def fed_candidate_committee_contributions_ytd(self, value: float):
        """Set fed_candidate_committee_contributions_ytd"""
        self._data["fed_candidate_committee_contributions_ytd"] = value

    @property
    def fed_candidate_contribution_refunds_period(self) -> float:
        """Get fed_candidate_contribution_refunds_period"""
        return self._data.get("fed_candidate_contribution_refunds_period")
    @fed_candidate_contribution_refunds_period.setter
    def fed_candidate_contribution_refunds_period(self, value: float):
        """Set fed_candidate_contribution_refunds_period"""
        self._data["fed_candidate_contribution_refunds_period"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def html_url(self) -> str:
        """Get html_url"""
        return self._data.get("html_url")
    @html_url.setter
    def html_url(self, value: str):
        """Set html_url"""
        self._data["html_url"] = value

    @property
    def independent_expenditures_period(self) -> float:
        """Get independent_expenditures_period"""
        return self._data.get("independent_expenditures_period")
    @independent_expenditures_period.setter
    def independent_expenditures_period(self, value: float):
        """Set independent_expenditures_period"""
        self._data["independent_expenditures_period"] = value

    @property
    def independent_expenditures_ytd(self) -> float:
        """Get independent_expenditures_ytd"""
        return self._data.get("independent_expenditures_ytd")
    @independent_expenditures_ytd.setter
    def independent_expenditures_ytd(self, value: float):
        """Set independent_expenditures_ytd"""
        self._data["independent_expenditures_ytd"] = value

    @property
    def individual_itemized_contributions_period(self) -> float:
        """Get individual_itemized_contributions_period"""
        return self._data.get("individual_itemized_contributions_period")
    @individual_itemized_contributions_period.setter
    def individual_itemized_contributions_period(self, value: float):
        """Set individual_itemized_contributions_period"""
        self._data["individual_itemized_contributions_period"] = value

    @property
    def individual_itemized_contributions_ytd(self) -> float:
        """Get individual_itemized_contributions_ytd"""
        return self._data.get("individual_itemized_contributions_ytd")
    @individual_itemized_contributions_ytd.setter
    def individual_itemized_contributions_ytd(self, value: float):
        """Set individual_itemized_contributions_ytd"""
        self._data["individual_itemized_contributions_ytd"] = value

    @property
    def individual_unitemized_contributions_period(self) -> float:
        """Get individual_unitemized_contributions_period"""
        return self._data.get("individual_unitemized_contributions_period")
    @individual_unitemized_contributions_period.setter
    def individual_unitemized_contributions_period(self, value: float):
        """Set individual_unitemized_contributions_period"""
        self._data["individual_unitemized_contributions_period"] = value

    @property
    def individual_unitemized_contributions_ytd(self) -> float:
        """Get individual_unitemized_contributions_ytd"""
        return self._data.get("individual_unitemized_contributions_ytd")
    @individual_unitemized_contributions_ytd.setter
    def individual_unitemized_contributions_ytd(self, value: float):
        """Set individual_unitemized_contributions_ytd"""
        self._data["individual_unitemized_contributions_ytd"] = value

    @property
    def is_amended(self) -> bool:
        """Get is_amended"""
        return self._data.get("is_amended")
    @is_amended.setter
    def is_amended(self, value: bool):
        """Set is_amended"""
        self._data["is_amended"] = value

    @property
    def loan_repayments_made_period(self) -> float:
        """Get loan_repayments_made_period"""
        return self._data.get("loan_repayments_made_period")
    @loan_repayments_made_period.setter
    def loan_repayments_made_period(self, value: float):
        """Set loan_repayments_made_period"""
        self._data["loan_repayments_made_period"] = value

    @property
    def loan_repayments_made_ytd(self) -> float:
        """Get loan_repayments_made_ytd"""
        return self._data.get("loan_repayments_made_ytd")
    @loan_repayments_made_ytd.setter
    def loan_repayments_made_ytd(self, value: float):
        """Set loan_repayments_made_ytd"""
        self._data["loan_repayments_made_ytd"] = value

    @property
    def loan_repayments_received_period(self) -> float:
        """Get loan_repayments_received_period"""
        return self._data.get("loan_repayments_received_period")
    @loan_repayments_received_period.setter
    def loan_repayments_received_period(self, value: float):
        """Set loan_repayments_received_period"""
        self._data["loan_repayments_received_period"] = value

    @property
    def loan_repayments_received_ytd(self) -> float:
        """Get loan_repayments_received_ytd"""
        return self._data.get("loan_repayments_received_ytd")
    @loan_repayments_received_ytd.setter
    def loan_repayments_received_ytd(self, value: float):
        """Set loan_repayments_received_ytd"""
        self._data["loan_repayments_received_ytd"] = value

    @property
    def loans_made_period(self) -> float:
        """Get loans_made_period"""
        return self._data.get("loans_made_period")
    @loans_made_period.setter
    def loans_made_period(self, value: float):
        """Set loans_made_period"""
        self._data["loans_made_period"] = value

    @property
    def loans_made_ytd(self) -> float:
        """Get loans_made_ytd"""
        return self._data.get("loans_made_ytd")
    @loans_made_ytd.setter
    def loans_made_ytd(self, value: float):
        """Set loans_made_ytd"""
        self._data["loans_made_ytd"] = value

    @property
    def means_filed(self) -> str:
        """Get means_filed"""
        return self._data.get("means_filed")
    @means_filed.setter
    def means_filed(self, value: str):
        """Set means_filed"""
        self._data["means_filed"] = value

    @property
    def most_recent(self) -> bool:
        """Get most_recent"""
        return self._data.get("most_recent")
    @most_recent.setter
    def most_recent(self, value: bool):
        """Set most_recent"""
        self._data["most_recent"] = value

    @property
    def most_recent_file_number(self) -> float:
        """Get most_recent_file_number"""
        return self._data.get("most_recent_file_number")
    @most_recent_file_number.setter
    def most_recent_file_number(self, value: float):
        """Set most_recent_file_number"""
        self._data["most_recent_file_number"] = value

    @property
    def net_contributions_period(self) -> float:
        """Get net_contributions_period"""
        return self._data.get("net_contributions_period")
    @net_contributions_period.setter
    def net_contributions_period(self, value: float):
        """Set net_contributions_period"""
        self._data["net_contributions_period"] = value

    @property
    def net_contributions_ytd(self) -> float:
        """Get net_contributions_ytd"""
        return self._data.get("net_contributions_ytd")
    @net_contributions_ytd.setter
    def net_contributions_ytd(self, value: float):
        """Set net_contributions_ytd"""
        self._data["net_contributions_ytd"] = value

    @property
    def net_operating_expenditures_period(self) -> float:
        """Get net_operating_expenditures_period"""
        return self._data.get("net_operating_expenditures_period")
    @net_operating_expenditures_period.setter
    def net_operating_expenditures_period(self, value: float):
        """Set net_operating_expenditures_period"""
        self._data["net_operating_expenditures_period"] = value

    @property
    def net_operating_expenditures_ytd(self) -> float:
        """Get net_operating_expenditures_ytd"""
        return self._data.get("net_operating_expenditures_ytd")
    @net_operating_expenditures_ytd.setter
    def net_operating_expenditures_ytd(self, value: float):
        """Set net_operating_expenditures_ytd"""
        self._data["net_operating_expenditures_ytd"] = value

    @property
    def non_allocated_fed_election_activity_period(self) -> float:
        """Get non_allocated_fed_election_activity_period"""
        return self._data.get("non_allocated_fed_election_activity_period")
    @non_allocated_fed_election_activity_period.setter
    def non_allocated_fed_election_activity_period(self, value: float):
        """Set non_allocated_fed_election_activity_period"""
        self._data["non_allocated_fed_election_activity_period"] = value

    @property
    def non_allocated_fed_election_activity_ytd(self) -> float:
        """Get non_allocated_fed_election_activity_ytd"""
        return self._data.get("non_allocated_fed_election_activity_ytd")
    @non_allocated_fed_election_activity_ytd.setter
    def non_allocated_fed_election_activity_ytd(self, value: float):
        """Set non_allocated_fed_election_activity_ytd"""
        self._data["non_allocated_fed_election_activity_ytd"] = value

    @property
    def nonfed_share_allocated_disbursements_period(self) -> float:
        """Get nonfed_share_allocated_disbursements_period"""
        return self._data.get("nonfed_share_allocated_disbursements_period")
    @nonfed_share_allocated_disbursements_period.setter
    def nonfed_share_allocated_disbursements_period(self, value: float):
        """Set nonfed_share_allocated_disbursements_period"""
        self._data["nonfed_share_allocated_disbursements_period"] = value

    @property
    def offsets_to_operating_expenditures_period(self) -> float:
        """Get offsets_to_operating_expenditures_period"""
        return self._data.get("offsets_to_operating_expenditures_period")
    @offsets_to_operating_expenditures_period.setter
    def offsets_to_operating_expenditures_period(self, value: float):
        """Set offsets_to_operating_expenditures_period"""
        self._data["offsets_to_operating_expenditures_period"] = value

    @property
    def offsets_to_operating_expenditures_ytd(self) -> float:
        """Get offsets_to_operating_expenditures_ytd"""
        return self._data.get("offsets_to_operating_expenditures_ytd")
    @offsets_to_operating_expenditures_ytd.setter
    def offsets_to_operating_expenditures_ytd(self, value: float):
        """Set offsets_to_operating_expenditures_ytd"""
        self._data["offsets_to_operating_expenditures_ytd"] = value

    @property
    def other_disbursements_period(self) -> float:
        """Get other_disbursements_period"""
        return self._data.get("other_disbursements_period")
    @other_disbursements_period.setter
    def other_disbursements_period(self, value: float):
        """Set other_disbursements_period"""
        self._data["other_disbursements_period"] = value

    @property
    def other_disbursements_ytd(self) -> float:
        """Get other_disbursements_ytd"""
        return self._data.get("other_disbursements_ytd")
    @other_disbursements_ytd.setter
    def other_disbursements_ytd(self, value: float):
        """Set other_disbursements_ytd"""
        self._data["other_disbursements_ytd"] = value

    @property
    def other_fed_operating_expenditures_period(self) -> float:
        """Get other_fed_operating_expenditures_period"""
        return self._data.get("other_fed_operating_expenditures_period")
    @other_fed_operating_expenditures_period.setter
    def other_fed_operating_expenditures_period(self, value: float):
        """Set other_fed_operating_expenditures_period"""
        self._data["other_fed_operating_expenditures_period"] = value

    @property
    def other_fed_operating_expenditures_ytd(self) -> float:
        """Get other_fed_operating_expenditures_ytd"""
        return self._data.get("other_fed_operating_expenditures_ytd")
    @other_fed_operating_expenditures_ytd.setter
    def other_fed_operating_expenditures_ytd(self, value: float):
        """Set other_fed_operating_expenditures_ytd"""
        self._data["other_fed_operating_expenditures_ytd"] = value

    @property
    def other_fed_receipts_period(self) -> float:
        """Get other_fed_receipts_period"""
        return self._data.get("other_fed_receipts_period")
    @other_fed_receipts_period.setter
    def other_fed_receipts_period(self, value: float):
        """Set other_fed_receipts_period"""
        self._data["other_fed_receipts_period"] = value

    @property
    def other_fed_receipts_ytd(self) -> float:
        """Get other_fed_receipts_ytd"""
        return self._data.get("other_fed_receipts_ytd")
    @other_fed_receipts_ytd.setter
    def other_fed_receipts_ytd(self, value: float):
        """Set other_fed_receipts_ytd"""
        self._data["other_fed_receipts_ytd"] = value

    @property
    def other_political_committee_contributions_period(self) -> float:
        """Get other_political_committee_contributions_period"""
        return self._data.get("other_political_committee_contributions_period")
    @other_political_committee_contributions_period.setter
    def other_political_committee_contributions_period(self, value: float):
        """Set other_political_committee_contributions_period"""
        self._data["other_political_committee_contributions_period"] = value

    @property
    def other_political_committee_contributions_ytd(self) -> float:
        """Get other_political_committee_contributions_ytd"""
        return self._data.get("other_political_committee_contributions_ytd")
    @other_political_committee_contributions_ytd.setter
    def other_political_committee_contributions_ytd(self, value: float):
        """Set other_political_committee_contributions_ytd"""
        self._data["other_political_committee_contributions_ytd"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def political_party_committee_contributions_period(self) -> float:
        """Get political_party_committee_contributions_period"""
        return self._data.get("political_party_committee_contributions_period")
    @political_party_committee_contributions_period.setter
    def political_party_committee_contributions_period(self, value: float):
        """Set political_party_committee_contributions_period"""
        self._data["political_party_committee_contributions_period"] = value

    @property
    def political_party_committee_contributions_ytd(self) -> float:
        """Get political_party_committee_contributions_ytd"""
        return self._data.get("political_party_committee_contributions_ytd")
    @political_party_committee_contributions_ytd.setter
    def political_party_committee_contributions_ytd(self, value: float):
        """Set political_party_committee_contributions_ytd"""
        self._data["political_party_committee_contributions_ytd"] = value

    @property
    def previous_file_number(self) -> float:
        """Get previous_file_number"""
        return self._data.get("previous_file_number")
    @previous_file_number.setter
    def previous_file_number(self, value: float):
        """Set previous_file_number"""
        self._data["previous_file_number"] = value

    @property
    def receipt_date(self) -> str:
        """Get receipt_date"""
        return self._data.get("receipt_date")
    @receipt_date.setter
    def receipt_date(self, value: str):
        """Set receipt_date"""
        self._data["receipt_date"] = value

    @property
    def refunded_individual_contributions_period(self) -> float:
        """Get refunded_individual_contributions_period"""
        return self._data.get("refunded_individual_contributions_period")
    @refunded_individual_contributions_period.setter
    def refunded_individual_contributions_period(self, value: float):
        """Set refunded_individual_contributions_period"""
        self._data["refunded_individual_contributions_period"] = value

    @property
    def refunded_individual_contributions_ytd(self) -> float:
        """Get refunded_individual_contributions_ytd"""
        return self._data.get("refunded_individual_contributions_ytd")
    @refunded_individual_contributions_ytd.setter
    def refunded_individual_contributions_ytd(self, value: float):
        """Set refunded_individual_contributions_ytd"""
        self._data["refunded_individual_contributions_ytd"] = value

    @property
    def refunded_other_political_committee_contributions_period(self) -> float:
        """Get refunded_other_political_committee_contributions_period"""
        return self._data.get("refunded_other_political_committee_contributions_period")
    @refunded_other_political_committee_contributions_period.setter
    def refunded_other_political_committee_contributions_period(self, value: float):
        """Set refunded_other_political_committee_contributions_period"""
        self._data["refunded_other_political_committee_contributions_period"] = value

    @property
    def refunded_other_political_committee_contributions_ytd(self) -> float:
        """Get refunded_other_political_committee_contributions_ytd"""
        return self._data.get("refunded_other_political_committee_contributions_ytd")
    @refunded_other_political_committee_contributions_ytd.setter
    def refunded_other_political_committee_contributions_ytd(self, value: float):
        """Set refunded_other_political_committee_contributions_ytd"""
        self._data["refunded_other_political_committee_contributions_ytd"] = value

    @property
    def refunded_political_party_committee_contributions_period(self) -> float:
        """Get refunded_political_party_committee_contributions_period"""
        return self._data.get("refunded_political_party_committee_contributions_period")
    @refunded_political_party_committee_contributions_period.setter
    def refunded_political_party_committee_contributions_period(self, value: float):
        """Set refunded_political_party_committee_contributions_period"""
        self._data["refunded_political_party_committee_contributions_period"] = value

    @property
    def refunded_political_party_committee_contributions_ytd(self) -> float:
        """Get refunded_political_party_committee_contributions_ytd"""
        return self._data.get("refunded_political_party_committee_contributions_ytd")
    @refunded_political_party_committee_contributions_ytd.setter
    def refunded_political_party_committee_contributions_ytd(self, value: float):
        """Set refunded_political_party_committee_contributions_ytd"""
        self._data["refunded_political_party_committee_contributions_ytd"] = value

    @property
    def report_form(self) -> str:
        """Get report_form"""
        return self._data.get("report_form")
    @report_form.setter
    def report_form(self, value: str):
        """Set report_form"""
        self._data["report_form"] = value

    @property
    def report_type(self) -> str:
        """Get report_type"""
        return self._data.get("report_type")
    @report_type.setter
    def report_type(self, value: str):
        """Set report_type"""
        self._data["report_type"] = value

    @property
    def report_type_full(self) -> str:
        """Get report_type_full"""
        return self._data.get("report_type_full")
    @report_type_full.setter
    def report_type_full(self, value: str):
        """Set report_type_full"""
        self._data["report_type_full"] = value

    @property
    def report_year(self) -> int:
        """Get report_year"""
        return self._data.get("report_year")
    @report_year.setter
    def report_year(self, value: int):
        """Set report_year"""
        self._data["report_year"] = value

    @property
    def shared_fed_activity_nonfed_ytd(self) -> float:
        """Get shared_fed_activity_nonfed_ytd"""
        return self._data.get("shared_fed_activity_nonfed_ytd")
    @shared_fed_activity_nonfed_ytd.setter
    def shared_fed_activity_nonfed_ytd(self, value: float):
        """Set shared_fed_activity_nonfed_ytd"""
        self._data["shared_fed_activity_nonfed_ytd"] = value

    @property
    def shared_fed_activity_period(self) -> float:
        """Get shared_fed_activity_period"""
        return self._data.get("shared_fed_activity_period")
    @shared_fed_activity_period.setter
    def shared_fed_activity_period(self, value: float):
        """Set shared_fed_activity_period"""
        self._data["shared_fed_activity_period"] = value

    @property
    def shared_fed_activity_ytd(self) -> float:
        """Get shared_fed_activity_ytd"""
        return self._data.get("shared_fed_activity_ytd")
    @shared_fed_activity_ytd.setter
    def shared_fed_activity_ytd(self, value: float):
        """Set shared_fed_activity_ytd"""
        self._data["shared_fed_activity_ytd"] = value

    @property
    def shared_fed_operating_expenditures_period(self) -> float:
        """Get shared_fed_operating_expenditures_period"""
        return self._data.get("shared_fed_operating_expenditures_period")
    @shared_fed_operating_expenditures_period.setter
    def shared_fed_operating_expenditures_period(self, value: float):
        """Set shared_fed_operating_expenditures_period"""
        self._data["shared_fed_operating_expenditures_period"] = value

    @property
    def shared_fed_operating_expenditures_ytd(self) -> float:
        """Get shared_fed_operating_expenditures_ytd"""
        return self._data.get("shared_fed_operating_expenditures_ytd")
    @shared_fed_operating_expenditures_ytd.setter
    def shared_fed_operating_expenditures_ytd(self, value: float):
        """Set shared_fed_operating_expenditures_ytd"""
        self._data["shared_fed_operating_expenditures_ytd"] = value

    @property
    def shared_nonfed_operating_expenditures_period(self) -> float:
        """Get shared_nonfed_operating_expenditures_period"""
        return self._data.get("shared_nonfed_operating_expenditures_period")
    @shared_nonfed_operating_expenditures_period.setter
    def shared_nonfed_operating_expenditures_period(self, value: float):
        """Set shared_nonfed_operating_expenditures_period"""
        self._data["shared_nonfed_operating_expenditures_period"] = value

    @property
    def shared_nonfed_operating_expenditures_ytd(self) -> float:
        """Get shared_nonfed_operating_expenditures_ytd"""
        return self._data.get("shared_nonfed_operating_expenditures_ytd")
    @shared_nonfed_operating_expenditures_ytd.setter
    def shared_nonfed_operating_expenditures_ytd(self, value: float):
        """Set shared_nonfed_operating_expenditures_ytd"""
        self._data["shared_nonfed_operating_expenditures_ytd"] = value

    @property
    def subtotal_summary_page_period(self) -> float:
        """Get subtotal_summary_page_period"""
        return self._data.get("subtotal_summary_page_period")
    @subtotal_summary_page_period.setter
    def subtotal_summary_page_period(self, value: float):
        """Set subtotal_summary_page_period"""
        self._data["subtotal_summary_page_period"] = value

    @property
    def subtotal_summary_ytd(self) -> float:
        """Get subtotal_summary_ytd"""
        return self._data.get("subtotal_summary_ytd")
    @subtotal_summary_ytd.setter
    def subtotal_summary_ytd(self, value: float):
        """Set subtotal_summary_ytd"""
        self._data["subtotal_summary_ytd"] = value

    @property
    def total_contribution_refunds_period(self) -> float:
        """Get total_contribution_refunds_period"""
        return self._data.get("total_contribution_refunds_period")
    @total_contribution_refunds_period.setter
    def total_contribution_refunds_period(self, value: float):
        """Set total_contribution_refunds_period"""
        self._data["total_contribution_refunds_period"] = value

    @property
    def total_contribution_refunds_ytd(self) -> float:
        """Get total_contribution_refunds_ytd"""
        return self._data.get("total_contribution_refunds_ytd")
    @total_contribution_refunds_ytd.setter
    def total_contribution_refunds_ytd(self, value: float):
        """Set total_contribution_refunds_ytd"""
        self._data["total_contribution_refunds_ytd"] = value

    @property
    def total_contributions_period(self) -> float:
        """Get total_contributions_period"""
        return self._data.get("total_contributions_period")
    @total_contributions_period.setter
    def total_contributions_period(self, value: float):
        """Set total_contributions_period"""
        self._data["total_contributions_period"] = value

    @property
    def total_contributions_ytd(self) -> float:
        """Get total_contributions_ytd"""
        return self._data.get("total_contributions_ytd")
    @total_contributions_ytd.setter
    def total_contributions_ytd(self, value: float):
        """Set total_contributions_ytd"""
        self._data["total_contributions_ytd"] = value

    @property
    def total_disbursements_period(self) -> float:
        """Get total_disbursements_period"""
        return self._data.get("total_disbursements_period")
    @total_disbursements_period.setter
    def total_disbursements_period(self, value: float):
        """Set total_disbursements_period"""
        self._data["total_disbursements_period"] = value

    @property
    def total_disbursements_ytd(self) -> float:
        """Get total_disbursements_ytd"""
        return self._data.get("total_disbursements_ytd")
    @total_disbursements_ytd.setter
    def total_disbursements_ytd(self, value: float):
        """Set total_disbursements_ytd"""
        self._data["total_disbursements_ytd"] = value

    @property
    def total_fed_disbursements_period(self) -> float:
        """Get total_fed_disbursements_period"""
        return self._data.get("total_fed_disbursements_period")
    @total_fed_disbursements_period.setter
    def total_fed_disbursements_period(self, value: float):
        """Set total_fed_disbursements_period"""
        self._data["total_fed_disbursements_period"] = value

    @property
    def total_fed_disbursements_ytd(self) -> float:
        """Get total_fed_disbursements_ytd"""
        return self._data.get("total_fed_disbursements_ytd")
    @total_fed_disbursements_ytd.setter
    def total_fed_disbursements_ytd(self, value: float):
        """Set total_fed_disbursements_ytd"""
        self._data["total_fed_disbursements_ytd"] = value

    @property
    def total_fed_election_activity_period(self) -> float:
        """Get total_fed_election_activity_period"""
        return self._data.get("total_fed_election_activity_period")
    @total_fed_election_activity_period.setter
    def total_fed_election_activity_period(self, value: float):
        """Set total_fed_election_activity_period"""
        self._data["total_fed_election_activity_period"] = value

    @property
    def total_fed_election_activity_ytd(self) -> float:
        """Get total_fed_election_activity_ytd"""
        return self._data.get("total_fed_election_activity_ytd")
    @total_fed_election_activity_ytd.setter
    def total_fed_election_activity_ytd(self, value: float):
        """Set total_fed_election_activity_ytd"""
        self._data["total_fed_election_activity_ytd"] = value

    @property
    def total_fed_operating_expenditures_period(self) -> float:
        """Get total_fed_operating_expenditures_period"""
        return self._data.get("total_fed_operating_expenditures_period")
    @total_fed_operating_expenditures_period.setter
    def total_fed_operating_expenditures_period(self, value: float):
        """Set total_fed_operating_expenditures_period"""
        self._data["total_fed_operating_expenditures_period"] = value

    @property
    def total_fed_operating_expenditures_ytd(self) -> float:
        """Get total_fed_operating_expenditures_ytd"""
        return self._data.get("total_fed_operating_expenditures_ytd")
    @total_fed_operating_expenditures_ytd.setter
    def total_fed_operating_expenditures_ytd(self, value: float):
        """Set total_fed_operating_expenditures_ytd"""
        self._data["total_fed_operating_expenditures_ytd"] = value

    @property
    def total_fed_receipts_period(self) -> float:
        """Get total_fed_receipts_period"""
        return self._data.get("total_fed_receipts_period")
    @total_fed_receipts_period.setter
    def total_fed_receipts_period(self, value: float):
        """Set total_fed_receipts_period"""
        self._data["total_fed_receipts_period"] = value

    @property
    def total_fed_receipts_ytd(self) -> float:
        """Get total_fed_receipts_ytd"""
        return self._data.get("total_fed_receipts_ytd")
    @total_fed_receipts_ytd.setter
    def total_fed_receipts_ytd(self, value: float):
        """Set total_fed_receipts_ytd"""
        self._data["total_fed_receipts_ytd"] = value

    @property
    def total_individual_contributions_period(self) -> float:
        """Get total_individual_contributions_period"""
        return self._data.get("total_individual_contributions_period")
    @total_individual_contributions_period.setter
    def total_individual_contributions_period(self, value: float):
        """Set total_individual_contributions_period"""
        self._data["total_individual_contributions_period"] = value

    @property
    def total_individual_contributions_ytd(self) -> float:
        """Get total_individual_contributions_ytd"""
        return self._data.get("total_individual_contributions_ytd")
    @total_individual_contributions_ytd.setter
    def total_individual_contributions_ytd(self, value: float):
        """Set total_individual_contributions_ytd"""
        self._data["total_individual_contributions_ytd"] = value

    @property
    def total_nonfed_transfers_period(self) -> float:
        """Get total_nonfed_transfers_period"""
        return self._data.get("total_nonfed_transfers_period")
    @total_nonfed_transfers_period.setter
    def total_nonfed_transfers_period(self, value: float):
        """Set total_nonfed_transfers_period"""
        self._data["total_nonfed_transfers_period"] = value

    @property
    def total_nonfed_transfers_ytd(self) -> float:
        """Get total_nonfed_transfers_ytd"""
        return self._data.get("total_nonfed_transfers_ytd")
    @total_nonfed_transfers_ytd.setter
    def total_nonfed_transfers_ytd(self, value: float):
        """Set total_nonfed_transfers_ytd"""
        self._data["total_nonfed_transfers_ytd"] = value

    @property
    def total_operating_expenditures_period(self) -> float:
        """Get total_operating_expenditures_period"""
        return self._data.get("total_operating_expenditures_period")
    @total_operating_expenditures_period.setter
    def total_operating_expenditures_period(self, value: float):
        """Set total_operating_expenditures_period"""
        self._data["total_operating_expenditures_period"] = value

    @property
    def total_operating_expenditures_ytd(self) -> float:
        """Get total_operating_expenditures_ytd"""
        return self._data.get("total_operating_expenditures_ytd")
    @total_operating_expenditures_ytd.setter
    def total_operating_expenditures_ytd(self, value: float):
        """Set total_operating_expenditures_ytd"""
        self._data["total_operating_expenditures_ytd"] = value

    @property
    def total_receipts_period(self) -> float:
        """Get total_receipts_period"""
        return self._data.get("total_receipts_period")
    @total_receipts_period.setter
    def total_receipts_period(self, value: float):
        """Set total_receipts_period"""
        self._data["total_receipts_period"] = value

    @property
    def total_receipts_ytd(self) -> float:
        """Get total_receipts_ytd"""
        return self._data.get("total_receipts_ytd")
    @total_receipts_ytd.setter
    def total_receipts_ytd(self, value: float):
        """Set total_receipts_ytd"""
        self._data["total_receipts_ytd"] = value

    @property
    def transfers_from_affiliated_party_period(self) -> float:
        """Get transfers_from_affiliated_party_period"""
        return self._data.get("transfers_from_affiliated_party_period")
    @transfers_from_affiliated_party_period.setter
    def transfers_from_affiliated_party_period(self, value: float):
        """Set transfers_from_affiliated_party_period"""
        self._data["transfers_from_affiliated_party_period"] = value

    @property
    def transfers_from_affiliated_party_ytd(self) -> float:
        """Get transfers_from_affiliated_party_ytd"""
        return self._data.get("transfers_from_affiliated_party_ytd")
    @transfers_from_affiliated_party_ytd.setter
    def transfers_from_affiliated_party_ytd(self, value: float):
        """Set transfers_from_affiliated_party_ytd"""
        self._data["transfers_from_affiliated_party_ytd"] = value

    @property
    def transfers_from_nonfed_account_period(self) -> float:
        """Get transfers_from_nonfed_account_period"""
        return self._data.get("transfers_from_nonfed_account_period")
    @transfers_from_nonfed_account_period.setter
    def transfers_from_nonfed_account_period(self, value: float):
        """Set transfers_from_nonfed_account_period"""
        self._data["transfers_from_nonfed_account_period"] = value

    @property
    def transfers_from_nonfed_account_ytd(self) -> float:
        """Get transfers_from_nonfed_account_ytd"""
        return self._data.get("transfers_from_nonfed_account_ytd")
    @transfers_from_nonfed_account_ytd.setter
    def transfers_from_nonfed_account_ytd(self, value: float):
        """Set transfers_from_nonfed_account_ytd"""
        self._data["transfers_from_nonfed_account_ytd"] = value

    @property
    def transfers_from_nonfed_levin_period(self) -> float:
        """Get transfers_from_nonfed_levin_period"""
        return self._data.get("transfers_from_nonfed_levin_period")
    @transfers_from_nonfed_levin_period.setter
    def transfers_from_nonfed_levin_period(self, value: float):
        """Set transfers_from_nonfed_levin_period"""
        self._data["transfers_from_nonfed_levin_period"] = value

    @property
    def transfers_from_nonfed_levin_ytd(self) -> float:
        """Get transfers_from_nonfed_levin_ytd"""
        return self._data.get("transfers_from_nonfed_levin_ytd")
    @transfers_from_nonfed_levin_ytd.setter
    def transfers_from_nonfed_levin_ytd(self, value: float):
        """Set transfers_from_nonfed_levin_ytd"""
        self._data["transfers_from_nonfed_levin_ytd"] = value

    @property
    def transfers_to_affiliated_committee_period(self) -> float:
        """Get transfers_to_affiliated_committee_period"""
        return self._data.get("transfers_to_affiliated_committee_period")
    @transfers_to_affiliated_committee_period.setter
    def transfers_to_affiliated_committee_period(self, value: float):
        """Set transfers_to_affiliated_committee_period"""
        self._data["transfers_to_affiliated_committee_period"] = value

    @property
    def transfers_to_affilitated_committees_ytd(self) -> float:
        """Get transfers_to_affilitated_committees_ytd"""
        return self._data.get("transfers_to_affilitated_committees_ytd")
    @transfers_to_affilitated_committees_ytd.setter
    def transfers_to_affilitated_committees_ytd(self, value: float):
        """Set transfers_to_affilitated_committees_ytd"""
        self._data["transfers_to_affilitated_committees_ytd"] = value
