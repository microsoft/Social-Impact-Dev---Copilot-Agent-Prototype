from __future__ import annotations

from typing import List, Union, Optional, Dict, Any

from ..base.base_model import BaseModel


class BaseF3XFiling(BaseModel):
    """
    Strongly-typed model class for BaseF3XFiling
    
    Generated from OpenAPI/Swagger specification
    """

    @property
    def amend_address(self) -> str:
        """Get amend_address"""
        return self._data.get("amend_address")
    @amend_address.setter
    def amend_address(self, value: str):
        """Set amend_address"""
        self._data["amend_address"] = value

    @property
    def amended_by(self) -> int:
        """Get amended_by"""
        return self._data.get("amended_by")
    @amended_by.setter
    def amended_by(self, value: int):
        """Set amended_by"""
        self._data["amended_by"] = value

    @property
    def amendment(self) -> str:
        """Get amendment"""
        return self._data.get("amendment")
    @amendment.setter
    def amendment(self, value: str):
        """Set amendment"""
        self._data["amendment"] = value

    @property
    def amendment_chain(self) -> List[int]:
        """Get amendment_chain"""
        return self._data.get("amendment_chain")
    @amendment_chain.setter
    def amendment_chain(self, value: List[int]):
        """Set amendment_chain"""
        self._data["amendment_chain"] = value

    @property
    def beginning_image_number(self) -> str:
        """Get beginning_image_number"""
        return self._data.get("beginning_image_number")
    @beginning_image_number.setter
    def beginning_image_number(self, value: str):
        """Set beginning_image_number"""
        self._data["beginning_image_number"] = value

    @property
    def city(self) -> str:
        """Get city"""
        return self._data.get("city")
    @city.setter
    def city(self, value: str):
        """Set city"""
        self._data["city"] = value

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
    def election_date(self) -> str:
        """Get election_date"""
        return self._data.get("election_date")
    @election_date.setter
    def election_date(self, value: str):
        """Set election_date"""
        self._data["election_date"] = value

    @property
    def election_state(self) -> str:
        """Get election_state"""
        return self._data.get("election_state")
    @election_state.setter
    def election_state(self, value: str):
        """Set election_state"""
        self._data["election_state"] = value

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
    def is_amended(self) -> bool:
        """Get is_amended"""
        return self._data.get("is_amended")
    @is_amended.setter
    def is_amended(self, value: bool):
        """Set is_amended"""
        self._data["is_amended"] = value

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
    def qualified_multicandidate_committee(self) -> str:
        """Get qualified_multicandidate_committee"""
        return self._data.get("qualified_multicandidate_committee")
    @qualified_multicandidate_committee.setter
    def qualified_multicandidate_committee(self, value: str):
        """Set qualified_multicandidate_committee"""
        self._data["qualified_multicandidate_committee"] = value

    @property
    def receipt_date(self) -> str:
        """Get receipt_date"""
        return self._data.get("receipt_date")
    @receipt_date.setter
    def receipt_date(self, value: str):
        """Set receipt_date"""
        self._data["receipt_date"] = value

    @property
    def report(self) -> str:
        """Get report"""
        return self._data.get("report")
    @report.setter
    def report(self, value: str):
        """Set report"""
        self._data["report"] = value

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
    def rpt_pgi(self) -> str:
        """Get rpt_pgi"""
        return self._data.get("rpt_pgi")
    @rpt_pgi.setter
    def rpt_pgi(self, value: str):
        """Set rpt_pgi"""
        self._data["rpt_pgi"] = value

    @property
    def sign_date(self) -> str:
        """Get sign_date"""
        return self._data.get("sign_date")
    @sign_date.setter
    def sign_date(self, value: str):
        """Set sign_date"""
        self._data["sign_date"] = value

    @property
    def state(self) -> str:
        """Get state"""
        return self._data.get("state")
    @state.setter
    def state(self, value: str):
        """Set state"""
        self._data["state"] = value

    @property
    def street_1(self) -> str:
        """Get street_1"""
        return self._data.get("street_1")
    @street_1.setter
    def street_1(self, value: str):
        """Set street_1"""
        self._data["street_1"] = value

    @property
    def street_2(self) -> str:
        """Get street_2"""
        return self._data.get("street_2")
    @street_2.setter
    def street_2(self, value: str):
        """Set street_2"""
        self._data["street_2"] = value

    @property
    def summary_lines(self) -> str:
        """Get summary_lines"""
        return self._data.get("summary_lines")
    @summary_lines.setter
    def summary_lines(self, value: str):
        """Set summary_lines"""
        self._data["summary_lines"] = value

    @property
    def zip(self) -> str:
        """Get zip"""
        return self._data.get("zip")
    @zip.setter
    def zip(self, value: str):
        """Set zip"""
        self._data["zip"] = value
