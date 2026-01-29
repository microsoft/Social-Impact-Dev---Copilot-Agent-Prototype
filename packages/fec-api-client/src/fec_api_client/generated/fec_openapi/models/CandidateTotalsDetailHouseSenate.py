from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CandidateTotalsDetailHouseSenate(BaseModel):
    """
    Strongly-typed model class for CandidateTotalsDetailHouseSenate
    
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
    def candidate_election_year(self) -> int:
        """Get candidate_election_year"""
        return self._data.get("candidate_election_year")
    @candidate_election_year.setter
    def candidate_election_year(self, value: int):
        """Set candidate_election_year"""
        self._data["candidate_election_year"] = value

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

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
    def election_full(self) -> bool:
        """Get election_full"""
        return self._data.get("election_full")
    @election_full.setter
    def election_full(self, value: bool):
        """Set election_full"""
        self._data["election_full"] = value

    @property
    def exempt_legal_accounting_disbursement(self) -> float:
        """Get exempt_legal_accounting_disbursement"""
        return self._data.get("exempt_legal_accounting_disbursement")
    @exempt_legal_accounting_disbursement.setter
    def exempt_legal_accounting_disbursement(self, value: float):
        """Set exempt_legal_accounting_disbursement"""
        self._data["exempt_legal_accounting_disbursement"] = value

    @property
    def federal_funds(self) -> float:
        """Get federal_funds"""
        return self._data.get("federal_funds")
    @federal_funds.setter
    def federal_funds(self, value: float):
        """Set federal_funds"""
        self._data["federal_funds"] = value

    @property
    def fundraising_disbursements(self) -> float:
        """Get fundraising_disbursements"""
        return self._data.get("fundraising_disbursements")
    @fundraising_disbursements.setter
    def fundraising_disbursements(self, value: float):
        """Set fundraising_disbursements"""
        self._data["fundraising_disbursements"] = value

    @property
    def individual_contributions(self) -> float:
        """Get individual_contributions"""
        return self._data.get("individual_contributions")
    @individual_contributions.setter
    def individual_contributions(self, value: float):
        """Set individual_contributions"""
        self._data["individual_contributions"] = value

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
    def last_net_contributions(self) -> float:
        """Get last_net_contributions"""
        return self._data.get("last_net_contributions")
    @last_net_contributions.setter
    def last_net_contributions(self, value: float):
        """Set last_net_contributions"""
        self._data["last_net_contributions"] = value

    @property
    def last_net_operating_expenditures(self) -> float:
        """Get last_net_operating_expenditures"""
        return self._data.get("last_net_operating_expenditures")
    @last_net_operating_expenditures.setter
    def last_net_operating_expenditures(self, value: float):
        """Set last_net_operating_expenditures"""
        self._data["last_net_operating_expenditures"] = value

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
    def offsets_to_fundraising_expenditures(self) -> float:
        """Get offsets_to_fundraising_expenditures"""
        return self._data.get("offsets_to_fundraising_expenditures")
    @offsets_to_fundraising_expenditures.setter
    def offsets_to_fundraising_expenditures(self, value: float):
        """Set offsets_to_fundraising_expenditures"""
        self._data["offsets_to_fundraising_expenditures"] = value

    @property
    def offsets_to_legal_accounting(self) -> float:
        """Get offsets_to_legal_accounting"""
        return self._data.get("offsets_to_legal_accounting")
    @offsets_to_legal_accounting.setter
    def offsets_to_legal_accounting(self, value: float):
        """Set offsets_to_legal_accounting"""
        self._data["offsets_to_legal_accounting"] = value

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
    def total_offsets_to_operating_expenditures(self) -> float:
        """Get total_offsets_to_operating_expenditures"""
        return self._data.get("total_offsets_to_operating_expenditures")
    @total_offsets_to_operating_expenditures.setter
    def total_offsets_to_operating_expenditures(self, value: float):
        """Set total_offsets_to_operating_expenditures"""
        self._data["total_offsets_to_operating_expenditures"] = value

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
