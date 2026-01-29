from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class Form56(BaseModel):
    """
    Strongly-typed model class for Form56
    
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
    def contribution_amount(self) -> float:
        """Get contribution_amount"""
        return self._data.get("contribution_amount")
    @contribution_amount.setter
    def contribution_amount(self, value: float):
        """Set contribution_amount"""
        self._data["contribution_amount"] = value

    @property
    def contribution_receipt_date(self) -> str:
        """Get contribution_receipt_date"""
        return self._data.get("contribution_receipt_date")
    @contribution_receipt_date.setter
    def contribution_receipt_date(self, value: str):
        """Set contribution_receipt_date"""
        self._data["contribution_receipt_date"] = value

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
    def contributor_type(self) -> str:
        """Get contributor_type"""
        return self._data.get("contributor_type")
    @contributor_type.setter
    def contributor_type(self, value: str):
        """Set contributor_type"""
        self._data["contributor_type"] = value

    @property
    def contributor_type_full(self) -> str:
        """Get contributor_type_full"""
        return self._data.get("contributor_type_full")
    @contributor_type_full.setter
    def contributor_type_full(self, value: str):
        """Set contributor_type_full"""
        self._data["contributor_type_full"] = value

    @property
    def contributor_zip(self) -> str:
        """Get contributor_zip"""
        return self._data.get("contributor_zip")
    @contributor_zip.setter
    def contributor_zip(self, value: str):
        """Set contributor_zip"""
        self._data["contributor_zip"] = value

    @property
    def file_number(self) -> int:
        """Get file_number"""
        return self._data.get("file_number")
    @file_number.setter
    def file_number(self, value: int):
        """Set file_number"""
        self._data["file_number"] = value

    @property
    def filer_name(self) -> str:
        """Get filer_name"""
        return self._data.get("filer_name")
    @filer_name.setter
    def filer_name(self, value: str):
        """Set filer_name"""
        self._data["filer_name"] = value

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
    def original_sub_id(self) -> str:
        """Get original_sub_id"""
        return self._data.get("original_sub_id")
    @original_sub_id.setter
    def original_sub_id(self, value: str):
        """Set original_sub_id"""
        self._data["original_sub_id"] = value

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
