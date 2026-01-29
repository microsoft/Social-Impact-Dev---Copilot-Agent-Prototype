from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class EFilings(BaseModel):
    """
    Strongly-typed model class for EFilings
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def amended_by(self) -> int:
        """Get amended_by"""
        return self._data.get("amended_by")
    @amended_by.setter
    def amended_by(self, value: int):
        """Set amended_by"""
        self._data["amended_by"] = value

    @property
    def amendment_chain(self) -> List[int]:
        """Get amendment_chain"""
        return self._data.get("amendment_chain")
    @amendment_chain.setter
    def amendment_chain(self, value: List[int]):
        """Set amendment_chain"""
        self._data["amendment_chain"] = value

    @property
    def amendment_number(self) -> int:
        """Get amendment_number"""
        return self._data.get("amendment_number")
    @amendment_number.setter
    def amendment_number(self, value: int):
        """Set amendment_number"""
        self._data["amendment_number"] = value

    @property
    def amends_file(self) -> int:
        """Get amends_file"""
        return self._data.get("amends_file")
    @amends_file.setter
    def amends_file(self, value: int):
        """Set amends_file"""
        self._data["amends_file"] = value

    @property
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

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
    def document_description(self) -> str:
        """Get document_description"""
        return self._data.get("document_description")
    @document_description.setter
    def document_description(self, value: str):
        """Set document_description"""
        self._data["document_description"] = value

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
    def filed_date(self) -> str:
        """Get filed_date"""
        return self._data.get("filed_date")
    @filed_date.setter
    def filed_date(self, value: str):
        """Set filed_date"""
        self._data["filed_date"] = value

    @property
    def form_type(self) -> str:
        """Get form_type"""
        return self._data.get("form_type")
    @form_type.setter
    def form_type(self, value: str):
        """Set form_type"""
        self._data["form_type"] = value

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
    def load_timestamp(self) -> str:
        """Get load_timestamp"""
        return self._data.get("load_timestamp")
    @load_timestamp.setter
    def load_timestamp(self, value: str):
        """Set load_timestamp"""
        self._data["load_timestamp"] = value

    @property
    def most_recent(self) -> bool:
        """Get most_recent"""
        return self._data.get("most_recent")
    @most_recent.setter
    def most_recent(self, value: bool):
        """Set most_recent"""
        self._data["most_recent"] = value

    @property
    def most_recent_filing(self) -> int:
        """Get most_recent_filing"""
        return self._data.get("most_recent_filing")
    @most_recent_filing.setter
    def most_recent_filing(self, value: int):
        """Set most_recent_filing"""
        self._data["most_recent_filing"] = value

    @property
    def pdf_url(self) -> str:
        """Get pdf_url"""
        return self._data.get("pdf_url")
    @pdf_url.setter
    def pdf_url(self, value: str):
        """Set pdf_url"""
        self._data["pdf_url"] = value

    @property
    def receipt_date(self) -> str:
        """Get receipt_date"""
        return self._data.get("receipt_date")
    @receipt_date.setter
    def receipt_date(self, value: str):
        """Set receipt_date"""
        self._data["receipt_date"] = value
