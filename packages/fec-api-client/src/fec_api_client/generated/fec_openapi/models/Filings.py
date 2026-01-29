from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Filings(BaseModel):
    """
    Strongly-typed model class for Filings
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def additional_bank_names(self) -> List[str]:
        """Get additional_bank_names"""
        return self._data.get("additional_bank_names")
    @additional_bank_names.setter
    def additional_bank_names(self, value: List[str]):
        """Set additional_bank_names"""
        self._data["additional_bank_names"] = value

    @property
    def amendment_chain(self) -> List[int]:
        """Get amendment_chain"""
        return self._data.get("amendment_chain")
    @amendment_chain.setter
    def amendment_chain(self, value: List[int]):
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
    def amendment_version(self) -> int:
        """Get amendment_version"""
        return self._data.get("amendment_version")
    @amendment_version.setter
    def amendment_version(self, value: int):
        """Set amendment_version"""
        self._data["amendment_version"] = value

    @property
    def bank_depository_city(self) -> str:
        """Get bank_depository_city"""
        return self._data.get("bank_depository_city")
    @bank_depository_city.setter
    def bank_depository_city(self, value: str):
        """Set bank_depository_city"""
        self._data["bank_depository_city"] = value

    @property
    def bank_depository_name(self) -> str:
        """Get bank_depository_name"""
        return self._data.get("bank_depository_name")
    @bank_depository_name.setter
    def bank_depository_name(self, value: str):
        """Set bank_depository_name"""
        self._data["bank_depository_name"] = value

    @property
    def bank_depository_state(self) -> str:
        """Get bank_depository_state"""
        return self._data.get("bank_depository_state")
    @bank_depository_state.setter
    def bank_depository_state(self, value: str):
        """Set bank_depository_state"""
        self._data["bank_depository_state"] = value

    @property
    def bank_depository_street_1(self) -> str:
        """Get bank_depository_street_1"""
        return self._data.get("bank_depository_street_1")
    @bank_depository_street_1.setter
    def bank_depository_street_1(self, value: str):
        """Set bank_depository_street_1"""
        self._data["bank_depository_street_1"] = value

    @property
    def bank_depository_street_2(self) -> str:
        """Get bank_depository_street_2"""
        return self._data.get("bank_depository_street_2")
    @bank_depository_street_2.setter
    def bank_depository_street_2(self, value: str):
        """Set bank_depository_street_2"""
        self._data["bank_depository_street_2"] = value

    @property
    def bank_depository_zip(self) -> str:
        """Get bank_depository_zip"""
        return self._data.get("bank_depository_zip")
    @bank_depository_zip.setter
    def bank_depository_zip(self, value: str):
        """Set bank_depository_zip"""
        self._data["bank_depository_zip"] = value

    @property
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

    @property
    def candidate_id(self) -> str:
        """Get candidate_id"""
        return self._data.get("candidate_id")
    @candidate_id.setter
    def candidate_id(self, value: str):
        """Set candidate_id"""
        self._data["candidate_id"] = value

    @property
    def candidate_name(self) -> str:
        """Get candidate_name"""
        return self._data.get("candidate_name")
    @candidate_name.setter
    def candidate_name(self, value: str):
        """Set candidate_name"""
        self._data["candidate_name"] = value

    @property
    def cash_on_hand_beginning_period(self) -> float:
        """Get cash_on_hand_beginning_period"""
        return self._data.get("cash_on_hand_beginning_period")
    @cash_on_hand_beginning_period.setter
    def cash_on_hand_beginning_period(self, value: float):
        """Set cash_on_hand_beginning_period"""
        self._data["cash_on_hand_beginning_period"] = value

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
    def document_type(self) -> str:
        """Get document_type"""
        return self._data.get("document_type")
    @document_type.setter
    def document_type(self, value: str):
        """Set document_type"""
        self._data["document_type"] = value

    @property
    def document_type_full(self) -> str:
        """Get document_type_full"""
        return self._data.get("document_type_full")
    @document_type_full.setter
    def document_type_full(self, value: str):
        """Set document_type_full"""
        self._data["document_type_full"] = value

    @property
    def election_year(self) -> int:
        """Get election_year"""
        return self._data.get("election_year")
    @election_year.setter
    def election_year(self, value: int):
        """Set election_year"""
        self._data["election_year"] = value

    @property
    def ending_image_number(self) -> str:
        """Get ending_image_number"""
        return self._data.get("ending_image_number")
    @ending_image_number.setter
    def ending_image_number(self, value: str):
        """Set ending_image_number"""
        self._data["ending_image_number"] = value

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
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def form_category(self) -> str:
        """Get form_category"""
        return self._data.get("form_category")
    @form_category.setter
    def form_category(self, value: str):
        """Set form_category"""
        self._data["form_category"] = value

    @property
    def form_type(self) -> str:
        """Get form_type"""
        return self._data.get("form_type")
    @form_type.setter
    def form_type(self, value: str):
        """Set form_type"""
        self._data["form_type"] = value

    @property
    def house_personal_funds(self) -> float:
        """Get house_personal_funds"""
        return self._data.get("house_personal_funds")
    @house_personal_funds.setter
    def house_personal_funds(self, value: float):
        """Set house_personal_funds"""
        self._data["house_personal_funds"] = value

    @property
    def html_url(self) -> str:
        """Get html_url"""
        return self._data.get("html_url")
    @html_url.setter
    def html_url(self, value: str):
        """Set html_url"""
        self._data["html_url"] = value

    @property
    def is_amended(self) -> bool:
        """Get is_amended"""
        return self._data.get("is_amended")
    @is_amended.setter
    def is_amended(self, value: bool):
        """Set is_amended"""
        self._data["is_amended"] = value

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
    def most_recent_file_number(self) -> int:
        """Get most_recent_file_number"""
        return self._data.get("most_recent_file_number")
    @most_recent_file_number.setter
    def most_recent_file_number(self, value: int):
        """Set most_recent_file_number"""
        self._data["most_recent_file_number"] = value

    @property
    def net_donations(self) -> float:
        """Get net_donations"""
        return self._data.get("net_donations")
    @net_donations.setter
    def net_donations(self, value: float):
        """Set net_donations"""
        self._data["net_donations"] = value

    @property
    def office(self) -> str:
        """Get office"""
        return self._data.get("office")
    @office.setter
    def office(self, value: str):
        """Set office"""
        self._data["office"] = value

    @property
    def opposition_personal_funds(self) -> float:
        """Get opposition_personal_funds"""
        return self._data.get("opposition_personal_funds")
    @opposition_personal_funds.setter
    def opposition_personal_funds(self, value: float):
        """Set opposition_personal_funds"""
        self._data["opposition_personal_funds"] = value

    @property
    def pages(self) -> int:
        """Get pages"""
        return self._data.get("pages")
    @pages.setter
    def pages(self, value: int):
        """Set pages"""
        self._data["pages"] = value

    @property
    def party(self) -> str:
        """Get party"""
        return self._data.get("party")
    @party.setter
    def party(self, value: str):
        """Set party"""
        self._data["party"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def previous_file_number(self) -> int:
        """Get previous_file_number"""
        return self._data.get("previous_file_number")
    @previous_file_number.setter
    def previous_file_number(self, value: int):
        """Set previous_file_number"""
        self._data["previous_file_number"] = value

    @property
    def primary_general_indicator(self) -> str:
        """Get primary_general_indicator"""
        return self._data.get("primary_general_indicator")
    @primary_general_indicator.setter
    def primary_general_indicator(self, value: str):
        """Set primary_general_indicator"""
        self._data["primary_general_indicator"] = value

    @property
    def receipt_date(self) -> str:
        """Get receipt_date"""
        return self._data.get("receipt_date")
    @receipt_date.setter
    def receipt_date(self, value: str):
        """Set receipt_date"""
        self._data["receipt_date"] = value

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
    def request_type(self) -> str:
        """Get request_type"""
        return self._data.get("request_type")
    @request_type.setter
    def request_type(self, value: str):
        """Set request_type"""
        self._data["request_type"] = value

    @property
    def senate_personal_funds(self) -> float:
        """Get senate_personal_funds"""
        return self._data.get("senate_personal_funds")
    @senate_personal_funds.setter
    def senate_personal_funds(self, value: float):
        """Set senate_personal_funds"""
        self._data["senate_personal_funds"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

    @property
    def sub_id(self) -> str:
        """Get sub_id"""
        return self._data.get("sub_id")
    @sub_id.setter
    def sub_id(self, value: str):
        """Set sub_id"""
        self._data["sub_id"] = value

    @property
    def total_communication_cost(self) -> float:
        """Get total_communication_cost"""
        return self._data.get("total_communication_cost")
    @total_communication_cost.setter
    def total_communication_cost(self, value: float):
        """Set total_communication_cost"""
        self._data["total_communication_cost"] = value

    @property
    def total_disbursements(self) -> float:
        """Get total_disbursements"""
        return self._data.get("total_disbursements")
    @total_disbursements.setter
    def total_disbursements(self, value: float):
        """Set total_disbursements"""
        self._data["total_disbursements"] = value

    @property
    def total_independent_expenditures(self) -> float:
        """Get total_independent_expenditures"""
        return self._data.get("total_independent_expenditures")
    @total_independent_expenditures.setter
    def total_independent_expenditures(self, value: float):
        """Set total_independent_expenditures"""
        self._data["total_independent_expenditures"] = value

    @property
    def total_individual_contributions(self) -> float:
        """Get total_individual_contributions"""
        return self._data.get("total_individual_contributions")
    @total_individual_contributions.setter
    def total_individual_contributions(self, value: float):
        """Set total_individual_contributions"""
        self._data["total_individual_contributions"] = value

    @property
    def total_receipts(self) -> float:
        """Get total_receipts"""
        return self._data.get("total_receipts")
    @total_receipts.setter
    def total_receipts(self, value: float):
        """Set total_receipts"""
        self._data["total_receipts"] = value

    @property
    def treasurer_name(self) -> str:
        """Get treasurer_name"""
        return self._data.get("treasurer_name")
    @treasurer_name.setter
    def treasurer_name(self, value: str):
        """Set treasurer_name"""
        self._data["treasurer_name"] = value

    @property
    def update_date(self) -> str:
        """Get update_date"""
        return self._data.get("update_date")
    @update_date.setter
    def update_date(self, value: str):
        """Set update_date"""
        self._data["update_date"] = value
