from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class CommitteeTotalsIEOnly(BaseModel):
    """
    Strongly-typed model class for CommitteeTotalsIEOnly
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def committee_id(self) -> str:
        """Get committee_id"""
        return self._data.get("committee_id")
    @committee_id.setter
    def committee_id(self, value: str):
        """Set committee_id"""
        self._data["committee_id"] = value

    @property
    def committee_state(self) -> str:
        """Get committee_state"""
        return self._data.get("committee_state")
    @committee_state.setter
    def committee_state(self, value: str):
        """Set committee_state"""
        self._data["committee_state"] = value

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
    def first_file_date(self) -> str:
        """Get first_file_date"""
        return self._data.get("first_file_date")
    @first_file_date.setter
    def first_file_date(self, value: str):
        """Set first_file_date"""
        self._data["first_file_date"] = value

    @property
    def individual_contributions_percent(self) -> float:
        """Get individual_contributions_percent"""
        return self._data.get("individual_contributions_percent")
    @individual_contributions_percent.setter
    def individual_contributions_percent(self, value: float):
        """Set individual_contributions_percent"""
        self._data["individual_contributions_percent"] = value

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
    def operating_expenditures_percent(self) -> float:
        """Get operating_expenditures_percent"""
        return self._data.get("operating_expenditures_percent")
    @operating_expenditures_percent.setter
    def operating_expenditures_percent(self, value: float):
        """Set operating_expenditures_percent"""
        self._data["operating_expenditures_percent"] = value

    @property
    def party_and_other_committee_contributions_percent(self) -> float:
        """Get party_and_other_committee_contributions_percent"""
        return self._data.get("party_and_other_committee_contributions_percent")
    @party_and_other_committee_contributions_percent.setter
    def party_and_other_committee_contributions_percent(self, value: float):
        """Set party_and_other_committee_contributions_percent"""
        self._data["party_and_other_committee_contributions_percent"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def report_form(self) -> str:
        """Get report_form"""
        return self._data.get("report_form")
    @report_form.setter
    def report_form(self, value: str):
        """Set report_form"""
        self._data["report_form"] = value

    @property
    def total_independent_contributions(self) -> float:
        """Get total_independent_contributions"""
        return self._data.get("total_independent_contributions")
    @total_independent_contributions.setter
    def total_independent_contributions(self, value: float):
        """Set total_independent_contributions"""
        self._data["total_independent_contributions"] = value

    @property
    def total_independent_expenditures(self) -> float:
        """Get total_independent_expenditures"""
        return self._data.get("total_independent_expenditures")
    @total_independent_expenditures.setter
    def total_independent_expenditures(self, value: float):
        """Set total_independent_expenditures"""
        self._data["total_independent_expenditures"] = value

    @property
    def transaction_coverage_date(self) -> str:
        """Get transaction_coverage_date"""
        return self._data.get("transaction_coverage_date")
    @transaction_coverage_date.setter
    def transaction_coverage_date(self, value: str):
        """Set transaction_coverage_date"""
        self._data["transaction_coverage_date"] = value
