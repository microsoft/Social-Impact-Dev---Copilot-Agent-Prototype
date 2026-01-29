from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CommitteeTotalsHouseSenate(BaseModel):
    """
    Strongly-typed model class for CommitteeTotalsHouseSenate
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def all_other_loans(self) -> float:
        """Get all_other_loans"""
        return self._data.get("all_other_loans")
    @all_other_loans.setter
    def all_other_loans(self, value: float):
        """Set all_other_loans"""
        self._data["all_other_loans"] = value

    @property
    def candidate_contribution(self) -> float:
        """Get candidate_contribution"""
        return self._data.get("candidate_contribution")
    @candidate_contribution.setter
    def candidate_contribution(self, value: float):
        """Set candidate_contribution"""
        self._data["candidate_contribution"] = value

    @property
    def cash_on_hand_beginning_period(self) -> float:
        """Get cash_on_hand_beginning_period"""
        return self._data.get("cash_on_hand_beginning_period")
    @cash_on_hand_beginning_period.setter
    def cash_on_hand_beginning_period(self, value: float):
        """Set cash_on_hand_beginning_period"""
        self._data["cash_on_hand_beginning_period"] = value

    @property
    def committee_designation(self) -> str:
        """Get committee_designation"""
        return self._data.get("committee_designation")
    @committee_designation.setter
    def committee_designation(self, value: str):
        """Set committee_designation"""
        self._data["committee_designation"] = value

    @property
    def committee_designation_full(self) -> str:
        """Get committee_designation_full"""
        return self._data.get("committee_designation_full")
    @committee_designation_full.setter
    def committee_designation_full(self, value: str):
        """Set committee_designation_full"""
        self._data["committee_designation_full"] = value

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
    def committee_state(self) -> str:
        """Get committee_state"""
        return self._data.get("committee_state")
    @committee_state.setter
    def committee_state(self, value: str):
        """Set committee_state"""
        self._data["committee_state"] = value

    @property
    def committee_type(self) -> str:
        """Get committee_type"""
        return self._data.get("committee_type")
    @committee_type.setter
    def committee_type(self, value: str):
        """Set committee_type"""
        self._data["committee_type"] = value

    @property
    def committee_type_full(self) -> str:
        """Get committee_type_full"""
        return self._data.get("committee_type_full")
    @committee_type_full.setter
    def committee_type_full(self, value: str):
        """Set committee_type_full"""
        self._data["committee_type_full"] = value

    @property
    def contribution_refunds(self) -> float:
        """Get contribution_refunds"""
        return self._data.get("contribution_refunds")
    @contribution_refunds.setter
    def contribution_refunds(self, value: float):
        """Set contribution_refunds"""
        self._data["contribution_refunds"] = value

    @property
    def contributions(self) -> float:
        """Get contributions"""
        return self._data.get("contributions")
    @contributions.setter
    def contributions(self, value: float):
        """Set contributions"""
        self._data["contributions"] = value

    @property
    def contributions_ie_and_party_expenditures_made_percent(self) -> float:
        """Get contributions_ie_and_party_expenditures_made_percent"""
        return self._data.get("contributions_ie_and_party_expenditures_made_percent")
    @contributions_ie_and_party_expenditures_made_percent.setter
    def contributions_ie_and_party_expenditures_made_percent(self, value: float):
        """Set contributions_ie_and_party_expenditures_made_percent"""
        self._data["contributions_ie_and_party_expenditures_made_percent"] = value

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
    def cycle(self) -> int:
        """Get cycle"""
        return self._data.get("cycle")
    @cycle.setter
    def cycle(self, value: int):
        """Set cycle"""
        self._data["cycle"] = value

    @property
    def disbursements(self) -> float:
        """Get disbursements"""
        return self._data.get("disbursements")
    @disbursements.setter
    def disbursements(self, value: float):
        """Set disbursements"""
        self._data["disbursements"] = value

    @property
    def filing_frequency(self) -> str:
        """Get filing_frequency"""
        return self._data.get("filing_frequency")
    @filing_frequency.setter
    def filing_frequency(self, value: str):
        """Set filing_frequency"""
        self._data["filing_frequency"] = value

    @property
    def filing_frequency_full(self) -> str:
        """Get filing_frequency_full"""
        return self._data.get("filing_frequency_full")
    @filing_frequency_full.setter
    def filing_frequency_full(self, value: str):
        """Set filing_frequency_full"""
        self._data["filing_frequency_full"] = value

    @property
    def first_f1_date(self) -> str:
        """Get first_f1_date"""
        return self._data.get("first_f1_date")
    @first_f1_date.setter
    def first_f1_date(self, value: str):
        """Set first_f1_date"""
        self._data["first_f1_date"] = value

    @property
    def first_file_date(self) -> str:
        """Get first_file_date"""
        return self._data.get("first_file_date")
    @first_file_date.setter
    def first_file_date(self, value: str):
        """Set first_file_date"""
        self._data["first_file_date"] = value

    @property
    def individual_contributions(self) -> float:
        """Get individual_contributions"""
        return self._data.get("individual_contributions")
    @individual_contributions.setter
    def individual_contributions(self, value: float):
        """Set individual_contributions"""
        self._data["individual_contributions"] = value

    @property
    def individual_contributions_percent(self) -> float:
        """Get individual_contributions_percent"""
        return self._data.get("individual_contributions_percent")
    @individual_contributions_percent.setter
    def individual_contributions_percent(self, value: float):
        """Set individual_contributions_percent"""
        self._data["individual_contributions_percent"] = value

    @property
    def individual_itemized_contributions(self) -> float:
        """Get individual_itemized_contributions"""
        return self._data.get("individual_itemized_contributions")
    @individual_itemized_contributions.setter
    def individual_itemized_contributions(self, value: float):
        """Set individual_itemized_contributions"""
        self._data["individual_itemized_contributions"] = value

    @property
    def individual_unitemized_contributions(self) -> float:
        """Get individual_unitemized_contributions"""
        return self._data.get("individual_unitemized_contributions")
    @individual_unitemized_contributions.setter
    def individual_unitemized_contributions(self, value: float):
        """Set individual_unitemized_contributions"""
        self._data["individual_unitemized_contributions"] = value

    @property
    def last_beginning_image_number(self) -> str:
        """Get last_beginning_image_number"""
        return self._data.get("last_beginning_image_number")
    @last_beginning_image_number.setter
    def last_beginning_image_number(self, value: str):
        """Set last_beginning_image_number"""
        self._data["last_beginning_image_number"] = value

    @property
    def last_cash_on_hand_end_period(self) -> float:
        """Get last_cash_on_hand_end_period"""
        return self._data.get("last_cash_on_hand_end_period")
    @last_cash_on_hand_end_period.setter
    def last_cash_on_hand_end_period(self, value: float):
        """Set last_cash_on_hand_end_period"""
        self._data["last_cash_on_hand_end_period"] = value

    @property
    def last_debts_owed_by_committee(self) -> float:
        """Get last_debts_owed_by_committee"""
        return self._data.get("last_debts_owed_by_committee")
    @last_debts_owed_by_committee.setter
    def last_debts_owed_by_committee(self, value: float):
        """Set last_debts_owed_by_committee"""
        self._data["last_debts_owed_by_committee"] = value

    @property
    def last_debts_owed_to_committee(self) -> float:
        """Get last_debts_owed_to_committee"""
        return self._data.get("last_debts_owed_to_committee")
    @last_debts_owed_to_committee.setter
    def last_debts_owed_to_committee(self, value: float):
        """Set last_debts_owed_to_committee"""
        self._data["last_debts_owed_to_committee"] = value

    @property
    def last_report_type_full(self) -> str:
        """Get last_report_type_full"""
        return self._data.get("last_report_type_full")
    @last_report_type_full.setter
    def last_report_type_full(self, value: str):
        """Set last_report_type_full"""
        self._data["last_report_type_full"] = value

    @property
    def last_report_year(self) -> int:
        """Get last_report_year"""
        return self._data.get("last_report_year")
    @last_report_year.setter
    def last_report_year(self, value: int):
        """Set last_report_year"""
        self._data["last_report_year"] = value

    @property
    def loan_repayments(self) -> float:
        """Get loan_repayments"""
        return self._data.get("loan_repayments")
    @loan_repayments.setter
    def loan_repayments(self, value: float):
        """Set loan_repayments"""
        self._data["loan_repayments"] = value

    @property
    def loan_repayments_candidate_loans(self) -> float:
        """Get loan_repayments_candidate_loans"""
        return self._data.get("loan_repayments_candidate_loans")
    @loan_repayments_candidate_loans.setter
    def loan_repayments_candidate_loans(self, value: float):
        """Set loan_repayments_candidate_loans"""
        self._data["loan_repayments_candidate_loans"] = value

    @property
    def loan_repayments_other_loans(self) -> float:
        """Get loan_repayments_other_loans"""
        return self._data.get("loan_repayments_other_loans")
    @loan_repayments_other_loans.setter
    def loan_repayments_other_loans(self, value: float):
        """Set loan_repayments_other_loans"""
        self._data["loan_repayments_other_loans"] = value

    @property
    def loans(self) -> float:
        """Get loans"""
        return self._data.get("loans")
    @loans.setter
    def loans(self, value: float):
        """Set loans"""
        self._data["loans"] = value

    @property
    def loans_made_by_candidate(self) -> float:
        """Get loans_made_by_candidate"""
        return self._data.get("loans_made_by_candidate")
    @loans_made_by_candidate.setter
    def loans_made_by_candidate(self, value: float):
        """Set loans_made_by_candidate"""
        self._data["loans_made_by_candidate"] = value

    @property
    def net_contributions(self) -> float:
        """Get net_contributions"""
        return self._data.get("net_contributions")
    @net_contributions.setter
    def net_contributions(self, value: float):
        """Set net_contributions"""
        self._data["net_contributions"] = value

    @property
    def net_operating_expenditures(self) -> float:
        """Get net_operating_expenditures"""
        return self._data.get("net_operating_expenditures")
    @net_operating_expenditures.setter
    def net_operating_expenditures(self, value: float):
        """Set net_operating_expenditures"""
        self._data["net_operating_expenditures"] = value

    @property
    def offsets_to_operating_expenditures(self) -> float:
        """Get offsets_to_operating_expenditures"""
        return self._data.get("offsets_to_operating_expenditures")
    @offsets_to_operating_expenditures.setter
    def offsets_to_operating_expenditures(self, value: float):
        """Set offsets_to_operating_expenditures"""
        self._data["offsets_to_operating_expenditures"] = value

    @property
    def operating_expenditures(self) -> float:
        """Get operating_expenditures"""
        return self._data.get("operating_expenditures")
    @operating_expenditures.setter
    def operating_expenditures(self, value: float):
        """Set operating_expenditures"""
        self._data["operating_expenditures"] = value

    @property
    def operating_expenditures_percent(self) -> float:
        """Get operating_expenditures_percent"""
        return self._data.get("operating_expenditures_percent")
    @operating_expenditures_percent.setter
    def operating_expenditures_percent(self, value: float):
        """Set operating_expenditures_percent"""
        self._data["operating_expenditures_percent"] = value

    @property
    def organization_type(self) -> str:
        """Get organization_type"""
        return self._data.get("organization_type")
    @organization_type.setter
    def organization_type(self, value: str):
        """Set organization_type"""
        self._data["organization_type"] = value

    @property
    def organization_type_full(self) -> str:
        """Get organization_type_full"""
        return self._data.get("organization_type_full")
    @organization_type_full.setter
    def organization_type_full(self, value: str):
        """Set organization_type_full"""
        self._data["organization_type_full"] = value

    @property
    def other_disbursements(self) -> float:
        """Get other_disbursements"""
        return self._data.get("other_disbursements")
    @other_disbursements.setter
    def other_disbursements(self, value: float):
        """Set other_disbursements"""
        self._data["other_disbursements"] = value

    @property
    def other_political_committee_contributions(self) -> float:
        """Get other_political_committee_contributions"""
        return self._data.get("other_political_committee_contributions")
    @other_political_committee_contributions.setter
    def other_political_committee_contributions(self, value: float):
        """Set other_political_committee_contributions"""
        self._data["other_political_committee_contributions"] = value

    @property
    def other_receipts(self) -> float:
        """Get other_receipts"""
        return self._data.get("other_receipts")
    @other_receipts.setter
    def other_receipts(self, value: float):
        """Set other_receipts"""
        self._data["other_receipts"] = value

    @property
    def party_and_other_committee_contributions_percent(self) -> float:
        """Get party_and_other_committee_contributions_percent"""
        return self._data.get("party_and_other_committee_contributions_percent")
    @party_and_other_committee_contributions_percent.setter
    def party_and_other_committee_contributions_percent(self, value: float):
        """Set party_and_other_committee_contributions_percent"""
        self._data["party_and_other_committee_contributions_percent"] = value

    @property
    def party_full(self) -> str:
        """Get party_full"""
        return self._data.get("party_full")
    @party_full.setter
    def party_full(self, value: str):
        """Set party_full"""
        self._data["party_full"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def political_party_committee_contributions(self) -> float:
        """Get political_party_committee_contributions"""
        return self._data.get("political_party_committee_contributions")
    @political_party_committee_contributions.setter
    def political_party_committee_contributions(self, value: float):
        """Set political_party_committee_contributions"""
        self._data["political_party_committee_contributions"] = value

    @property
    def receipts(self) -> float:
        """Get receipts"""
        return self._data.get("receipts")
    @receipts.setter
    def receipts(self, value: float):
        """Set receipts"""
        self._data["receipts"] = value

    @property
    def refunded_individual_contributions(self) -> float:
        """Get refunded_individual_contributions"""
        return self._data.get("refunded_individual_contributions")
    @refunded_individual_contributions.setter
    def refunded_individual_contributions(self, value: float):
        """Set refunded_individual_contributions"""
        self._data["refunded_individual_contributions"] = value

    @property
    def refunded_other_political_committee_contributions(self) -> float:
        """Get refunded_other_political_committee_contributions"""
        return self._data.get("refunded_other_political_committee_contributions")
    @refunded_other_political_committee_contributions.setter
    def refunded_other_political_committee_contributions(self, value: float):
        """Set refunded_other_political_committee_contributions"""
        self._data["refunded_other_political_committee_contributions"] = value

    @property
    def refunded_political_party_committee_contributions(self) -> float:
        """Get refunded_political_party_committee_contributions"""
        return self._data.get("refunded_political_party_committee_contributions")
    @refunded_political_party_committee_contributions.setter
    def refunded_political_party_committee_contributions(self, value: float):
        """Set refunded_political_party_committee_contributions"""
        self._data["refunded_political_party_committee_contributions"] = value

    @property
    def report_form(self) -> str:
        """Get report_form"""
        return self._data.get("report_form")
    @report_form.setter
    def report_form(self, value: str):
        """Set report_form"""
        self._data["report_form"] = value

    @property
    def transaction_coverage_date(self) -> str:
        """Get transaction_coverage_date"""
        return self._data.get("transaction_coverage_date")
    @transaction_coverage_date.setter
    def transaction_coverage_date(self, value: str):
        """Set transaction_coverage_date"""
        self._data["transaction_coverage_date"] = value

    @property
    def transfers_from_other_authorized_committee(self) -> float:
        """Get transfers_from_other_authorized_committee"""
        return self._data.get("transfers_from_other_authorized_committee")
    @transfers_from_other_authorized_committee.setter
    def transfers_from_other_authorized_committee(self, value: float):
        """Set transfers_from_other_authorized_committee"""
        self._data["transfers_from_other_authorized_committee"] = value

    @property
    def transfers_to_other_authorized_committee(self) -> float:
        """Get transfers_to_other_authorized_committee"""
        return self._data.get("transfers_to_other_authorized_committee")
    @transfers_to_other_authorized_committee.setter
    def transfers_to_other_authorized_committee(self, value: float):
        """Set transfers_to_other_authorized_committee"""
        self._data["transfers_to_other_authorized_committee"] = value

    @property
    def treasurer_name(self) -> str:
        """Get treasurer_name"""
        return self._data.get("treasurer_name")
    @treasurer_name.setter
    def treasurer_name(self, value: str):
        """Set treasurer_name"""
        self._data["treasurer_name"] = value
