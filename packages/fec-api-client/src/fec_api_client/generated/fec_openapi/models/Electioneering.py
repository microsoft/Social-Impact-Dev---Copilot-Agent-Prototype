from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Electioneering(BaseModel):
    """
    Strongly-typed model class for Electioneering
    
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
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

    @property
    def calculated_candidate_share(self) -> float:
        """Get calculated_candidate_share"""
        return self._data.get("calculated_candidate_share")
    @calculated_candidate_share.setter
    def calculated_candidate_share(self, value: float):
        """Set calculated_candidate_share"""
        self._data["calculated_candidate_share"] = value

    @property
    def candidate_district(self) -> str:
        """Get candidate_district"""
        return self._data.get("candidate_district")
    @candidate_district.setter
    def candidate_district(self, value: str):
        """Set candidate_district"""
        self._data["candidate_district"] = value

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
    def candidate_office(self) -> str:
        """Get candidate_office"""
        return self._data.get("candidate_office")
    @candidate_office.setter
    def candidate_office(self, value: str):
        """Set candidate_office"""
        self._data["candidate_office"] = value

    @property
    def candidate_state(self) -> str:
        """Get candidate_state"""
        return self._data.get("candidate_state")
    @candidate_state.setter
    def candidate_state(self, value: str):
        """Set candidate_state"""
        self._data["candidate_state"] = value

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
    def communication_date(self) -> str:
        """Get communication_date"""
        return self._data.get("communication_date")
    @communication_date.setter
    def communication_date(self, value: str):
        """Set communication_date"""
        self._data["communication_date"] = value

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
    def election_type(self) -> str:
        """Get election_type"""
        return self._data.get("election_type")
    @election_type.setter
    def election_type(self, value: str):
        """Set election_type"""
        self._data["election_type"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def link_id(self) -> int:
        """Get link_id"""
        return self._data.get("link_id")
    @link_id.setter
    def link_id(self, value: int):
        """Set link_id"""
        self._data["link_id"] = value

    @property
    def number_of_candidates(self) -> float:
        """Get number_of_candidates"""
        return self._data.get("number_of_candidates")
    @number_of_candidates.setter
    def number_of_candidates(self, value: float):
        """Set number_of_candidates"""
        self._data["number_of_candidates"] = value

    @property
    def payee_name(self) -> str:
        """Get payee_name"""
        return self._data.get("payee_name")
    @payee_name.setter
    def payee_name(self, value: str):
        """Set payee_name"""
        self._data["payee_name"] = value

    @property
    def payee_state(self) -> str:
        """Get payee_state"""
        return self._data.get("payee_state")
    @payee_state.setter
    def payee_state(self, value: str):
        """Set payee_state"""
        self._data["payee_state"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def public_distribution_date(self) -> str:
        """Get public_distribution_date"""
        return self._data.get("public_distribution_date")
    @public_distribution_date.setter
    def public_distribution_date(self, value: str):
        """Set public_distribution_date"""
        self._data["public_distribution_date"] = value

    @property
    def purpose_description(self) -> str:
        """Get purpose_description"""
        return self._data.get("purpose_description")
    @purpose_description.setter
    def purpose_description(self, value: str):
        """Set purpose_description"""
        self._data["purpose_description"] = value

    @property
    def receipt_date(self) -> str:
        """Get receipt_date"""
        return self._data.get("receipt_date")
    @receipt_date.setter
    def receipt_date(self, value: str):
        """Set receipt_date"""
        self._data["receipt_date"] = value

    @property
    def report_year(self) -> int:
        """Get report_year"""
        return self._data.get("report_year")
    @report_year.setter
    def report_year(self, value: int):
        """Set report_year"""
        self._data["report_year"] = value

    @property
    def sb_image_num(self) -> str:
        """Get sb_image_num"""
        return self._data.get("sb_image_num")
    @sb_image_num.setter
    def sb_image_num(self, value: str):
        """Set sb_image_num"""
        self._data["sb_image_num"] = value

    @property
    def sb_link_id(self) -> str:
        """Get sb_link_id"""
        return self._data.get("sb_link_id")
    @sb_link_id.setter
    def sb_link_id(self, value: str):
        """Set sb_link_id"""
        self._data["sb_link_id"] = value

    @property
    def sub_id(self) -> int:
        """Get sub_id"""
        return self._data.get("sub_id")
    @sub_id.setter
    def sub_id(self, value: int):
        """Set sub_id"""
        self._data["sub_id"] = value
