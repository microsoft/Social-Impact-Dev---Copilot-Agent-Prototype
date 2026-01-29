from __future__ import annotations

from typing import List, Union, Optional, Dict, Any, TYPE_CHECKING

if TYPE_CHECKING:
    from .PacSponsorCandidate import PacSponsorCandidate

from ..base.base_model import BaseModel


class CommitteeTotalsPacParty(BaseModel):
    """
    Strongly-typed model class for CommitteeTotalsPacParty
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def all_loans_received(self) -> float:
        """Get all_loans_received"""
        return self._data.get("all_loans_received")
    @all_loans_received.setter
    def all_loans_received(self, value: float):
        """Set all_loans_received"""
        self._data["all_loans_received"] = value

    @property
    def allocated_federal_election_levin_share(self) -> float:
        """Get allocated_federal_election_levin_share"""
        return self._data.get("allocated_federal_election_levin_share")
    @allocated_federal_election_levin_share.setter
    def allocated_federal_election_levin_share(self, value: float):
        """Set allocated_federal_election_levin_share"""
        self._data["allocated_federal_election_levin_share"] = value

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
    def convention_exp(self) -> float:
        """Get convention_exp"""
        return self._data.get("convention_exp")
    @convention_exp.setter
    def convention_exp(self, value: float):
        """Set convention_exp"""
        self._data["convention_exp"] = value

    @property
    def coordinated_expenditures_by_party_committee(self) -> float:
        """Get coordinated_expenditures_by_party_committee"""
        return self._data.get("coordinated_expenditures_by_party_committee")
    @coordinated_expenditures_by_party_committee.setter
    def coordinated_expenditures_by_party_committee(self, value: float):
        """Set coordinated_expenditures_by_party_committee"""
        self._data["coordinated_expenditures_by_party_committee"] = value

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
    def exp_prior_years_subject_limits(self) -> float:
        """Get exp_prior_years_subject_limits"""
        return self._data.get("exp_prior_years_subject_limits")
    @exp_prior_years_subject_limits.setter
    def exp_prior_years_subject_limits(self, value: float):
        """Set exp_prior_years_subject_limits"""
        self._data["exp_prior_years_subject_limits"] = value

    @property
    def exp_subject_limits(self) -> float:
        """Get exp_subject_limits"""
        return self._data.get("exp_subject_limits")
    @exp_subject_limits.setter
    def exp_subject_limits(self, value: float):
        """Set exp_subject_limits"""
        self._data["exp_subject_limits"] = value

    @property
    def fed_candidate_committee_contributions(self) -> float:
        """Get fed_candidate_committee_contributions"""
        return self._data.get("fed_candidate_committee_contributions")
    @fed_candidate_committee_contributions.setter
    def fed_candidate_committee_contributions(self, value: float):
        """Set fed_candidate_committee_contributions"""
        self._data["fed_candidate_committee_contributions"] = value

    @property
    def fed_candidate_contribution_refunds(self) -> float:
        """Get fed_candidate_contribution_refunds"""
        return self._data.get("fed_candidate_contribution_refunds")
    @fed_candidate_contribution_refunds.setter
    def fed_candidate_contribution_refunds(self, value: float):
        """Set fed_candidate_contribution_refunds"""
        self._data["fed_candidate_contribution_refunds"] = value

    @property
    def fed_disbursements(self) -> float:
        """Get fed_disbursements"""
        return self._data.get("fed_disbursements")
    @fed_disbursements.setter
    def fed_disbursements(self, value: float):
        """Set fed_disbursements"""
        self._data["fed_disbursements"] = value

    @property
    def fed_election_activity(self) -> float:
        """Get fed_election_activity"""
        return self._data.get("fed_election_activity")
    @fed_election_activity.setter
    def fed_election_activity(self, value: float):
        """Set fed_election_activity"""
        self._data["fed_election_activity"] = value

    @property
    def fed_operating_expenditures(self) -> float:
        """Get fed_operating_expenditures"""
        return self._data.get("fed_operating_expenditures")
    @fed_operating_expenditures.setter
    def fed_operating_expenditures(self, value: float):
        """Set fed_operating_expenditures"""
        self._data["fed_operating_expenditures"] = value

    @property
    def fed_receipts(self) -> float:
        """Get fed_receipts"""
        return self._data.get("fed_receipts")
    @fed_receipts.setter
    def fed_receipts(self, value: float):
        """Set fed_receipts"""
        self._data["fed_receipts"] = value

    @property
    def federal_funds(self) -> float:
        """Get federal_funds"""
        return self._data.get("federal_funds")
    @federal_funds.setter
    def federal_funds(self, value: float):
        """Set federal_funds"""
        self._data["federal_funds"] = value

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
    def independent_expenditures(self) -> float:
        """Get independent_expenditures"""
        return self._data.get("independent_expenditures")
    @independent_expenditures.setter
    def independent_expenditures(self, value: float):
        """Set independent_expenditures"""
        self._data["independent_expenditures"] = value

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
    def itemized_convention_exp(self) -> float:
        """Get itemized_convention_exp"""
        return self._data.get("itemized_convention_exp")
    @itemized_convention_exp.setter
    def itemized_convention_exp(self, value: float):
        """Set itemized_convention_exp"""
        self._data["itemized_convention_exp"] = value

    @property
    def itemized_other_disb(self) -> float:
        """Get itemized_other_disb"""
        return self._data.get("itemized_other_disb")
    @itemized_other_disb.setter
    def itemized_other_disb(self, value: float):
        """Set itemized_other_disb"""
        self._data["itemized_other_disb"] = value

    @property
    def itemized_other_income(self) -> float:
        """Get itemized_other_income"""
        return self._data.get("itemized_other_income")
    @itemized_other_income.setter
    def itemized_other_income(self, value: float):
        """Set itemized_other_income"""
        self._data["itemized_other_income"] = value

    @property
    def itemized_other_refunds(self) -> float:
        """Get itemized_other_refunds"""
        return self._data.get("itemized_other_refunds")
    @itemized_other_refunds.setter
    def itemized_other_refunds(self, value: float):
        """Set itemized_other_refunds"""
        self._data["itemized_other_refunds"] = value

    @property
    def itemized_refunds_relating_convention_exp(self) -> float:
        """Get itemized_refunds_relating_convention_exp"""
        return self._data.get("itemized_refunds_relating_convention_exp")
    @itemized_refunds_relating_convention_exp.setter
    def itemized_refunds_relating_convention_exp(self, value: float):
        """Set itemized_refunds_relating_convention_exp"""
        self._data["itemized_refunds_relating_convention_exp"] = value

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
    def loan_repayments_made(self) -> float:
        """Get loan_repayments_made"""
        return self._data.get("loan_repayments_made")
    @loan_repayments_made.setter
    def loan_repayments_made(self, value: float):
        """Set loan_repayments_made"""
        self._data["loan_repayments_made"] = value

    @property
    def loan_repayments_received(self) -> float:
        """Get loan_repayments_received"""
        return self._data.get("loan_repayments_received")
    @loan_repayments_received.setter
    def loan_repayments_received(self, value: float):
        """Set loan_repayments_received"""
        self._data["loan_repayments_received"] = value

    @property
    def loans_and_loan_repayments_made(self) -> float:
        """Get loans_and_loan_repayments_made"""
        return self._data.get("loans_and_loan_repayments_made")
    @loans_and_loan_repayments_made.setter
    def loans_and_loan_repayments_made(self, value: float):
        """Set loans_and_loan_repayments_made"""
        self._data["loans_and_loan_repayments_made"] = value

    @property
    def loans_and_loan_repayments_received(self) -> float:
        """Get loans_and_loan_repayments_received"""
        return self._data.get("loans_and_loan_repayments_received")
    @loans_and_loan_repayments_received.setter
    def loans_and_loan_repayments_received(self, value: float):
        """Set loans_and_loan_repayments_received"""
        self._data["loans_and_loan_repayments_received"] = value

    @property
    def loans_made(self) -> float:
        """Get loans_made"""
        return self._data.get("loans_made")
    @loans_made.setter
    def loans_made(self, value: float):
        """Set loans_made"""
        self._data["loans_made"] = value

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
    def non_allocated_fed_election_activity(self) -> float:
        """Get non_allocated_fed_election_activity"""
        return self._data.get("non_allocated_fed_election_activity")
    @non_allocated_fed_election_activity.setter
    def non_allocated_fed_election_activity(self, value: float):
        """Set non_allocated_fed_election_activity"""
        self._data["non_allocated_fed_election_activity"] = value

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
    def other_fed_operating_expenditures(self) -> float:
        """Get other_fed_operating_expenditures"""
        return self._data.get("other_fed_operating_expenditures")
    @other_fed_operating_expenditures.setter
    def other_fed_operating_expenditures(self, value: float):
        """Set other_fed_operating_expenditures"""
        self._data["other_fed_operating_expenditures"] = value

    @property
    def other_fed_receipts(self) -> float:
        """Get other_fed_receipts"""
        return self._data.get("other_fed_receipts")
    @other_fed_receipts.setter
    def other_fed_receipts(self, value: float):
        """Set other_fed_receipts"""
        self._data["other_fed_receipts"] = value

    @property
    def other_political_committee_contributions(self) -> float:
        """Get other_political_committee_contributions"""
        return self._data.get("other_political_committee_contributions")
    @other_political_committee_contributions.setter
    def other_political_committee_contributions(self, value: float):
        """Set other_political_committee_contributions"""
        self._data["other_political_committee_contributions"] = value

    @property
    def other_refunds(self) -> float:
        """Get other_refunds"""
        return self._data.get("other_refunds")
    @other_refunds.setter
    def other_refunds(self, value: float):
        """Set other_refunds"""
        self._data["other_refunds"] = value

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
    def refunds_relating_convention_exp(self) -> float:
        """Get refunds_relating_convention_exp"""
        return self._data.get("refunds_relating_convention_exp")
    @refunds_relating_convention_exp.setter
    def refunds_relating_convention_exp(self, value: float):
        """Set refunds_relating_convention_exp"""
        self._data["refunds_relating_convention_exp"] = value

    @property
    def report_form(self) -> str:
        """Get report_form"""
        return self._data.get("report_form")
    @report_form.setter
    def report_form(self, value: str):
        """Set report_form"""
        self._data["report_form"] = value

    @property
    def shared_fed_activity(self) -> float:
        """Get shared_fed_activity"""
        return self._data.get("shared_fed_activity")
    @shared_fed_activity.setter
    def shared_fed_activity(self, value: float):
        """Set shared_fed_activity"""
        self._data["shared_fed_activity"] = value

    @property
    def shared_fed_activity_nonfed(self) -> float:
        """Get shared_fed_activity_nonfed"""
        return self._data.get("shared_fed_activity_nonfed")
    @shared_fed_activity_nonfed.setter
    def shared_fed_activity_nonfed(self, value: float):
        """Set shared_fed_activity_nonfed"""
        self._data["shared_fed_activity_nonfed"] = value

    @property
    def shared_fed_operating_expenditures(self) -> float:
        """Get shared_fed_operating_expenditures"""
        return self._data.get("shared_fed_operating_expenditures")
    @shared_fed_operating_expenditures.setter
    def shared_fed_operating_expenditures(self, value: float):
        """Set shared_fed_operating_expenditures"""
        self._data["shared_fed_operating_expenditures"] = value

    @property
    def shared_nonfed_operating_expenditures(self) -> float:
        """Get shared_nonfed_operating_expenditures"""
        return self._data.get("shared_nonfed_operating_expenditures")
    @shared_nonfed_operating_expenditures.setter
    def shared_nonfed_operating_expenditures(self, value: float):
        """Set shared_nonfed_operating_expenditures"""
        self._data["shared_nonfed_operating_expenditures"] = value

    @property
    def sponsor_candidate_ids(self) -> List[str]:
        """Get sponsor_candidate_ids"""
        return self._data.get("sponsor_candidate_ids")
    @sponsor_candidate_ids.setter
    def sponsor_candidate_ids(self, value: List[str]):
        """Set sponsor_candidate_ids"""
        self._data["sponsor_candidate_ids"] = value

    @property
    def sponsor_candidate_list(self) -> List['PacSponsorCandidate']:
        """Get sponsor_candidate_list"""
        return self._data.get("sponsor_candidate_list")
    @sponsor_candidate_list.setter
    def sponsor_candidate_list(self, value: List['PacSponsorCandidate']):
        """Set sponsor_candidate_list"""
        self._data["sponsor_candidate_list"] = value

    @property
    def total_exp_subject_limits(self) -> float:
        """Get total_exp_subject_limits"""
        return self._data.get("total_exp_subject_limits")
    @total_exp_subject_limits.setter
    def total_exp_subject_limits(self, value: float):
        """Set total_exp_subject_limits"""
        self._data["total_exp_subject_limits"] = value

    @property
    def total_transfers(self) -> float:
        """Get total_transfers"""
        return self._data.get("total_transfers")
    @total_transfers.setter
    def total_transfers(self, value: float):
        """Set total_transfers"""
        self._data["total_transfers"] = value

    @property
    def transaction_coverage_date(self) -> str:
        """Get transaction_coverage_date"""
        return self._data.get("transaction_coverage_date")
    @transaction_coverage_date.setter
    def transaction_coverage_date(self, value: str):
        """Set transaction_coverage_date"""
        self._data["transaction_coverage_date"] = value

    @property
    def transfers_from_affiliated_party(self) -> float:
        """Get transfers_from_affiliated_party"""
        return self._data.get("transfers_from_affiliated_party")
    @transfers_from_affiliated_party.setter
    def transfers_from_affiliated_party(self, value: float):
        """Set transfers_from_affiliated_party"""
        self._data["transfers_from_affiliated_party"] = value

    @property
    def transfers_from_nonfed_account(self) -> float:
        """Get transfers_from_nonfed_account"""
        return self._data.get("transfers_from_nonfed_account")
    @transfers_from_nonfed_account.setter
    def transfers_from_nonfed_account(self, value: float):
        """Set transfers_from_nonfed_account"""
        self._data["transfers_from_nonfed_account"] = value

    @property
    def transfers_from_nonfed_levin(self) -> float:
        """Get transfers_from_nonfed_levin"""
        return self._data.get("transfers_from_nonfed_levin")
    @transfers_from_nonfed_levin.setter
    def transfers_from_nonfed_levin(self, value: float):
        """Set transfers_from_nonfed_levin"""
        self._data["transfers_from_nonfed_levin"] = value

    @property
    def transfers_to_affiliated_committee(self) -> float:
        """Get transfers_to_affiliated_committee"""
        return self._data.get("transfers_to_affiliated_committee")
    @transfers_to_affiliated_committee.setter
    def transfers_to_affiliated_committee(self, value: float):
        """Set transfers_to_affiliated_committee"""
        self._data["transfers_to_affiliated_committee"] = value

    @property
    def treasurer_name(self) -> str:
        """Get treasurer_name"""
        return self._data.get("treasurer_name")
    @treasurer_name.setter
    def treasurer_name(self, value: str):
        """Set treasurer_name"""
        self._data["treasurer_name"] = value

    @property
    def unitemized_convention_exp(self) -> float:
        """Get unitemized_convention_exp"""
        return self._data.get("unitemized_convention_exp")
    @unitemized_convention_exp.setter
    def unitemized_convention_exp(self, value: float):
        """Set unitemized_convention_exp"""
        self._data["unitemized_convention_exp"] = value

    @property
    def unitemized_other_disb(self) -> float:
        """Get unitemized_other_disb"""
        return self._data.get("unitemized_other_disb")
    @unitemized_other_disb.setter
    def unitemized_other_disb(self, value: float):
        """Set unitemized_other_disb"""
        self._data["unitemized_other_disb"] = value

    @property
    def unitemized_other_income(self) -> float:
        """Get unitemized_other_income"""
        return self._data.get("unitemized_other_income")
    @unitemized_other_income.setter
    def unitemized_other_income(self, value: float):
        """Set unitemized_other_income"""
        self._data["unitemized_other_income"] = value

    @property
    def unitemized_other_refunds(self) -> float:
        """Get unitemized_other_refunds"""
        return self._data.get("unitemized_other_refunds")
    @unitemized_other_refunds.setter
    def unitemized_other_refunds(self, value: float):
        """Set unitemized_other_refunds"""
        self._data["unitemized_other_refunds"] = value

    @property
    def unitemized_refunds_relating_convention_exp(self) -> float:
        """Get unitemized_refunds_relating_convention_exp"""
        return self._data.get("unitemized_refunds_relating_convention_exp")
    @unitemized_refunds_relating_convention_exp.setter
    def unitemized_refunds_relating_convention_exp(self, value: float):
        """Set unitemized_refunds_relating_convention_exp"""
        self._data["unitemized_refunds_relating_convention_exp"] = value
