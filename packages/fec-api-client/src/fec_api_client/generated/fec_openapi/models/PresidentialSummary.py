from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class PresidentialSummary(BaseModel):
    """
    Strongly-typed model class for PresidentialSummary
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def candidate_contributions_less_repayments(self) -> float:
        """Get candidate_contributions_less_repayments"""
        return self._data.get("candidate_contributions_less_repayments")
    @candidate_contributions_less_repayments.setter
    def candidate_contributions_less_repayments(self, value: float):
        """Set candidate_contributions_less_repayments"""
        self._data["candidate_contributions_less_repayments"] = value

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
    def candidate_name(self) -> str:
        """Get candidate_name"""
        return self._data.get("candidate_name")
    @candidate_name.setter
    def candidate_name(self, value: str):
        """Set candidate_name"""
        self._data["candidate_name"] = value

    @property
    def candidate_party_affiliation(self) -> str:
        """Get candidate_party_affiliation"""
        return self._data.get("candidate_party_affiliation")
    @candidate_party_affiliation.setter
    def candidate_party_affiliation(self, value: str):
        """Set candidate_party_affiliation"""
        self._data["candidate_party_affiliation"] = value

    @property
    def cash_on_hand_end(self) -> float:
        """Get cash_on_hand_end"""
        return self._data.get("cash_on_hand_end")
    @cash_on_hand_end.setter
    def cash_on_hand_end(self, value: float):
        """Set cash_on_hand_end"""
        self._data["cash_on_hand_end"] = value

    @property
    def committee_designation(self) -> str:
        """Get committee_designation"""
        return self._data.get("committee_designation")
    @committee_designation.setter
    def committee_designation(self, value: str):
        """Set committee_designation"""
        self._data["committee_designation"] = value

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
    def debts_owed_by_committee(self) -> float:
        """Get debts_owed_by_committee"""
        return self._data.get("debts_owed_by_committee")
    @debts_owed_by_committee.setter
    def debts_owed_by_committee(self, value: float):
        """Set debts_owed_by_committee"""
        self._data["debts_owed_by_committee"] = value

    @property
    def disbursements_less_offsets(self) -> float:
        """Get disbursements_less_offsets"""
        return self._data.get("disbursements_less_offsets")
    @disbursements_less_offsets.setter
    def disbursements_less_offsets(self, value: float):
        """Set disbursements_less_offsets"""
        self._data["disbursements_less_offsets"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

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
    def individual_contributions_less_refunds(self) -> float:
        """Get individual_contributions_less_refunds"""
        return self._data.get("individual_contributions_less_refunds")
    @individual_contributions_less_refunds.setter
    def individual_contributions_less_refunds(self, value: float):
        """Set individual_contributions_less_refunds"""
        self._data["individual_contributions_less_refunds"] = value

    @property
    def net_receipts(self) -> float:
        """Get net_receipts"""
        return self._data.get("net_receipts")
    @net_receipts.setter
    def net_receipts(self, value: float):
        """Set net_receipts"""
        self._data["net_receipts"] = value

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
    def pac_contributions_less_refunds(self) -> float:
        """Get pac_contributions_less_refunds"""
        return self._data.get("pac_contributions_less_refunds")
    @pac_contributions_less_refunds.setter
    def pac_contributions_less_refunds(self, value: float):
        """Set pac_contributions_less_refunds"""
        self._data["pac_contributions_less_refunds"] = value

    @property
    def party_contributions_less_refunds(self) -> float:
        """Get party_contributions_less_refunds"""
        return self._data.get("party_contributions_less_refunds")
    @party_contributions_less_refunds.setter
    def party_contributions_less_refunds(self, value: float):
        """Set party_contributions_less_refunds"""
        self._data["party_contributions_less_refunds"] = value

    @property
    def repayments_loans_made_by_candidate(self) -> float:
        """Get repayments_loans_made_by_candidate"""
        return self._data.get("repayments_loans_made_by_candidate")
    @repayments_loans_made_by_candidate.setter
    def repayments_loans_made_by_candidate(self, value: float):
        """Set repayments_loans_made_by_candidate"""
        self._data["repayments_loans_made_by_candidate"] = value

    @property
    def repayments_other_loans(self) -> float:
        """Get repayments_other_loans"""
        return self._data.get("repayments_other_loans")
    @repayments_other_loans.setter
    def repayments_other_loans(self, value: float):
        """Set repayments_other_loans"""
        self._data["repayments_other_loans"] = value

    @property
    def rounded_net_receipts(self) -> float:
        """Get rounded_net_receipts"""
        return self._data.get("rounded_net_receipts")
    @rounded_net_receipts.setter
    def rounded_net_receipts(self, value: float):
        """Set rounded_net_receipts"""
        self._data["rounded_net_receipts"] = value

    @property
    def total_contribution_refunds(self) -> float:
        """Get total_contribution_refunds"""
        return self._data.get("total_contribution_refunds")
    @total_contribution_refunds.setter
    def total_contribution_refunds(self, value: float):
        """Set total_contribution_refunds"""
        self._data["total_contribution_refunds"] = value

    @property
    def total_loan_repayments_made(self) -> float:
        """Get total_loan_repayments_made"""
        return self._data.get("total_loan_repayments_made")
    @total_loan_repayments_made.setter
    def total_loan_repayments_made(self, value: float):
        """Set total_loan_repayments_made"""
        self._data["total_loan_repayments_made"] = value

    @property
    def transfers_from_affiliated_committees(self) -> float:
        """Get transfers_from_affiliated_committees"""
        return self._data.get("transfers_from_affiliated_committees")
    @transfers_from_affiliated_committees.setter
    def transfers_from_affiliated_committees(self, value: float):
        """Set transfers_from_affiliated_committees"""
        self._data["transfers_from_affiliated_committees"] = value

    @property
    def transfers_to_other_authorized_committees(self) -> float:
        """Get transfers_to_other_authorized_committees"""
        return self._data.get("transfers_to_other_authorized_committees")
    @transfers_to_other_authorized_committees.setter
    def transfers_to_other_authorized_committees(self, value: float):
        """Set transfers_to_other_authorized_committees"""
        self._data["transfers_to_other_authorized_committees"] = value
