import requests
import logging
from typing import Optional, Dict, Any, Union, List
from .models.AuditCandidateSearch import AuditCandidateSearch
from .models.AuditCandidateSearchList import AuditCandidateSearchList
from .models.AuditCase import AuditCase
from .models.AuditCaseCategoryRelation import AuditCaseCategoryRelation
from .models.AuditCaseCategoryRelationPage import AuditCaseCategoryRelationPage
from .models.AuditCasePage import AuditCasePage
from .models.AuditCaseSubCategory import AuditCaseSubCategory
from .models.AuditCaseSubCategoryPage import AuditCaseSubCategoryPage
from .models.AuditCategory import AuditCategory
from .models.AuditCategoryPage import AuditCategoryPage
from .models.AuditCategoryRelation import AuditCategoryRelation
from .models.AuditCategoryRelationPage import AuditCategoryRelationPage
from .models.AuditCommitteeSearch import AuditCommitteeSearch
from .models.AuditCommitteeSearchList import AuditCommitteeSearchList
from .models.AuditPrimaryCategory import AuditPrimaryCategory
from .models.AuditPrimaryCategoryPage import AuditPrimaryCategoryPage
from .models.BaseF3Filing import BaseF3Filing
from .models.BaseF3FilingPage import BaseF3FilingPage
from .models.BaseF3PFiling import BaseF3PFiling
from .models.BaseF3PFilingPage import BaseF3PFilingPage
from .models.BaseF3XFiling import BaseF3XFiling
from .models.BaseF3XFilingPage import BaseF3XFilingPage
from .models.CCAggregates import CCAggregates
from .models.CCAggregatesPage import CCAggregatesPage
from .models.CCTotalsByCandidate import CCTotalsByCandidate
from .models.CCTotalsByCandidatePage import CCTotalsByCandidatePage
from .models.CalendarDate import CalendarDate
from .models.CalendarDatePage import CalendarDatePage
from .models.Candidate import Candidate
from .models.CandidateDetail import CandidateDetail
from .models.CandidateDetailPage import CandidateDetailPage
from .models.CandidateFlags import CandidateFlags
from .models.CandidateFlagsPage import CandidateFlagsPage
from .models.CandidateHistory import CandidateHistory
from .models.CandidateHistoryPage import CandidateHistoryPage
from .models.CandidateHistoryTotal import CandidateHistoryTotal
from .models.CandidateHistoryTotalPage import CandidateHistoryTotalPage
from .models.CandidatePage import CandidatePage
from .models.CandidateSearch import CandidateSearch
from .models.CandidateSearchBaseSchema import CandidateSearchBaseSchema
from .models.CandidateSearchListSchema import CandidateSearchListSchema
from .models.CandidateSearchPage import CandidateSearchPage
from .models.CandidateTotal import CandidateTotal
from .models.CandidateTotalAggregate import CandidateTotalAggregate
from .models.CandidateTotalAggregatePage import CandidateTotalAggregatePage
from .models.CandidateTotalPage import CandidateTotalPage
from .models.CandidateTotalsDetailHouseSenate import CandidateTotalsDetailHouseSenate
from .models.CandidateTotalsDetailHouseSenatePage import CandidateTotalsDetailHouseSenatePage
from .models.CandidateTotalsDetailPresidential import CandidateTotalsDetailPresidential
from .models.CandidateTotalsDetailPresidentialPage import CandidateTotalsDetailPresidentialPage
from .models.Committee import Committee
from .models.CommitteeDetail import CommitteeDetail
from .models.CommitteeDetailPage import CommitteeDetailPage
from .models.CommitteeHistory import CommitteeHistory
from .models.CommitteeHistoryPage import CommitteeHistoryPage
from .models.CommitteeHistoryProfile import CommitteeHistoryProfile
from .models.CommitteeHistoryProfilePage import CommitteeHistoryProfilePage
from .models.CommitteePage import CommitteePage
from .models.CommitteeReports import CommitteeReports
from .models.CommitteeReportsHouseSenate import CommitteeReportsHouseSenate
from .models.CommitteeReportsHouseSenatePage import CommitteeReportsHouseSenatePage
from .models.CommitteeReportsIEOnly import CommitteeReportsIEOnly
from .models.CommitteeReportsIEOnlyPage import CommitteeReportsIEOnlyPage
from .models.CommitteeReportsPacParty import CommitteeReportsPacParty
from .models.CommitteeReportsPacPartyPage import CommitteeReportsPacPartyPage
from .models.CommitteeReportsPage import CommitteeReportsPage
from .models.CommitteeReportsPresidential import CommitteeReportsPresidential
from .models.CommitteeReportsPresidentialPage import CommitteeReportsPresidentialPage
from .models.CommitteeSearch import CommitteeSearch
from .models.CommitteeSearchList import CommitteeSearchList
from .models.CommitteeTotals import CommitteeTotals
from .models.CommitteeTotalsHouseSenate import CommitteeTotalsHouseSenate
from .models.CommitteeTotalsHouseSenatePage import CommitteeTotalsHouseSenatePage
from .models.CommitteeTotalsIEOnly import CommitteeTotalsIEOnly
from .models.CommitteeTotalsIEOnlyPage import CommitteeTotalsIEOnlyPage
from .models.CommitteeTotalsPacParty import CommitteeTotalsPacParty
from .models.CommitteeTotalsPacPartyPage import CommitteeTotalsPacPartyPage
from .models.CommitteeTotalsPage import CommitteeTotalsPage
from .models.CommitteeTotalsPerCycle import CommitteeTotalsPerCycle
from .models.CommitteeTotalsPerCyclePage import CommitteeTotalsPerCyclePage
from .models.CommunicationCost import CommunicationCost
from .models.CommunicationCostByCandidate import CommunicationCostByCandidate
from .models.CommunicationCostByCandidatePage import CommunicationCostByCandidatePage
from .models.CommunicationCostPage import CommunicationCostPage
from .models.ECAggregates import ECAggregates
from .models.ECAggregatesPage import ECAggregatesPage
from .models.ECTotalsByCandidate import ECTotalsByCandidate
from .models.ECTotalsByCandidatePage import ECTotalsByCandidatePage
from .models.EFilings import EFilings
from .models.EFilingsPage import EFilingsPage
from .models.EfilingsAmendments import EfilingsAmendments
from .models.EfilingsAmendmentsPage import EfilingsAmendmentsPage
from .models.Election import Election
from .models.ElectionDates import ElectionDates
from .models.ElectionDatesPage import ElectionDatesPage
from .models.ElectionPage import ElectionPage
from .models.ElectionSearch import ElectionSearch
from .models.ElectionSearchPage import ElectionSearchPage
from .models.ElectionSummary import ElectionSummary
from .models.Electioneering import Electioneering
from .models.ElectioneeringByCandidate import ElectioneeringByCandidate
from .models.ElectioneeringByCandidatePage import ElectioneeringByCandidatePage
from .models.ElectioneeringPage import ElectioneeringPage
from .models.ElectionsList import ElectionsList
from .models.ElectionsListPage import ElectionsListPage
from .models.EntityReceiptDisbursementTotals import EntityReceiptDisbursementTotals
from .models.EntityReceiptDisbursementTotalsPage import EntityReceiptDisbursementTotalsPage
from .models.Filings import Filings
from .models.FilingsPage import FilingsPage
from .models.Form1 import Form1
from .models.Form1Page import Form1Page
from .models.Form2 import Form2
from .models.Form2Page import Form2Page
from .models.Form56 import Form56
from .models.Form56Page import Form56Page
from .models.IETotalsByCandidate import IETotalsByCandidate
from .models.IETotalsByCandidatePage import IETotalsByCandidatePage
from .models.InauguralDonations import InauguralDonations
from .models.InauguralDonationsPage import InauguralDonationsPage
from .models.JFCCommittee import JFCCommittee
from .models.NationalPartyTotals import NationalPartyTotals
from .models.NationalPartyTotalsPage import NationalPartyTotalsPage
from .models.NationalParty_ScheduleA import NationalParty_ScheduleA
from .models.NationalParty_ScheduleAPage import NationalParty_ScheduleAPage
from .models.NationalParty_ScheduleB import NationalParty_ScheduleB
from .models.NationalParty_ScheduleBPage import NationalParty_ScheduleBPage
from .models.OffsetInfo import OffsetInfo
from .models.OperationsLog import OperationsLog
from .models.OperationsLogPage import OperationsLogPage
from .models.PacSponsorCandidate import PacSponsorCandidate
from .models.PresidentialByCandidate import PresidentialByCandidate
from .models.PresidentialByCandidatePage import PresidentialByCandidatePage
from .models.PresidentialBySize import PresidentialBySize
from .models.PresidentialBySizePage import PresidentialBySizePage
from .models.PresidentialByState import PresidentialByState
from .models.PresidentialByStatePage import PresidentialByStatePage
from .models.PresidentialCoverage import PresidentialCoverage
from .models.PresidentialCoveragePage import PresidentialCoveragePage
from .models.PresidentialSummary import PresidentialSummary
from .models.PresidentialSummaryPage import PresidentialSummaryPage
from .models.PrincipalCommittee import PrincipalCommittee
from .models.RadAnalyst import RadAnalyst
from .models.RadAnalystPage import RadAnalystPage
from .models.ReportType import ReportType
from .models.ReportingDates import ReportingDates
from .models.ReportingDatesPage import ReportingDatesPage
from .models.ScheduleA import ScheduleA
from .models.ScheduleAByEmployer import ScheduleAByEmployer
from .models.ScheduleAByEmployerPage import ScheduleAByEmployerPage
from .models.ScheduleAByOccupation import ScheduleAByOccupation
from .models.ScheduleAByOccupationPage import ScheduleAByOccupationPage
from .models.ScheduleABySize import ScheduleABySize
from .models.ScheduleABySizeCandidate import ScheduleABySizeCandidate
from .models.ScheduleABySizeCandidatePage import ScheduleABySizeCandidatePage
from .models.ScheduleABySizePage import ScheduleABySizePage
from .models.ScheduleAByState import ScheduleAByState
from .models.ScheduleAByStateCandidate import ScheduleAByStateCandidate
from .models.ScheduleAByStateCandidatePage import ScheduleAByStateCandidatePage
from .models.ScheduleAByStatePage import ScheduleAByStatePage
from .models.ScheduleAByStateRecipientTotals import ScheduleAByStateRecipientTotals
from .models.ScheduleAByStateRecipientTotalsPage import ScheduleAByStateRecipientTotalsPage
from .models.ScheduleAByZip import ScheduleAByZip
from .models.ScheduleAByZipPage import ScheduleAByZipPage
from .models.ScheduleAEfile import ScheduleAEfile
from .models.ScheduleAEfilePage import ScheduleAEfilePage
from .models.ScheduleAPage import ScheduleAPage
from .models.ScheduleB import ScheduleB
from .models.ScheduleBByPurpose import ScheduleBByPurpose
from .models.ScheduleBByPurposePage import ScheduleBByPurposePage
from .models.ScheduleBByRecipient import ScheduleBByRecipient
from .models.ScheduleBByRecipientID import ScheduleBByRecipientID
from .models.ScheduleBByRecipientIDPage import ScheduleBByRecipientIDPage
from .models.ScheduleBByRecipientPage import ScheduleBByRecipientPage
from .models.ScheduleBEfile import ScheduleBEfile
from .models.ScheduleBEfilePage import ScheduleBEfilePage
from .models.ScheduleBPage import ScheduleBPage
from .models.ScheduleC import ScheduleC
from .models.ScheduleCPage import ScheduleCPage
from .models.ScheduleD import ScheduleD
from .models.ScheduleDPage import ScheduleDPage
from .models.ScheduleE import ScheduleE
from .models.ScheduleEByCandidate import ScheduleEByCandidate
from .models.ScheduleEByCandidatePage import ScheduleEByCandidatePage
from .models.ScheduleEEfile import ScheduleEEfile
from .models.ScheduleEEfilePage import ScheduleEEfilePage
from .models.ScheduleEPage import ScheduleEPage
from .models.ScheduleF import ScheduleF
from .models.ScheduleFPage import ScheduleFPage
from .models.ScheduleH4 import ScheduleH4
from .models.ScheduleH4Efile import ScheduleH4Efile
from .models.ScheduleH4EfilePage import ScheduleH4EfilePage
from .models.ScheduleH4Page import ScheduleH4Page
from .models.SeekInfo import SeekInfo
from .models.StateElectionOfficeInfo import StateElectionOfficeInfo
from .models.StateElectionOfficeInfoPage import StateElectionOfficeInfoPage
from .models.TestForm1 import TestForm1
from .models.TestForm1Page import TestForm1Page
from .models.TotalByOffice import TotalByOffice
from .models.TotalByOfficeByParty import TotalByOfficeByParty
from .models.TotalByOfficeByPartyPage import TotalByOfficeByPartyPage
from .models.TotalByOfficePage import TotalByOfficePage
from .models.TotalsCommittee import TotalsCommittee
from .models.TotalsCommitteePage import TotalsCommitteePage

class FecOpenapiAPIs:
    """
    Strongly-typed API client for fec_openapi
    
    This class provides methods to interact with the fec_openapi API endpoints.
    All methods are strongly-typed with automatic model serialization/deserialization.
    """
    
    def __init__(self, base_url: str = None, auth_token: str = None, tenant: str = None):
        """
        Initialize the API client
        
        Args:
            base_url: Base URL for the API service (default: not specified)
            auth_token: Authentication token for API requests
            tenant: Tenant ID for multi-tenant APIs
        """
        self.logger = logging.getLogger(__name__)
        self._tenant = tenant or ""
        self._base_url = base_url or ""
        self._headers = {
            "Content-Type": "application/json",
            "User-Agent": f"GeneratedApiClient/fec_openapi",
        }
        
        if auth_token:
            self.set_auth_token(auth_token)
    
    def set_base_url(self, base_url: str):
        """Set the base URL for API requests"""
        self._base_url = base_url.rstrip('/')
        self.logger.info(f"Base URL set to: {self._base_url}")
    
    def set_tenant(self, tenant: str):
        """Set the tenant ID"""
        self._tenant = tenant
        self.logger.info(f"Tenant set to: {tenant}")
    
    def get_tenant(self) -> str:
        """Get the current tenant ID"""
        return self._tenant
    
    def set_auth_token(self, token: str):
        """Set the authentication token"""
        self._headers["Authorization"] = f"Bearer {token}"
        self.logger.info("Authentication token updated")
    
    def get_headers(self) -> Dict[str, str]:
        """Get the current headers"""
        return self._headers.copy()
    
    def _make_request(self, method: str, url: str, **kwargs) -> requests.Response:
        """
        Make an HTTP request with error handling and logging
        
        Args:
            method: HTTP method (GET, POST, PUT, DELETE, etc.)
            url: Request URL
            **kwargs: Additional arguments for requests
            
        Returns:
            requests.Response: The response object
            
        Raises:
            requests.exceptions.RequestException: For request errors
        """
        try:
            self.logger.debug(f"Making {method} request to: {url}")
            
            # Ensure headers are included
            if 'headers' not in kwargs:
                kwargs['headers'] = self.get_headers()
            
            response = requests.request(method, url, **kwargs)
            
            # Log response details
            self.logger.debug(f"Response status: {response.status_code}")
            
            if not response.ok:
                self.logger.error(f"Request failed: {response.status_code} - {response.text}")
                response.raise_for_status()
            
            return response
            
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Request error: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected error: {e}")
            raise


    def get_v1_audit_case(self, page: Optional[int] = None, per_page: Optional[int] = None, q: Optional[List[str]] = None, qq: Optional[List[str]] = None, primary_category_id: Optional[str] = None, sub_category_id: Optional[str] = None, audit_case_id: Optional[List[str]] = None, cycle: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, committee_designation: Optional[str] = None, audit_id: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, min_election_cycle: Optional[int] = None, max_election_cycle: Optional[int] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_audit_case operation"""
        url = f"{self._base_url}/v1/audit-case/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if q is not None:
            params["q"] = q
        if qq is not None:
            params["qq"] = qq
        if primary_category_id is not None:
            params["primary_category_id"] = primary_category_id
        if sub_category_id is not None:
            params["sub_category_id"] = sub_category_id
        if audit_case_id is not None:
            params["audit_case_id"] = audit_case_id
        if cycle is not None:
            params["cycle"] = cycle
        if committee_id is not None:
            params["committee_id"] = committee_id
        if committee_type is not None:
            params["committee_type"] = committee_type
        if committee_designation is not None:
            params["committee_designation"] = committee_designation
        if audit_id is not None:
            params["audit_id"] = audit_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if min_election_cycle is not None:
            params["min_election_cycle"] = min_election_cycle
        if max_election_cycle is not None:
            params["max_election_cycle"] = max_election_cycle
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_audit_category(self, page: Optional[int] = None, per_page: Optional[int] = None, primary_category_id: Optional[List[str]] = None, primary_category_name: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_audit_category operation"""
        url = f"{self._base_url}/v1/audit-category/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if primary_category_id is not None:
            params["primary_category_id"] = primary_category_id
        if primary_category_name is not None:
            params["primary_category_name"] = primary_category_name
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_audit_primary_category(self, page: Optional[int] = None, per_page: Optional[int] = None, primary_category_id: Optional[List[str]] = None, primary_category_name: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_audit_primary_category operation"""
        url = f"{self._base_url}/v1/audit-primary-category/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if primary_category_id is not None:
            params["primary_category_id"] = primary_category_id
        if primary_category_name is not None:
            params["primary_category_name"] = primary_category_name
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_calendar_dates(self, page: Optional[int] = None, per_page: Optional[int] = None, calendar_category_id: Optional[List[int]] = None, description: Optional[List[str]] = None, summary: Optional[List[str]] = None, min_start_date: Optional[str] = None, min_end_date: Optional[str] = None, max_start_date: Optional[str] = None, max_end_date: Optional[str] = None, event_id: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_calendar_dates operation"""
        url = f"{self._base_url}/v1/calendar-dates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if calendar_category_id is not None:
            params["calendar_category_id"] = calendar_category_id
        if description is not None:
            params["description"] = description
        if summary is not None:
            params["summary"] = summary
        if min_start_date is not None:
            params["min_start_date"] = min_start_date
        if min_end_date is not None:
            params["min_end_date"] = min_end_date
        if max_start_date is not None:
            params["max_start_date"] = max_start_date
        if max_end_date is not None:
            params["max_end_date"] = max_end_date
        if event_id is not None:
            params["event_id"] = event_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_calendar_dates_export(self, renderer: Optional[str] = None, page: Optional[int] = None, per_page: Optional[int] = None, calendar_category_id: Optional[List[int]] = None, description: Optional[List[str]] = None, summary: Optional[List[str]] = None, min_start_date: Optional[str] = None, min_end_date: Optional[str] = None, max_start_date: Optional[str] = None, max_end_date: Optional[str] = None, event_id: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_calendar_dates_export operation"""
        url = f"{self._base_url}/v1/calendar-dates/export/"
        params = {}
        if renderer is not None:
            params["renderer"] = renderer
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if calendar_category_id is not None:
            params["calendar_category_id"] = calendar_category_id
        if description is not None:
            params["description"] = description
        if summary is not None:
            params["summary"] = summary
        if min_start_date is not None:
            params["min_start_date"] = min_start_date
        if min_end_date is not None:
            params["min_end_date"] = min_end_date
        if max_start_date is not None:
            params["max_start_date"] = max_start_date
        if max_end_date is not None:
            params["max_end_date"] = max_end_date
        if event_id is not None:
            params["event_id"] = event_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id(self, candidate_id: str, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, election_year: Optional[List[int]] = None, office: Optional[List[str]] = None, state: Optional[List[str]] = None, party: Optional[List[str]] = None, year: Optional[str] = None, district: Optional[List[str]] = None, candidate_status: Optional[List[str]] = None, incumbent_challenge: Optional[List[str]] = None, federal_funds_flag: Optional[bool] = None, has_raised_funds: Optional[bool] = None, name: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if election_year is not None:
            params["election_year"] = election_year
        if office is not None:
            params["office"] = office
        if state is not None:
            params["state"] = state
        if party is not None:
            params["party"] = party
        if year is not None:
            params["year"] = year
        if district is not None:
            params["district"] = district
        if candidate_status is not None:
            params["candidate_status"] = candidate_status
        if incumbent_challenge is not None:
            params["incumbent_challenge"] = incumbent_challenge
        if federal_funds_flag is not None:
            params["federal_funds_flag"] = federal_funds_flag
        if has_raised_funds is not None:
            params["has_raised_funds"] = has_raised_funds
        if name is not None:
            params["name"] = name
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_committees(self, candidate_id: str, page: Optional[int] = None, per_page: Optional[int] = None, year: Optional[List[int]] = None, cycle: Optional[List[int]] = None, filing_frequency: Optional[List[str]] = None, designation: Optional[List[str]] = None, organization_type: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_committees operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/committees/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if year is not None:
            params["year"] = year
        if cycle is not None:
            params["cycle"] = cycle
        if filing_frequency is not None:
            params["filing_frequency"] = filing_frequency
        if designation is not None:
            params["designation"] = designation
        if organization_type is not None:
            params["organization_type"] = organization_type
        if committee_type is not None:
            params["committee_type"] = committee_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_committees_history(self, candidate_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, designation: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_committees_history operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/committees/history/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if designation is not None:
            params["designation"] = designation
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_committees_history_cycle(self, candidate_id: str, cycle: int, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, designation: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_committees_history_cycle operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/committees/history/{cycle}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if designation is not None:
            params["designation"] = designation
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_filings(self, candidate_id: str, page: Optional[int] = None, per_page: Optional[int] = None, committee_type: Optional[str] = None, cycle: Optional[List[int]] = None, is_amended: Optional[bool] = None, most_recent: Optional[bool] = None, report_type: Optional[List[str]] = None, request_type: Optional[List[str]] = None, document_type: Optional[List[str]] = None, beginning_image_number: Optional[List[str]] = None, report_year: Optional[List[int]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, form_type: Optional[List[str]] = None, state: Optional[List[str]] = None, district: Optional[List[str]] = None, office: Optional[List[str]] = None, party: Optional[List[str]] = None, filer_type: Optional[str] = None, file_number: Optional[List[int]] = None, primary_general_indicator: Optional[List[str]] = None, amendment_indicator: Optional[List[str]] = None, form_category: Optional[List[str]] = None, q_filer: Optional[List[str]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_filings operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/filings/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_type is not None:
            params["committee_type"] = committee_type
        if cycle is not None:
            params["cycle"] = cycle
        if is_amended is not None:
            params["is_amended"] = is_amended
        if most_recent is not None:
            params["most_recent"] = most_recent
        if report_type is not None:
            params["report_type"] = report_type
        if request_type is not None:
            params["request_type"] = request_type
        if document_type is not None:
            params["document_type"] = document_type
        if beginning_image_number is not None:
            params["beginning_image_number"] = beginning_image_number
        if report_year is not None:
            params["report_year"] = report_year
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if form_type is not None:
            params["form_type"] = form_type
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if office is not None:
            params["office"] = office
        if party is not None:
            params["party"] = party
        if filer_type is not None:
            params["filer_type"] = filer_type
        if file_number is not None:
            params["file_number"] = file_number
        if primary_general_indicator is not None:
            params["primary_general_indicator"] = primary_general_indicator
        if amendment_indicator is not None:
            params["amendment_indicator"] = amendment_indicator
        if form_category is not None:
            params["form_category"] = form_category
        if q_filer is not None:
            params["q_filer"] = q_filer
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_history(self, candidate_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_history operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/history/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_history_cycle(self, candidate_id: str, cycle: int, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_history_cycle operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/history/{cycle}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidate_candidate_id_totals(self, candidate_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, cycle: Optional[List[int]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidate_candidate_id_totals operation"""
        url = f"{self._base_url}/v1/candidate/{candidate_id}/totals/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if cycle is not None:
            params["cycle"] = cycle
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidates(self, page: Optional[int] = None, per_page: Optional[int] = None, q: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, min_first_file_date: Optional[str] = None, max_first_file_date: Optional[str] = None, is_active_candidate: Optional[bool] = None, cycle: Optional[List[int]] = None, election_year: Optional[List[int]] = None, office: Optional[List[str]] = None, state: Optional[List[str]] = None, party: Optional[List[str]] = None, year: Optional[str] = None, district: Optional[List[str]] = None, candidate_status: Optional[List[str]] = None, incumbent_challenge: Optional[List[str]] = None, federal_funds_flag: Optional[bool] = None, has_raised_funds: Optional[bool] = None, name: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidates operation"""
        url = f"{self._base_url}/v1/candidates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if q is not None:
            params["q"] = q
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if min_first_file_date is not None:
            params["min_first_file_date"] = min_first_file_date
        if max_first_file_date is not None:
            params["max_first_file_date"] = max_first_file_date
        if is_active_candidate is not None:
            params["is_active_candidate"] = is_active_candidate
        if cycle is not None:
            params["cycle"] = cycle
        if election_year is not None:
            params["election_year"] = election_year
        if office is not None:
            params["office"] = office
        if state is not None:
            params["state"] = state
        if party is not None:
            params["party"] = party
        if year is not None:
            params["year"] = year
        if district is not None:
            params["district"] = district
        if candidate_status is not None:
            params["candidate_status"] = candidate_status
        if incumbent_challenge is not None:
            params["incumbent_challenge"] = incumbent_challenge
        if federal_funds_flag is not None:
            params["federal_funds_flag"] = federal_funds_flag
        if has_raised_funds is not None:
            params["has_raised_funds"] = has_raised_funds
        if name is not None:
            params["name"] = name
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidates_search(self, page: Optional[int] = None, per_page: Optional[int] = None, q: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, min_first_file_date: Optional[str] = None, max_first_file_date: Optional[str] = None, is_active_candidate: Optional[bool] = None, cycle: Optional[List[int]] = None, election_year: Optional[List[int]] = None, office: Optional[List[str]] = None, state: Optional[List[str]] = None, party: Optional[List[str]] = None, year: Optional[str] = None, district: Optional[List[str]] = None, candidate_status: Optional[List[str]] = None, incumbent_challenge: Optional[List[str]] = None, federal_funds_flag: Optional[bool] = None, has_raised_funds: Optional[bool] = None, name: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidates_search operation"""
        url = f"{self._base_url}/v1/candidates/search/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if q is not None:
            params["q"] = q
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if min_first_file_date is not None:
            params["min_first_file_date"] = min_first_file_date
        if max_first_file_date is not None:
            params["max_first_file_date"] = max_first_file_date
        if is_active_candidate is not None:
            params["is_active_candidate"] = is_active_candidate
        if cycle is not None:
            params["cycle"] = cycle
        if election_year is not None:
            params["election_year"] = election_year
        if office is not None:
            params["office"] = office
        if state is not None:
            params["state"] = state
        if party is not None:
            params["party"] = party
        if year is not None:
            params["year"] = year
        if district is not None:
            params["district"] = district
        if candidate_status is not None:
            params["candidate_status"] = candidate_status
        if incumbent_challenge is not None:
            params["incumbent_challenge"] = incumbent_challenge
        if federal_funds_flag is not None:
            params["federal_funds_flag"] = federal_funds_flag
        if has_raised_funds is not None:
            params["has_raised_funds"] = has_raised_funds
        if name is not None:
            params["name"] = name
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidates_totals(self, page: Optional[int] = None, per_page: Optional[int] = None, q: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, election_year: Optional[List[int]] = None, cycle: Optional[List[int]] = None, office: Optional[List[str]] = None, election_full: Optional[bool] = None, state: Optional[List[str]] = None, district: Optional[List[str]] = None, party: Optional[List[str]] = None, min_receipts: Optional[float] = None, max_receipts: Optional[float] = None, min_disbursements: Optional[float] = None, max_disbursements: Optional[float] = None, min_cash_on_hand_end_period: Optional[float] = None, max_cash_on_hand_end_period: Optional[float] = None, min_debts_owed_by_committee: Optional[float] = None, max_debts_owed_by_committee: Optional[float] = None, federal_funds_flag: Optional[bool] = None, has_raised_funds: Optional[bool] = None, is_active_candidate: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidates_totals operation"""
        url = f"{self._base_url}/v1/candidates/totals/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if q is not None:
            params["q"] = q
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if election_year is not None:
            params["election_year"] = election_year
        if cycle is not None:
            params["cycle"] = cycle
        if office is not None:
            params["office"] = office
        if election_full is not None:
            params["election_full"] = election_full
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if party is not None:
            params["party"] = party
        if min_receipts is not None:
            params["min_receipts"] = min_receipts
        if max_receipts is not None:
            params["max_receipts"] = max_receipts
        if min_disbursements is not None:
            params["min_disbursements"] = min_disbursements
        if max_disbursements is not None:
            params["max_disbursements"] = max_disbursements
        if min_cash_on_hand_end_period is not None:
            params["min_cash_on_hand_end_period"] = min_cash_on_hand_end_period
        if max_cash_on_hand_end_period is not None:
            params["max_cash_on_hand_end_period"] = max_cash_on_hand_end_period
        if min_debts_owed_by_committee is not None:
            params["min_debts_owed_by_committee"] = min_debts_owed_by_committee
        if max_debts_owed_by_committee is not None:
            params["max_debts_owed_by_committee"] = max_debts_owed_by_committee
        if federal_funds_flag is not None:
            params["federal_funds_flag"] = federal_funds_flag
        if has_raised_funds is not None:
            params["has_raised_funds"] = has_raised_funds
        if is_active_candidate is not None:
            params["is_active_candidate"] = is_active_candidate
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_candidates_totals_aggregates(self, page: Optional[int] = None, per_page: Optional[int] = None, election_year: Optional[List[int]] = None, office: Optional[str] = None, is_active_candidate: Optional[bool] = None, election_full: Optional[bool] = None, min_election_cycle: Optional[int] = None, max_election_cycle: Optional[int] = None, state: Optional[List[str]] = None, district: Optional[List[str]] = None, party: Optional[str] = None, aggregate_by: Optional[str] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_candidates_totals_aggregates operation"""
        url = f"{self._base_url}/v1/candidates/totals/aggregates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_year is not None:
            params["election_year"] = election_year
        if office is not None:
            params["office"] = office
        if is_active_candidate is not None:
            params["is_active_candidate"] = is_active_candidate
        if election_full is not None:
            params["election_full"] = election_full
        if min_election_cycle is not None:
            params["min_election_cycle"] = min_election_cycle
        if max_election_cycle is not None:
            params["max_election_cycle"] = max_election_cycle
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if party is not None:
            params["party"] = party
        if aggregate_by is not None:
            params["aggregate_by"] = aggregate_by
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, year: Optional[List[int]] = None, cycle: Optional[List[int]] = None, filing_frequency: Optional[List[str]] = None, designation: Optional[List[str]] = None, organization_type: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if year is not None:
            params["year"] = year
        if cycle is not None:
            params["cycle"] = cycle
        if filing_frequency is not None:
            params["filing_frequency"] = filing_frequency
        if designation is not None:
            params["designation"] = designation
        if organization_type is not None:
            params["organization_type"] = organization_type
        if committee_type is not None:
            params["committee_type"] = committee_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_candidates(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, election_year: Optional[List[int]] = None, office: Optional[List[str]] = None, state: Optional[List[str]] = None, party: Optional[List[str]] = None, year: Optional[str] = None, district: Optional[List[str]] = None, candidate_status: Optional[List[str]] = None, incumbent_challenge: Optional[List[str]] = None, federal_funds_flag: Optional[bool] = None, has_raised_funds: Optional[bool] = None, name: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_candidates operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/candidates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if election_year is not None:
            params["election_year"] = election_year
        if office is not None:
            params["office"] = office
        if state is not None:
            params["state"] = state
        if party is not None:
            params["party"] = party
        if year is not None:
            params["year"] = year
        if district is not None:
            params["district"] = district
        if candidate_status is not None:
            params["candidate_status"] = candidate_status
        if incumbent_challenge is not None:
            params["incumbent_challenge"] = incumbent_challenge
        if federal_funds_flag is not None:
            params["federal_funds_flag"] = federal_funds_flag
        if has_raised_funds is not None:
            params["has_raised_funds"] = has_raised_funds
        if name is not None:
            params["name"] = name
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_candidates_history(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_candidates_history operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/candidates/history/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_candidates_history_cycle(self, cycle: int, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_candidates_history_cycle operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/candidates/history/{cycle}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_filings(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, committee_type: Optional[str] = None, cycle: Optional[List[int]] = None, is_amended: Optional[bool] = None, most_recent: Optional[bool] = None, report_type: Optional[List[str]] = None, request_type: Optional[List[str]] = None, document_type: Optional[List[str]] = None, beginning_image_number: Optional[List[str]] = None, report_year: Optional[List[int]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, form_type: Optional[List[str]] = None, state: Optional[List[str]] = None, district: Optional[List[str]] = None, office: Optional[List[str]] = None, party: Optional[List[str]] = None, filer_type: Optional[str] = None, file_number: Optional[List[int]] = None, primary_general_indicator: Optional[List[str]] = None, amendment_indicator: Optional[List[str]] = None, form_category: Optional[List[str]] = None, q_filer: Optional[List[str]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_filings operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/filings/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_type is not None:
            params["committee_type"] = committee_type
        if cycle is not None:
            params["cycle"] = cycle
        if is_amended is not None:
            params["is_amended"] = is_amended
        if most_recent is not None:
            params["most_recent"] = most_recent
        if report_type is not None:
            params["report_type"] = report_type
        if request_type is not None:
            params["request_type"] = request_type
        if document_type is not None:
            params["document_type"] = document_type
        if beginning_image_number is not None:
            params["beginning_image_number"] = beginning_image_number
        if report_year is not None:
            params["report_year"] = report_year
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if form_type is not None:
            params["form_type"] = form_type
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if office is not None:
            params["office"] = office
        if party is not None:
            params["party"] = party
        if filer_type is not None:
            params["filer_type"] = filer_type
        if file_number is not None:
            params["file_number"] = file_number
        if primary_general_indicator is not None:
            params["primary_general_indicator"] = primary_general_indicator
        if amendment_indicator is not None:
            params["amendment_indicator"] = amendment_indicator
        if form_category is not None:
            params["form_category"] = form_category
        if q_filer is not None:
            params["q_filer"] = q_filer
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_history(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, designation: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_history operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/history/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if designation is not None:
            params["designation"] = designation
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_history_cycle(self, cycle: int, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, election_full: Optional[bool] = None, designation: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_history_cycle operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/history/{cycle}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_full is not None:
            params["election_full"] = election_full
        if designation is not None:
            params["designation"] = designation
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_reports(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, year: Optional[List[int]] = None, cycle: Optional[List[int]] = None, beginning_image_number: Optional[List[str]] = None, report_type: Optional[List[str]] = None, is_amended: Optional[bool] = None, min_disbursements_amount: Optional[float] = None, max_disbursements_amount: Optional[float] = None, min_receipts_amount: Optional[float] = None, max_receipts_amount: Optional[float] = None, min_cash_on_hand_end_period_amount: Optional[float] = None, max_cash_on_hand_end_period_amount: Optional[float] = None, min_debts_owed_amount: Optional[float] = None, max_debts_owed_expenditures: Optional[float] = None, min_independent_expenditures: Optional[float] = None, max_independent_expenditures: Optional[float] = None, min_party_coordinated_expenditures: Optional[float] = None, max_party_coordinated_expenditures: Optional[float] = None, min_total_contributions: Optional[float] = None, max_total_contributions: Optional[float] = None, type: Optional[List[str]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_reports operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/reports/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if year is not None:
            params["year"] = year
        if cycle is not None:
            params["cycle"] = cycle
        if beginning_image_number is not None:
            params["beginning_image_number"] = beginning_image_number
        if report_type is not None:
            params["report_type"] = report_type
        if is_amended is not None:
            params["is_amended"] = is_amended
        if min_disbursements_amount is not None:
            params["min_disbursements_amount"] = min_disbursements_amount
        if max_disbursements_amount is not None:
            params["max_disbursements_amount"] = max_disbursements_amount
        if min_receipts_amount is not None:
            params["min_receipts_amount"] = min_receipts_amount
        if max_receipts_amount is not None:
            params["max_receipts_amount"] = max_receipts_amount
        if min_cash_on_hand_end_period_amount is not None:
            params["min_cash_on_hand_end_period_amount"] = min_cash_on_hand_end_period_amount
        if max_cash_on_hand_end_period_amount is not None:
            params["max_cash_on_hand_end_period_amount"] = max_cash_on_hand_end_period_amount
        if min_debts_owed_amount is not None:
            params["min_debts_owed_amount"] = min_debts_owed_amount
        if max_debts_owed_expenditures is not None:
            params["max_debts_owed_expenditures"] = max_debts_owed_expenditures
        if min_independent_expenditures is not None:
            params["min_independent_expenditures"] = min_independent_expenditures
        if max_independent_expenditures is not None:
            params["max_independent_expenditures"] = max_independent_expenditures
        if min_party_coordinated_expenditures is not None:
            params["min_party_coordinated_expenditures"] = min_party_coordinated_expenditures
        if max_party_coordinated_expenditures is not None:
            params["max_party_coordinated_expenditures"] = max_party_coordinated_expenditures
        if min_total_contributions is not None:
            params["min_total_contributions"] = min_total_contributions
        if max_total_contributions is not None:
            params["max_total_contributions"] = max_total_contributions
        if type is not None:
            params["type"] = type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committee_committee_id_totals(self, committee_id: str, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committee_committee_id_totals operation"""
        url = f"{self._base_url}/v1/committee/{committee_id}/totals/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_committees(self, page: Optional[int] = None, per_page: Optional[int] = None, year: Optional[List[int]] = None, cycle: Optional[List[int]] = None, filing_frequency: Optional[List[str]] = None, designation: Optional[List[str]] = None, organization_type: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, q: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, state: Optional[List[str]] = None, party: Optional[List[str]] = None, min_first_file_date: Optional[str] = None, max_first_file_date: Optional[str] = None, min_last_file_date: Optional[str] = None, max_last_file_date: Optional[str] = None, min_first_f1_date: Optional[str] = None, max_first_f1_date: Optional[str] = None, min_last_f1_date: Optional[str] = None, max_last_f1_date: Optional[str] = None, treasurer_name: Optional[List[str]] = None, sponsor_candidate_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_committees operation"""
        url = f"{self._base_url}/v1/committees/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if year is not None:
            params["year"] = year
        if cycle is not None:
            params["cycle"] = cycle
        if filing_frequency is not None:
            params["filing_frequency"] = filing_frequency
        if designation is not None:
            params["designation"] = designation
        if organization_type is not None:
            params["organization_type"] = organization_type
        if committee_type is not None:
            params["committee_type"] = committee_type
        if q is not None:
            params["q"] = q
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if state is not None:
            params["state"] = state
        if party is not None:
            params["party"] = party
        if min_first_file_date is not None:
            params["min_first_file_date"] = min_first_file_date
        if max_first_file_date is not None:
            params["max_first_file_date"] = max_first_file_date
        if min_last_file_date is not None:
            params["min_last_file_date"] = min_last_file_date
        if max_last_file_date is not None:
            params["max_last_file_date"] = max_last_file_date
        if min_first_f1_date is not None:
            params["min_first_f1_date"] = min_first_f1_date
        if max_first_f1_date is not None:
            params["max_first_f1_date"] = max_first_f1_date
        if min_last_f1_date is not None:
            params["min_last_f1_date"] = min_last_f1_date
        if max_last_f1_date is not None:
            params["max_last_f1_date"] = max_last_f1_date
        if treasurer_name is not None:
            params["treasurer_name"] = treasurer_name
        if sponsor_candidate_id is not None:
            params["sponsor_candidate_id"] = sponsor_candidate_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_communication_costs(self, page: Optional[int] = None, per_page: Optional[int] = None, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, support_oppose_indicator: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_communication_costs operation"""
        url = f"{self._base_url}/v1/communication_costs/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if support_oppose_indicator is not None:
            params["support_oppose_indicator"] = support_oppose_indicator
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_communication_costs_aggregates(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, support_oppose_indicator: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_communication_costs_aggregates operation"""
        url = f"{self._base_url}/v1/communication_costs/aggregates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if committee_id is not None:
            params["committee_id"] = committee_id
        if support_oppose_indicator is not None:
            params["support_oppose_indicator"] = support_oppose_indicator
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_communication_costs_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, state: Optional[str] = None, district: Optional[str] = None, cycle: Optional[List[int]] = None, office: Optional[str] = None, election_full: Optional[bool] = None, candidate_id: Optional[List[str]] = None, support_oppose: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_communication_costs_by_candidate operation"""
        url = f"{self._base_url}/v1/communication_costs/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if cycle is not None:
            params["cycle"] = cycle
        if office is not None:
            params["office"] = office
        if election_full is not None:
            params["election_full"] = election_full
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if support_oppose is not None:
            params["support_oppose"] = support_oppose
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_communication_costs_totals_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, election_full: Optional[bool] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_communication_costs_totals_by_candidate operation"""
        url = f"{self._base_url}/v1/communication_costs/totals/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_efile_filings(self, page: Optional[int] = None, per_page: Optional[int] = None, file_number: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, q_filer: Optional[List[str]] = None, form_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_efile_filings operation"""
        url = f"{self._base_url}/v1/efile/filings/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if file_number is not None:
            params["file_number"] = file_number
        if committee_id is not None:
            params["committee_id"] = committee_id
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if q_filer is not None:
            params["q_filer"] = q_filer
        if form_type is not None:
            params["form_type"] = form_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_efile_form1(self, page: Optional[int] = None, per_page: Optional[int] = None, file_number: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, election_state: Optional[List[str]] = None, candidate_office: Optional[List[str]] = None, candidate_district: Optional[List[str]] = None, candidate_party: Optional[List[str]] = None, image_number: Optional[List[str]] = None, min_load_timestamp: Optional[str] = None, max_load_timestamp: Optional[str] = None, committee_type: Optional[List[str]] = None, organization_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_efile_form1 operation"""
        url = f"{self._base_url}/v1/efile/form1/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if file_number is not None:
            params["file_number"] = file_number
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if election_state is not None:
            params["election_state"] = election_state
        if candidate_office is not None:
            params["candidate_office"] = candidate_office
        if candidate_district is not None:
            params["candidate_district"] = candidate_district
        if candidate_party is not None:
            params["candidate_party"] = candidate_party
        if image_number is not None:
            params["image_number"] = image_number
        if min_load_timestamp is not None:
            params["min_load_timestamp"] = min_load_timestamp
        if max_load_timestamp is not None:
            params["max_load_timestamp"] = max_load_timestamp
        if committee_type is not None:
            params["committee_type"] = committee_type
        if organization_type is not None:
            params["organization_type"] = organization_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_efile_form2(self, page: Optional[int] = None, per_page: Optional[int] = None, file_number: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, election_state: Optional[List[str]] = None, candidate_office: Optional[List[str]] = None, candidate_district: Optional[List[str]] = None, candidate_party: Optional[List[str]] = None, image_number: Optional[List[str]] = None, min_load_timestamp: Optional[str] = None, max_load_timestamp: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_efile_form2 operation"""
        url = f"{self._base_url}/v1/efile/form2/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if file_number is not None:
            params["file_number"] = file_number
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if election_state is not None:
            params["election_state"] = election_state
        if candidate_office is not None:
            params["candidate_office"] = candidate_office
        if candidate_district is not None:
            params["candidate_district"] = candidate_district
        if candidate_party is not None:
            params["candidate_party"] = candidate_party
        if image_number is not None:
            params["image_number"] = image_number
        if min_load_timestamp is not None:
            params["min_load_timestamp"] = min_load_timestamp
        if max_load_timestamp is not None:
            params["max_load_timestamp"] = max_load_timestamp
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_efile_reports_house_senate(self, page: Optional[int] = None, per_page: Optional[int] = None, file_number: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, q_filer: Optional[List[str]] = None, form_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_efile_reports_house_senate operation"""
        url = f"{self._base_url}/v1/efile/reports/house-senate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if file_number is not None:
            params["file_number"] = file_number
        if committee_id is not None:
            params["committee_id"] = committee_id
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if q_filer is not None:
            params["q_filer"] = q_filer
        if form_type is not None:
            params["form_type"] = form_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_efile_reports_pac_party(self, page: Optional[int] = None, per_page: Optional[int] = None, file_number: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, q_filer: Optional[List[str]] = None, form_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_efile_reports_pac_party operation"""
        url = f"{self._base_url}/v1/efile/reports/pac-party/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if file_number is not None:
            params["file_number"] = file_number
        if committee_id is not None:
            params["committee_id"] = committee_id
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if q_filer is not None:
            params["q_filer"] = q_filer
        if form_type is not None:
            params["form_type"] = form_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_efile_reports_presidential(self, page: Optional[int] = None, per_page: Optional[int] = None, file_number: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, q_filer: Optional[List[str]] = None, form_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_efile_reports_presidential operation"""
        url = f"{self._base_url}/v1/efile/reports/presidential/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if file_number is not None:
            params["file_number"] = file_number
        if committee_id is not None:
            params["committee_id"] = committee_id
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if q_filer is not None:
            params["q_filer"] = q_filer
        if form_type is not None:
            params["form_type"] = form_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_election_dates(self, page: Optional[int] = None, per_page: Optional[int] = None, election_state: Optional[List[str]] = None, election_district: Optional[List[str]] = None, election_party: Optional[List[str]] = None, office_sought: Optional[List[str]] = None, min_election_date: Optional[str] = None, max_election_date: Optional[str] = None, election_type_id: Optional[List[str]] = None, min_create_date: Optional[str] = None, max_create_date: Optional[str] = None, min_update_date: Optional[str] = None, max_update_date: Optional[str] = None, election_year: Optional[List[str]] = None, min_primary_general_date: Optional[str] = None, max_primary_general_date: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_election_dates operation"""
        url = f"{self._base_url}/v1/election-dates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_state is not None:
            params["election_state"] = election_state
        if election_district is not None:
            params["election_district"] = election_district
        if election_party is not None:
            params["election_party"] = election_party
        if office_sought is not None:
            params["office_sought"] = office_sought
        if min_election_date is not None:
            params["min_election_date"] = min_election_date
        if max_election_date is not None:
            params["max_election_date"] = max_election_date
        if election_type_id is not None:
            params["election_type_id"] = election_type_id
        if min_create_date is not None:
            params["min_create_date"] = min_create_date
        if max_create_date is not None:
            params["max_create_date"] = max_create_date
        if min_update_date is not None:
            params["min_update_date"] = min_update_date
        if max_update_date is not None:
            params["max_update_date"] = max_update_date
        if election_year is not None:
            params["election_year"] = election_year
        if min_primary_general_date is not None:
            params["min_primary_general_date"] = min_primary_general_date
        if max_primary_general_date is not None:
            params["max_primary_general_date"] = max_primary_general_date
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_electioneering(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, report_year: Optional[List[int]] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, disbursement_description: Optional[List[str]] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_electioneering operation"""
        url = f"{self._base_url}/v1/electioneering/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if report_year is not None:
            params["report_year"] = report_year
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if disbursement_description is not None:
            params["disbursement_description"] = disbursement_description
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_electioneering_aggregates(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_electioneering_aggregates operation"""
        url = f"{self._base_url}/v1/electioneering/aggregates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_electioneering_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, state: Optional[str] = None, district: Optional[str] = None, cycle: Optional[List[int]] = None, office: Optional[str] = None, election_full: Optional[bool] = None, candidate_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_electioneering_by_candidate operation"""
        url = f"{self._base_url}/v1/electioneering/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if cycle is not None:
            params["cycle"] = cycle
        if office is not None:
            params["office"] = office
        if election_full is not None:
            params["election_full"] = election_full
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_electioneering_totals_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, election_full: Optional[bool] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_electioneering_totals_by_candidate operation"""
        url = f"{self._base_url}/v1/electioneering/totals/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_elections(self, page: Optional[int] = None, per_page: Optional[int] = None, state: Optional[str] = None, district: Optional[str] = None, cycle: int, office: str, election_full: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_elections operation"""
        url = f"{self._base_url}/v1/elections/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        params["cycle"] = cycle
        params["office"] = office
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_elections_search(self, page: Optional[int] = None, per_page: Optional[int] = None, state: Optional[List[str]] = None, district: Optional[List[str]] = None, cycle: Optional[List[int]] = None, zip: Optional[List[int]] = None, office: Optional[List[str]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_elections_search operation"""
        url = f"{self._base_url}/v1/elections/search/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if cycle is not None:
            params["cycle"] = cycle
        if zip is not None:
            params["zip"] = zip
        if office is not None:
            params["office"] = office
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_elections_summary(self, state: Optional[str] = None, district: Optional[str] = None, cycle: int, office: str, election_full: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_elections_summary operation"""
        url = f"{self._base_url}/v1/elections/summary/"
        params = {}
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        params["cycle"] = cycle
        params["office"] = office
        if election_full is not None:
            params["election_full"] = election_full
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_filings(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_type: Optional[str] = None, cycle: Optional[List[int]] = None, is_amended: Optional[bool] = None, most_recent: Optional[bool] = None, report_type: Optional[List[str]] = None, request_type: Optional[List[str]] = None, document_type: Optional[List[str]] = None, beginning_image_number: Optional[List[str]] = None, report_year: Optional[List[int]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, form_type: Optional[List[str]] = None, state: Optional[List[str]] = None, district: Optional[List[str]] = None, office: Optional[List[str]] = None, party: Optional[List[str]] = None, filer_type: Optional[str] = None, file_number: Optional[List[int]] = None, primary_general_indicator: Optional[List[str]] = None, amendment_indicator: Optional[List[str]] = None, form_category: Optional[List[str]] = None, q_filer: Optional[List[str]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_filings operation"""
        url = f"{self._base_url}/v1/filings/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_type is not None:
            params["committee_type"] = committee_type
        if cycle is not None:
            params["cycle"] = cycle
        if is_amended is not None:
            params["is_amended"] = is_amended
        if most_recent is not None:
            params["most_recent"] = most_recent
        if report_type is not None:
            params["report_type"] = report_type
        if request_type is not None:
            params["request_type"] = request_type
        if document_type is not None:
            params["document_type"] = document_type
        if beginning_image_number is not None:
            params["beginning_image_number"] = beginning_image_number
        if report_year is not None:
            params["report_year"] = report_year
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if form_type is not None:
            params["form_type"] = form_type
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if office is not None:
            params["office"] = office
        if party is not None:
            params["party"] = party
        if filer_type is not None:
            params["filer_type"] = filer_type
        if file_number is not None:
            params["file_number"] = file_number
        if primary_general_indicator is not None:
            params["primary_general_indicator"] = primary_general_indicator
        if amendment_indicator is not None:
            params["amendment_indicator"] = amendment_indicator
        if form_category is not None:
            params["form_category"] = form_category
        if q_filer is not None:
            params["q_filer"] = q_filer
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_legal_docs_doc_type_no(self, no: str, doc_type: str, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_legal_docs_doc_type_no operation"""
        url = f"{self._base_url}/v1/legal/docs/{doc_type}/{no}"
        params = {}
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_legal_search(self, q: Optional[str] = None, from_hit: Optional[int] = None, hits_returned: Optional[int] = None, type: Optional[str] = None, ao_no: Optional[List[str]] = None, ao_year: Optional[int] = None, ao_name: Optional[List[str]] = None, ao_min_issue_date: Optional[str] = None, ao_max_issue_date: Optional[str] = None, ao_min_request_date: Optional[str] = None, ao_max_request_date: Optional[str] = None, ao_min_document_date: Optional[str] = None, ao_max_document_date: Optional[str] = None, ao_doc_category_id: Optional[List[str]] = None, ao_is_pending: Optional[bool] = None, ao_status: Optional[str] = None, ao_requestor: Optional[str] = None, ao_requestor_type: Optional[List[str]] = None, ao_regulatory_citation: Optional[List[str]] = None, ao_statutory_citation: Optional[List[str]] = None, ao_citation_require_all: Optional[bool] = None, ao_commenter: Optional[str] = None, ao_representative: Optional[str] = None, case_no: Optional[List[str]] = None, case_respondents: Optional[str] = None, case_election_cycles: Optional[int] = None, case_min_open_date: Optional[str] = None, primary_subject_id: Optional[List[str]] = None, secondary_subject_id: Optional[List[str]] = None, case_max_open_date: Optional[str] = None, case_min_close_date: Optional[str] = None, case_max_close_date: Optional[str] = None, case_min_document_date: Optional[str] = None, case_max_document_date: Optional[str] = None, case_regulatory_citation: Optional[List[str]] = None, case_statutory_citation: Optional[List[str]] = None, case_citation_require_all: Optional[bool] = None, q_exclude: Optional[str] = None, case_doc_category_id: Optional[List[str]] = None, mur_type: Optional[str] = None, mur_disposition_category_id: Optional[List[str]] = None, af_name: Optional[List[str]] = None, af_committee_id: Optional[str] = None, af_report_year: Optional[str] = None, af_min_rtb_date: Optional[str] = None, af_max_rtb_date: Optional[str] = None, af_rtb_fine_amount: Optional[int] = None, af_min_fd_date: Optional[str] = None, af_max_fd_date: Optional[str] = None, af_fd_fine_amount: Optional[int] = None, sort: Optional[str] = None, case_min_penalty_amount: Optional[str] = None, case_max_penalty_amount: Optional[str] = None, q_proximity: Optional[List[str]] = None, max_gaps: Optional[int] = None, proximity_preserve_order: Optional[bool] = None, proximity_filter: Optional[str] = None, proximity_filter_term: Optional[str] = None, filename: Optional[str] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_legal_search operation"""
        url = f"{self._base_url}/v1/legal/search/"
        params = {}
        if q is not None:
            params["q"] = q
        if from_hit is not None:
            params["from_hit"] = from_hit
        if hits_returned is not None:
            params["hits_returned"] = hits_returned
        if type is not None:
            params["type"] = type
        if ao_no is not None:
            params["ao_no"] = ao_no
        if ao_year is not None:
            params["ao_year"] = ao_year
        if ao_name is not None:
            params["ao_name"] = ao_name
        if ao_min_issue_date is not None:
            params["ao_min_issue_date"] = ao_min_issue_date
        if ao_max_issue_date is not None:
            params["ao_max_issue_date"] = ao_max_issue_date
        if ao_min_request_date is not None:
            params["ao_min_request_date"] = ao_min_request_date
        if ao_max_request_date is not None:
            params["ao_max_request_date"] = ao_max_request_date
        if ao_min_document_date is not None:
            params["ao_min_document_date"] = ao_min_document_date
        if ao_max_document_date is not None:
            params["ao_max_document_date"] = ao_max_document_date
        if ao_doc_category_id is not None:
            params["ao_doc_category_id"] = ao_doc_category_id
        if ao_is_pending is not None:
            params["ao_is_pending"] = ao_is_pending
        if ao_status is not None:
            params["ao_status"] = ao_status
        if ao_requestor is not None:
            params["ao_requestor"] = ao_requestor
        if ao_requestor_type is not None:
            params["ao_requestor_type"] = ao_requestor_type
        if ao_regulatory_citation is not None:
            params["ao_regulatory_citation"] = ao_regulatory_citation
        if ao_statutory_citation is not None:
            params["ao_statutory_citation"] = ao_statutory_citation
        if ao_citation_require_all is not None:
            params["ao_citation_require_all"] = ao_citation_require_all
        if ao_commenter is not None:
            params["ao_commenter"] = ao_commenter
        if ao_representative is not None:
            params["ao_representative"] = ao_representative
        if case_no is not None:
            params["case_no"] = case_no
        if case_respondents is not None:
            params["case_respondents"] = case_respondents
        if case_election_cycles is not None:
            params["case_election_cycles"] = case_election_cycles
        if case_min_open_date is not None:
            params["case_min_open_date"] = case_min_open_date
        if primary_subject_id is not None:
            params["primary_subject_id"] = primary_subject_id
        if secondary_subject_id is not None:
            params["secondary_subject_id"] = secondary_subject_id
        if case_max_open_date is not None:
            params["case_max_open_date"] = case_max_open_date
        if case_min_close_date is not None:
            params["case_min_close_date"] = case_min_close_date
        if case_max_close_date is not None:
            params["case_max_close_date"] = case_max_close_date
        if case_min_document_date is not None:
            params["case_min_document_date"] = case_min_document_date
        if case_max_document_date is not None:
            params["case_max_document_date"] = case_max_document_date
        if case_regulatory_citation is not None:
            params["case_regulatory_citation"] = case_regulatory_citation
        if case_statutory_citation is not None:
            params["case_statutory_citation"] = case_statutory_citation
        if case_citation_require_all is not None:
            params["case_citation_require_all"] = case_citation_require_all
        if q_exclude is not None:
            params["q_exclude"] = q_exclude
        if case_doc_category_id is not None:
            params["case_doc_category_id"] = case_doc_category_id
        if mur_type is not None:
            params["mur_type"] = mur_type
        if mur_disposition_category_id is not None:
            params["mur_disposition_category_id"] = mur_disposition_category_id
        if af_name is not None:
            params["af_name"] = af_name
        if af_committee_id is not None:
            params["af_committee_id"] = af_committee_id
        if af_report_year is not None:
            params["af_report_year"] = af_report_year
        if af_min_rtb_date is not None:
            params["af_min_rtb_date"] = af_min_rtb_date
        if af_max_rtb_date is not None:
            params["af_max_rtb_date"] = af_max_rtb_date
        if af_rtb_fine_amount is not None:
            params["af_rtb_fine_amount"] = af_rtb_fine_amount
        if af_min_fd_date is not None:
            params["af_min_fd_date"] = af_min_fd_date
        if af_max_fd_date is not None:
            params["af_max_fd_date"] = af_max_fd_date
        if af_fd_fine_amount is not None:
            params["af_fd_fine_amount"] = af_fd_fine_amount
        if sort is not None:
            params["sort"] = sort
        if case_min_penalty_amount is not None:
            params["case_min_penalty_amount"] = case_min_penalty_amount
        if case_max_penalty_amount is not None:
            params["case_max_penalty_amount"] = case_max_penalty_amount
        if q_proximity is not None:
            params["q_proximity"] = q_proximity
        if max_gaps is not None:
            params["max_gaps"] = max_gaps
        if proximity_preserve_order is not None:
            params["proximity_preserve_order"] = proximity_preserve_order
        if proximity_filter is not None:
            params["proximity_filter"] = proximity_filter
        if proximity_filter_term is not None:
            params["proximity_filter_term"] = proximity_filter_term
        if filename is not None:
            params["filename"] = filename
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_names_audit_candidates(self, q: List[str], api_key: Optional[str] = None) -> requests.Response:
        """get_v1_names_audit_candidates operation"""
        url = f"{self._base_url}/v1/names/audit_candidates/"
        params = {}
        params["q"] = q
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_names_audit_committees(self, q: List[str], api_key: Optional[str] = None) -> requests.Response:
        """get_v1_names_audit_committees operation"""
        url = f"{self._base_url}/v1/names/audit_committees/"
        params = {}
        params["q"] = q
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_names_candidates(self, q: List[str], api_key: Optional[str] = None) -> requests.Response:
        """get_v1_names_candidates operation"""
        url = f"{self._base_url}/v1/names/candidates/"
        params = {}
        params["q"] = q
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_names_committees(self, q: List[str], api_key: Optional[str] = None) -> requests.Response:
        """get_v1_names_committees operation"""
        url = f"{self._base_url}/v1/names/committees/"
        params = {}
        params["q"] = q
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_national_party_schedule_a(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, contributor_id: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, contributor_name: Optional[List[str]] = None, contributor_city: Optional[List[str]] = None, contributor_state: Optional[List[str]] = None, contributor_zip: Optional[List[str]] = None, contributor_occupation: Optional[List[str]] = None, contributor_employer: Optional[List[str]] = None, image_number: Optional[List[str]] = None, min_contribution_receipt_date: Optional[str] = None, max_contribution_receipt_date: Optional[str] = None, is_individual: Optional[bool] = None, contributor_type: Optional[List[str]] = None, contributor_committee_type: Optional[List[str]] = None, contributor_committee_designation: Optional[List[str]] = None, min_contribution_receipt_amount: Optional[float] = None, max_contribution_receipt_amount: Optional[float] = None, party_account_type: Optional[List[str]] = None, receipt_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_national_party_schedule_a operation"""
        url = f"{self._base_url}/v1/national_party/schedule_a/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if contributor_id is not None:
            params["contributor_id"] = contributor_id
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if contributor_name is not None:
            params["contributor_name"] = contributor_name
        if contributor_city is not None:
            params["contributor_city"] = contributor_city
        if contributor_state is not None:
            params["contributor_state"] = contributor_state
        if contributor_zip is not None:
            params["contributor_zip"] = contributor_zip
        if contributor_occupation is not None:
            params["contributor_occupation"] = contributor_occupation
        if contributor_employer is not None:
            params["contributor_employer"] = contributor_employer
        if image_number is not None:
            params["image_number"] = image_number
        if min_contribution_receipt_date is not None:
            params["min_contribution_receipt_date"] = min_contribution_receipt_date
        if max_contribution_receipt_date is not None:
            params["max_contribution_receipt_date"] = max_contribution_receipt_date
        if is_individual is not None:
            params["is_individual"] = is_individual
        if contributor_type is not None:
            params["contributor_type"] = contributor_type
        if contributor_committee_type is not None:
            params["contributor_committee_type"] = contributor_committee_type
        if contributor_committee_designation is not None:
            params["contributor_committee_designation"] = contributor_committee_designation
        if min_contribution_receipt_amount is not None:
            params["min_contribution_receipt_amount"] = min_contribution_receipt_amount
        if max_contribution_receipt_amount is not None:
            params["max_contribution_receipt_amount"] = max_contribution_receipt_amount
        if party_account_type is not None:
            params["party_account_type"] = party_account_type
        if receipt_type is not None:
            params["receipt_type"] = receipt_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_national_party_schedule_b(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, disbursement_type: Optional[List[str]] = None, disbursement_description: Optional[List[str]] = None, disbursement_purpose_category: Optional[List[str]] = None, image_number: Optional[List[str]] = None, line_number: Optional[str] = None, min_disbursement_amount: Optional[float] = None, max_disbursement_amount: Optional[float] = None, min_disbursement_date: Optional[str] = None, max_disbursement_date: Optional[str] = None, recipient_city: Optional[List[str]] = None, recipient_committee_id: Optional[List[str]] = None, recipient_name: Optional[List[str]] = None, recipient_state: Optional[List[str]] = None, recipient_zip: Optional[List[str]] = None, recipient_committee_designation: Optional[List[str]] = None, recipient_committee_type: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, party_account_type: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_national_party_schedule_b operation"""
        url = f"{self._base_url}/v1/national_party/schedule_b/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if disbursement_type is not None:
            params["disbursement_type"] = disbursement_type
        if disbursement_description is not None:
            params["disbursement_description"] = disbursement_description
        if disbursement_purpose_category is not None:
            params["disbursement_purpose_category"] = disbursement_purpose_category
        if image_number is not None:
            params["image_number"] = image_number
        if line_number is not None:
            params["line_number"] = line_number
        if min_disbursement_amount is not None:
            params["min_disbursement_amount"] = min_disbursement_amount
        if max_disbursement_amount is not None:
            params["max_disbursement_amount"] = max_disbursement_amount
        if min_disbursement_date is not None:
            params["min_disbursement_date"] = min_disbursement_date
        if max_disbursement_date is not None:
            params["max_disbursement_date"] = max_disbursement_date
        if recipient_city is not None:
            params["recipient_city"] = recipient_city
        if recipient_committee_id is not None:
            params["recipient_committee_id"] = recipient_committee_id
        if recipient_name is not None:
            params["recipient_name"] = recipient_name
        if recipient_state is not None:
            params["recipient_state"] = recipient_state
        if recipient_zip is not None:
            params["recipient_zip"] = recipient_zip
        if recipient_committee_designation is not None:
            params["recipient_committee_designation"] = recipient_committee_designation
        if recipient_committee_type is not None:
            params["recipient_committee_type"] = recipient_committee_type
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if party_account_type is not None:
            params["party_account_type"] = party_account_type
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_national_party_totals(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_national_party_totals operation"""
        url = f"{self._base_url}/v1/national_party/totals/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_operations_log(self, page: Optional[int] = None, per_page: Optional[int] = None, candidate_committee_id: Optional[List[str]] = None, report_type: Optional[List[str]] = None, beginning_image_number: Optional[List[str]] = None, report_year: Optional[List[int]] = None, form_type: Optional[List[str]] = None, amendment_indicator: Optional[List[str]] = None, status_num: Optional[List[str]] = None, min_receipt_date: Optional[str] = None, max_receipt_date: Optional[str] = None, min_coverage_end_date: Optional[str] = None, max_coverage_end_date: Optional[str] = None, min_transaction_data_complete_date: Optional[str] = None, max_transaction_data_complete_date: Optional[str] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_operations_log operation"""
        url = f"{self._base_url}/v1/operations-log/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if candidate_committee_id is not None:
            params["candidate_committee_id"] = candidate_committee_id
        if report_type is not None:
            params["report_type"] = report_type
        if beginning_image_number is not None:
            params["beginning_image_number"] = beginning_image_number
        if report_year is not None:
            params["report_year"] = report_year
        if form_type is not None:
            params["form_type"] = form_type
        if amendment_indicator is not None:
            params["amendment_indicator"] = amendment_indicator
        if status_num is not None:
            params["status_num"] = status_num
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if min_coverage_end_date is not None:
            params["min_coverage_end_date"] = min_coverage_end_date
        if max_coverage_end_date is not None:
            params["max_coverage_end_date"] = max_coverage_end_date
        if min_transaction_data_complete_date is not None:
            params["min_transaction_data_complete_date"] = min_transaction_data_complete_date
        if max_transaction_data_complete_date is not None:
            params["max_transaction_data_complete_date"] = max_transaction_data_complete_date
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_presidential_contributions_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, election_year: Optional[List[int]] = None, contributor_state: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_presidential_contributions_by_candidate operation"""
        url = f"{self._base_url}/v1/presidential/contributions/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_year is not None:
            params["election_year"] = election_year
        if contributor_state is not None:
            params["contributor_state"] = contributor_state
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_presidential_contributions_by_size(self, page: Optional[int] = None, per_page: Optional[int] = None, election_year: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, size: Optional[List[int]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_presidential_contributions_by_size operation"""
        url = f"{self._base_url}/v1/presidential/contributions/by_size/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_year is not None:
            params["election_year"] = election_year
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if size is not None:
            params["size"] = size
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_presidential_contributions_by_state(self, page: Optional[int] = None, per_page: Optional[int] = None, election_year: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_presidential_contributions_by_state operation"""
        url = f"{self._base_url}/v1/presidential/contributions/by_state/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_year is not None:
            params["election_year"] = election_year
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_presidential_coverage_end_date(self, page: Optional[int] = None, per_page: Optional[int] = None, election_year: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_presidential_coverage_end_date operation"""
        url = f"{self._base_url}/v1/presidential/coverage_end_date/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_year is not None:
            params["election_year"] = election_year
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_presidential_financial_summary(self, page: Optional[int] = None, per_page: Optional[int] = None, election_year: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_presidential_financial_summary operation"""
        url = f"{self._base_url}/v1/presidential/financial_summary/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if election_year is not None:
            params["election_year"] = election_year
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_rad_analyst(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, analyst_id: Optional[List[int]] = None, analyst_short_id: Optional[List[int]] = None, telephone_ext: Optional[List[int]] = None, name: Optional[List[str]] = None, email: Optional[List[str]] = None, title: Optional[List[str]] = None, min_assignment_update_date: Optional[str] = None, max_assignment_update_date: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_rad_analyst operation"""
        url = f"{self._base_url}/v1/rad-analyst/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if analyst_id is not None:
            params["analyst_id"] = analyst_id
        if analyst_short_id is not None:
            params["analyst_short_id"] = analyst_short_id
        if telephone_ext is not None:
            params["telephone_ext"] = telephone_ext
        if name is not None:
            params["name"] = name
        if email is not None:
            params["email"] = email
        if title is not None:
            params["title"] = title
        if min_assignment_update_date is not None:
            params["min_assignment_update_date"] = min_assignment_update_date
        if max_assignment_update_date is not None:
            params["max_assignment_update_date"] = max_assignment_update_date
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_reporting_dates(self, page: Optional[int] = None, per_page: Optional[int] = None, min_due_date: Optional[str] = None, max_due_date: Optional[str] = None, report_year: Optional[List[int]] = None, report_type: Optional[List[str]] = None, min_create_date: Optional[str] = None, max_create_date: Optional[str] = None, min_update_date: Optional[str] = None, max_update_date: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_reporting_dates operation"""
        url = f"{self._base_url}/v1/reporting-dates/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if min_due_date is not None:
            params["min_due_date"] = min_due_date
        if max_due_date is not None:
            params["max_due_date"] = max_due_date
        if report_year is not None:
            params["report_year"] = report_year
        if report_type is not None:
            params["report_type"] = report_type
        if min_create_date is not None:
            params["min_create_date"] = min_create_date
        if max_create_date is not None:
            params["max_create_date"] = max_create_date
        if min_update_date is not None:
            params["min_update_date"] = min_update_date
        if max_update_date is not None:
            params["max_update_date"] = max_update_date
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_reports_entity_type(self, entity_type: str, page: Optional[int] = None, per_page: Optional[int] = None, year: Optional[List[int]] = None, cycle: Optional[List[int]] = None, beginning_image_number: Optional[List[str]] = None, report_type: Optional[List[str]] = None, is_amended: Optional[bool] = None, most_recent: Optional[bool] = None, filer_type: Optional[str] = None, min_disbursements_amount: Optional[float] = None, max_disbursements_amount: Optional[float] = None, min_receipts_amount: Optional[float] = None, max_receipts_amount: Optional[float] = None, max_receipt_date: Optional[str] = None, min_receipt_date: Optional[str] = None, min_cash_on_hand_end_period_amount: Optional[float] = None, max_cash_on_hand_end_period_amount: Optional[float] = None, min_debts_owed_amount: Optional[float] = None, max_debts_owed_expenditures: Optional[float] = None, min_independent_expenditures: Optional[float] = None, max_independent_expenditures: Optional[float] = None, min_party_coordinated_expenditures: Optional[float] = None, max_party_coordinated_expenditures: Optional[float] = None, min_total_contributions: Optional[float] = None, max_total_contributions: Optional[float] = None, committee_type: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, amendment_indicator: Optional[List[str]] = None, q_filer: Optional[List[str]] = None, q_spender: Optional[List[str]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_reports_entity_type operation"""
        url = f"{self._base_url}/v1/reports/{entity_type}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if year is not None:
            params["year"] = year
        if cycle is not None:
            params["cycle"] = cycle
        if beginning_image_number is not None:
            params["beginning_image_number"] = beginning_image_number
        if report_type is not None:
            params["report_type"] = report_type
        if is_amended is not None:
            params["is_amended"] = is_amended
        if most_recent is not None:
            params["most_recent"] = most_recent
        if filer_type is not None:
            params["filer_type"] = filer_type
        if min_disbursements_amount is not None:
            params["min_disbursements_amount"] = min_disbursements_amount
        if max_disbursements_amount is not None:
            params["max_disbursements_amount"] = max_disbursements_amount
        if min_receipts_amount is not None:
            params["min_receipts_amount"] = min_receipts_amount
        if max_receipts_amount is not None:
            params["max_receipts_amount"] = max_receipts_amount
        if max_receipt_date is not None:
            params["max_receipt_date"] = max_receipt_date
        if min_receipt_date is not None:
            params["min_receipt_date"] = min_receipt_date
        if min_cash_on_hand_end_period_amount is not None:
            params["min_cash_on_hand_end_period_amount"] = min_cash_on_hand_end_period_amount
        if max_cash_on_hand_end_period_amount is not None:
            params["max_cash_on_hand_end_period_amount"] = max_cash_on_hand_end_period_amount
        if min_debts_owed_amount is not None:
            params["min_debts_owed_amount"] = min_debts_owed_amount
        if max_debts_owed_expenditures is not None:
            params["max_debts_owed_expenditures"] = max_debts_owed_expenditures
        if min_independent_expenditures is not None:
            params["min_independent_expenditures"] = min_independent_expenditures
        if max_independent_expenditures is not None:
            params["max_independent_expenditures"] = max_independent_expenditures
        if min_party_coordinated_expenditures is not None:
            params["min_party_coordinated_expenditures"] = min_party_coordinated_expenditures
        if max_party_coordinated_expenditures is not None:
            params["max_party_coordinated_expenditures"] = max_party_coordinated_expenditures
        if min_total_contributions is not None:
            params["min_total_contributions"] = min_total_contributions
        if max_total_contributions is not None:
            params["max_total_contributions"] = max_total_contributions
        if committee_type is not None:
            params["committee_type"] = committee_type
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if committee_id is not None:
            params["committee_id"] = committee_id
        if amendment_indicator is not None:
            params["amendment_indicator"] = amendment_indicator
        if q_filer is not None:
            params["q_filer"] = q_filer
        if q_spender is not None:
            params["q_spender"] = q_spender
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, committee_id: Optional[List[str]] = None, contributor_id: Optional[List[str]] = None, contributor_name: Optional[List[str]] = None, contributor_city: Optional[List[str]] = None, contributor_state: Optional[List[str]] = None, contributor_zip: Optional[List[str]] = None, contributor_employer: Optional[List[str]] = None, contributor_occupation: Optional[List[str]] = None, last_contribution_receipt_date: Optional[str] = None, last_contribution_receipt_amount: Optional[float] = None, line_number: Optional[str] = None, is_individual: Optional[bool] = None, contributor_type: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, recipient_committee_type: Optional[List[str]] = None, recipient_committee_org_type: Optional[List[str]] = None, recipient_committee_designation: Optional[List[str]] = None, min_load_date: Optional[str] = None, max_load_date: Optional[str] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if committee_id is not None:
            params["committee_id"] = committee_id
        if contributor_id is not None:
            params["contributor_id"] = contributor_id
        if contributor_name is not None:
            params["contributor_name"] = contributor_name
        if contributor_city is not None:
            params["contributor_city"] = contributor_city
        if contributor_state is not None:
            params["contributor_state"] = contributor_state
        if contributor_zip is not None:
            params["contributor_zip"] = contributor_zip
        if contributor_employer is not None:
            params["contributor_employer"] = contributor_employer
        if contributor_occupation is not None:
            params["contributor_occupation"] = contributor_occupation
        if last_contribution_receipt_date is not None:
            params["last_contribution_receipt_date"] = last_contribution_receipt_date
        if last_contribution_receipt_amount is not None:
            params["last_contribution_receipt_amount"] = last_contribution_receipt_amount
        if line_number is not None:
            params["line_number"] = line_number
        if is_individual is not None:
            params["is_individual"] = is_individual
        if contributor_type is not None:
            params["contributor_type"] = contributor_type
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if recipient_committee_type is not None:
            params["recipient_committee_type"] = recipient_committee_type
        if recipient_committee_org_type is not None:
            params["recipient_committee_org_type"] = recipient_committee_org_type
        if recipient_committee_designation is not None:
            params["recipient_committee_designation"] = recipient_committee_designation
        if min_load_date is not None:
            params["min_load_date"] = min_load_date
        if max_load_date is not None:
            params["max_load_date"] = max_load_date
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_employer(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, employer: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_employer operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_employer/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if employer is not None:
            params["employer"] = employer
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_occupation(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, occupation: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_occupation operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_occupation/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if occupation is not None:
            params["occupation"] = occupation
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_size(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, size: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_size operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_size/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if size is not None:
            params["size"] = size
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_size_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, candidate_id: List[str], cycle: List[int], election_full: Optional[bool] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_size_by_candidate operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_size/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        params["candidate_id"] = candidate_id
        params["cycle"] = cycle
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_state(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, state: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, hide_null: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_state operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_state/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if state is not None:
            params["state"] = state
        if committee_id is not None:
            params["committee_id"] = committee_id
        if hide_null is not None:
            params["hide_null"] = hide_null
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_state_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, candidate_id: List[str], cycle: List[int], election_full: Optional[bool] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_state_by_candidate operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_state/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        params["candidate_id"] = candidate_id
        params["cycle"] = cycle
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_state_by_candidate_totals(self, page: Optional[int] = None, per_page: Optional[int] = None, candidate_id: List[str], cycle: List[int], election_full: Optional[bool] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_state_by_candidate_totals operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_state/by_candidate/totals/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        params["candidate_id"] = candidate_id
        params["cycle"] = cycle
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_state_totals(self, cycle: Optional[List[int]] = None, state: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_state_totals operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_state/totals/"
        params = {}
        if cycle is not None:
            params["cycle"] = cycle
        if state is not None:
            params["state"] = state
        if committee_type is not None:
            params["committee_type"] = committee_type
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_by_zip(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, zip: Optional[List[str]] = None, state: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_by_zip operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/by_zip/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if zip is not None:
            params["zip"] = zip
        if state is not None:
            params["state"] = state
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_efile(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, contributor_name: Optional[List[str]] = None, contributor_city: Optional[List[str]] = None, contributor_state: Optional[List[str]] = None, contributor_employer: Optional[List[str]] = None, contributor_occupation: Optional[List[str]] = None, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_efile operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/efile/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if contributor_name is not None:
            params["contributor_name"] = contributor_name
        if contributor_city is not None:
            params["contributor_city"] = contributor_city
        if contributor_state is not None:
            params["contributor_state"] = contributor_state
        if contributor_employer is not None:
            params["contributor_employer"] = contributor_employer
        if contributor_occupation is not None:
            params["contributor_occupation"] = contributor_occupation
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_sub_id(self, sub_id: str, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, committee_id: Optional[List[str]] = None, contributor_id: Optional[List[str]] = None, contributor_name: Optional[List[str]] = None, contributor_city: Optional[List[str]] = None, contributor_state: Optional[List[str]] = None, contributor_zip: Optional[List[str]] = None, contributor_employer: Optional[List[str]] = None, contributor_occupation: Optional[List[str]] = None, last_contribution_receipt_date: Optional[str] = None, last_contribution_receipt_amount: Optional[float] = None, line_number: Optional[str] = None, is_individual: Optional[bool] = None, contributor_type: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, recipient_committee_type: Optional[List[str]] = None, recipient_committee_org_type: Optional[List[str]] = None, recipient_committee_designation: Optional[List[str]] = None, min_load_date: Optional[str] = None, max_load_date: Optional[str] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_sub_id operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a/{sub_id}/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if committee_id is not None:
            params["committee_id"] = committee_id
        if contributor_id is not None:
            params["contributor_id"] = contributor_id
        if contributor_name is not None:
            params["contributor_name"] = contributor_name
        if contributor_city is not None:
            params["contributor_city"] = contributor_city
        if contributor_state is not None:
            params["contributor_state"] = contributor_state
        if contributor_zip is not None:
            params["contributor_zip"] = contributor_zip
        if contributor_employer is not None:
            params["contributor_employer"] = contributor_employer
        if contributor_occupation is not None:
            params["contributor_occupation"] = contributor_occupation
        if last_contribution_receipt_date is not None:
            params["last_contribution_receipt_date"] = last_contribution_receipt_date
        if last_contribution_receipt_amount is not None:
            params["last_contribution_receipt_amount"] = last_contribution_receipt_amount
        if line_number is not None:
            params["line_number"] = line_number
        if is_individual is not None:
            params["is_individual"] = is_individual
        if contributor_type is not None:
            params["contributor_type"] = contributor_type
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if recipient_committee_type is not None:
            params["recipient_committee_type"] = recipient_committee_type
        if recipient_committee_org_type is not None:
            params["recipient_committee_org_type"] = recipient_committee_org_type
        if recipient_committee_designation is not None:
            params["recipient_committee_designation"] = recipient_committee_designation
        if min_load_date is not None:
            params["min_load_date"] = min_load_date
        if max_load_date is not None:
            params["max_load_date"] = max_load_date
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_a_form5(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, contributor_name: Optional[List[str]] = None, contributor_city: Optional[List[str]] = None, contributor_state: Optional[List[str]] = None, contributor_zip: Optional[List[str]] = None, contributor_employer: Optional[List[str]] = None, contributor_occupation: Optional[List[str]] = None, last_contribution_receipt_date: Optional[str] = None, last_contribution_amount: Optional[float] = None, report_year: Optional[List[int]] = None, report_type: Optional[List[str]] = None, contributor_type: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_a_form5 operation"""
        url = f"{self._base_url}/v1/schedules/schedule_a_form5/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if contributor_name is not None:
            params["contributor_name"] = contributor_name
        if contributor_city is not None:
            params["contributor_city"] = contributor_city
        if contributor_state is not None:
            params["contributor_state"] = contributor_state
        if contributor_zip is not None:
            params["contributor_zip"] = contributor_zip
        if contributor_employer is not None:
            params["contributor_employer"] = contributor_employer
        if contributor_occupation is not None:
            params["contributor_occupation"] = contributor_occupation
        if last_contribution_receipt_date is not None:
            params["last_contribution_receipt_date"] = last_contribution_receipt_date
        if last_contribution_amount is not None:
            params["last_contribution_amount"] = last_contribution_amount
        if report_year is not None:
            params["report_year"] = report_year
        if report_type is not None:
            params["report_type"] = report_type
        if contributor_type is not None:
            params["contributor_type"] = contributor_type
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_b(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, committee_id: Optional[List[str]] = None, disbursement_description: Optional[List[str]] = None, disbursement_purpose_category: Optional[List[str]] = None, last_disbursement_amount: Optional[float] = None, last_disbursement_date: Optional[str] = None, line_number: Optional[str] = None, recipient_city: Optional[List[str]] = None, recipient_committee_id: Optional[List[str]] = None, recipient_name: Optional[List[str]] = None, recipient_state: Optional[List[str]] = None, spender_committee_designation: Optional[List[str]] = None, spender_committee_org_type: Optional[List[str]] = None, spender_committee_type: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_b operation"""
        url = f"{self._base_url}/v1/schedules/schedule_b/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if committee_id is not None:
            params["committee_id"] = committee_id
        if disbursement_description is not None:
            params["disbursement_description"] = disbursement_description
        if disbursement_purpose_category is not None:
            params["disbursement_purpose_category"] = disbursement_purpose_category
        if last_disbursement_amount is not None:
            params["last_disbursement_amount"] = last_disbursement_amount
        if last_disbursement_date is not None:
            params["last_disbursement_date"] = last_disbursement_date
        if line_number is not None:
            params["line_number"] = line_number
        if recipient_city is not None:
            params["recipient_city"] = recipient_city
        if recipient_committee_id is not None:
            params["recipient_committee_id"] = recipient_committee_id
        if recipient_name is not None:
            params["recipient_name"] = recipient_name
        if recipient_state is not None:
            params["recipient_state"] = recipient_state
        if spender_committee_designation is not None:
            params["spender_committee_designation"] = spender_committee_designation
        if spender_committee_org_type is not None:
            params["spender_committee_org_type"] = spender_committee_org_type
        if spender_committee_type is not None:
            params["spender_committee_type"] = spender_committee_type
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_b_by_purpose(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, purpose: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_b_by_purpose operation"""
        url = f"{self._base_url}/v1/schedules/schedule_b/by_purpose/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if purpose is not None:
            params["purpose"] = purpose
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_b_by_recipient(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, recipient_name: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_b_by_recipient operation"""
        url = f"{self._base_url}/v1/schedules/schedule_b/by_recipient/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if recipient_name is not None:
            params["recipient_name"] = recipient_name
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_b_by_recipient_id(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, recipient_id: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_b_by_recipient_id operation"""
        url = f"{self._base_url}/v1/schedules/schedule_b/by_recipient_id/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if recipient_id is not None:
            params["recipient_id"] = recipient_id
        if committee_id is not None:
            params["committee_id"] = committee_id
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_b_efile(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, disbursement_description: Optional[List[str]] = None, image_number: Optional[List[str]] = None, recipient_city: Optional[List[str]] = None, recipient_state: Optional[List[str]] = None, max_date: Optional[str] = None, min_date: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_b_efile operation"""
        url = f"{self._base_url}/v1/schedules/schedule_b/efile/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if disbursement_description is not None:
            params["disbursement_description"] = disbursement_description
        if image_number is not None:
            params["image_number"] = image_number
        if recipient_city is not None:
            params["recipient_city"] = recipient_city
        if recipient_state is not None:
            params["recipient_state"] = recipient_state
        if max_date is not None:
            params["max_date"] = max_date
        if min_date is not None:
            params["min_date"] = min_date
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_b_sub_id(self, sub_id: str, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, committee_id: Optional[List[str]] = None, disbursement_description: Optional[List[str]] = None, disbursement_purpose_category: Optional[List[str]] = None, last_disbursement_amount: Optional[float] = None, last_disbursement_date: Optional[str] = None, line_number: Optional[str] = None, recipient_city: Optional[List[str]] = None, recipient_committee_id: Optional[List[str]] = None, recipient_name: Optional[List[str]] = None, recipient_state: Optional[List[str]] = None, spender_committee_designation: Optional[List[str]] = None, spender_committee_org_type: Optional[List[str]] = None, spender_committee_type: Optional[List[str]] = None, two_year_transaction_period: Optional[List[int]] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_b_sub_id operation"""
        url = f"{self._base_url}/v1/schedules/schedule_b/{sub_id}/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if committee_id is not None:
            params["committee_id"] = committee_id
        if disbursement_description is not None:
            params["disbursement_description"] = disbursement_description
        if disbursement_purpose_category is not None:
            params["disbursement_purpose_category"] = disbursement_purpose_category
        if last_disbursement_amount is not None:
            params["last_disbursement_amount"] = last_disbursement_amount
        if last_disbursement_date is not None:
            params["last_disbursement_date"] = last_disbursement_date
        if line_number is not None:
            params["line_number"] = line_number
        if recipient_city is not None:
            params["recipient_city"] = recipient_city
        if recipient_committee_id is not None:
            params["recipient_committee_id"] = recipient_committee_id
        if recipient_name is not None:
            params["recipient_name"] = recipient_name
        if recipient_state is not None:
            params["recipient_state"] = recipient_state
        if spender_committee_designation is not None:
            params["spender_committee_designation"] = spender_committee_designation
        if spender_committee_org_type is not None:
            params["spender_committee_org_type"] = spender_committee_org_type
        if spender_committee_type is not None:
            params["spender_committee_type"] = spender_committee_type
        if two_year_transaction_period is not None:
            params["two_year_transaction_period"] = two_year_transaction_period
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_c(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, committee_id: Optional[List[str]] = None, candidate_name: Optional[List[str]] = None, loan_source_name: Optional[List[str]] = None, min_payment_to_date: Optional[int] = None, max_payment_to_date: Optional[int] = None, min_incurred_date: Optional[str] = None, max_incurred_date: Optional[str] = None, form_line_number: Optional[List[str]] = None, page: Optional[int] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_c operation"""
        url = f"{self._base_url}/v1/schedules/schedule_c/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_name is not None:
            params["candidate_name"] = candidate_name
        if loan_source_name is not None:
            params["loan_source_name"] = loan_source_name
        if min_payment_to_date is not None:
            params["min_payment_to_date"] = min_payment_to_date
        if max_payment_to_date is not None:
            params["max_payment_to_date"] = max_payment_to_date
        if min_incurred_date is not None:
            params["min_incurred_date"] = min_incurred_date
        if max_incurred_date is not None:
            params["max_incurred_date"] = max_incurred_date
        if form_line_number is not None:
            params["form_line_number"] = form_line_number
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_c_sub_id(self, sub_id: str, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_c_sub_id operation"""
        url = f"{self._base_url}/v1/schedules/schedule_c/{sub_id}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_d(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_payment_period: Optional[float] = None, max_payment_period: Optional[float] = None, min_amount_incurred: Optional[float] = None, max_amount_incurred: Optional[float] = None, min_amount_outstanding_beginning: Optional[float] = None, max_amount_outstanding_beginning: Optional[float] = None, min_amount_outstanding_close: Optional[float] = None, max_amount_outstanding_close: Optional[float] = None, creditor_debtor_name: Optional[List[str]] = None, nature_of_debt: Optional[str] = None, committee_id: Optional[List[str]] = None, min_coverage_end_date: Optional[str] = None, max_coverage_end_date: Optional[str] = None, min_coverage_start_date: Optional[str] = None, max_coverage_start_date: Optional[str] = None, report_year: Optional[List[int]] = None, report_type: Optional[List[str]] = None, form_line_number: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, filing_form: Optional[List[str]] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_d operation"""
        url = f"{self._base_url}/v1/schedules/schedule_d/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_payment_period is not None:
            params["min_payment_period"] = min_payment_period
        if max_payment_period is not None:
            params["max_payment_period"] = max_payment_period
        if min_amount_incurred is not None:
            params["min_amount_incurred"] = min_amount_incurred
        if max_amount_incurred is not None:
            params["max_amount_incurred"] = max_amount_incurred
        if min_amount_outstanding_beginning is not None:
            params["min_amount_outstanding_beginning"] = min_amount_outstanding_beginning
        if max_amount_outstanding_beginning is not None:
            params["max_amount_outstanding_beginning"] = max_amount_outstanding_beginning
        if min_amount_outstanding_close is not None:
            params["min_amount_outstanding_close"] = min_amount_outstanding_close
        if max_amount_outstanding_close is not None:
            params["max_amount_outstanding_close"] = max_amount_outstanding_close
        if creditor_debtor_name is not None:
            params["creditor_debtor_name"] = creditor_debtor_name
        if nature_of_debt is not None:
            params["nature_of_debt"] = nature_of_debt
        if committee_id is not None:
            params["committee_id"] = committee_id
        if min_coverage_end_date is not None:
            params["min_coverage_end_date"] = min_coverage_end_date
        if max_coverage_end_date is not None:
            params["max_coverage_end_date"] = max_coverage_end_date
        if min_coverage_start_date is not None:
            params["min_coverage_start_date"] = min_coverage_start_date
        if max_coverage_start_date is not None:
            params["max_coverage_start_date"] = max_coverage_start_date
        if report_year is not None:
            params["report_year"] = report_year
        if report_type is not None:
            params["report_type"] = report_type
        if form_line_number is not None:
            params["form_line_number"] = form_line_number
        if committee_type is not None:
            params["committee_type"] = committee_type
        if filing_form is not None:
            params["filing_form"] = filing_form
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_d_sub_id(self, sub_id: str, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_d_sub_id operation"""
        url = f"{self._base_url}/v1/schedules/schedule_d/{sub_id}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_e(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, candidate_office: Optional[List[str]] = None, candidate_party: Optional[List[str]] = None, candidate_office_state: Optional[List[str]] = None, candidate_office_district: Optional[List[str]] = None, cycle: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, filing_form: Optional[List[str]] = None, last_expenditure_date: Optional[str] = None, last_expenditure_amount: Optional[float] = None, last_office_total_ytd: Optional[float] = None, payee_name: Optional[List[str]] = None, support_oppose_indicator: Optional[List[str]] = None, last_support_oppose_indicator: Optional[str] = None, is_notice: Optional[List[bool]] = None, min_dissemination_date: Optional[str] = None, max_dissemination_date: Optional[str] = None, min_filing_date: Optional[str] = None, max_filing_date: Optional[str] = None, most_recent: Optional[bool] = None, q_spender: Optional[List[str]] = None, form_line_number: Optional[List[str]] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_e operation"""
        url = f"{self._base_url}/v1/schedules/schedule_e/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if candidate_office is not None:
            params["candidate_office"] = candidate_office
        if candidate_party is not None:
            params["candidate_party"] = candidate_party
        if candidate_office_state is not None:
            params["candidate_office_state"] = candidate_office_state
        if candidate_office_district is not None:
            params["candidate_office_district"] = candidate_office_district
        if cycle is not None:
            params["cycle"] = cycle
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if filing_form is not None:
            params["filing_form"] = filing_form
        if last_expenditure_date is not None:
            params["last_expenditure_date"] = last_expenditure_date
        if last_expenditure_amount is not None:
            params["last_expenditure_amount"] = last_expenditure_amount
        if last_office_total_ytd is not None:
            params["last_office_total_ytd"] = last_office_total_ytd
        if payee_name is not None:
            params["payee_name"] = payee_name
        if support_oppose_indicator is not None:
            params["support_oppose_indicator"] = support_oppose_indicator
        if last_support_oppose_indicator is not None:
            params["last_support_oppose_indicator"] = last_support_oppose_indicator
        if is_notice is not None:
            params["is_notice"] = is_notice
        if min_dissemination_date is not None:
            params["min_dissemination_date"] = min_dissemination_date
        if max_dissemination_date is not None:
            params["max_dissemination_date"] = max_dissemination_date
        if min_filing_date is not None:
            params["min_filing_date"] = min_filing_date
        if max_filing_date is not None:
            params["max_filing_date"] = max_filing_date
        if most_recent is not None:
            params["most_recent"] = most_recent
        if q_spender is not None:
            params["q_spender"] = q_spender
        if form_line_number is not None:
            params["form_line_number"] = form_line_number
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_e_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, state: Optional[str] = None, district: Optional[str] = None, cycle: Optional[List[int]] = None, office: Optional[str] = None, election_full: Optional[bool] = None, candidate_id: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, support_oppose: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_e_by_candidate operation"""
        url = f"{self._base_url}/v1/schedules/schedule_e/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if state is not None:
            params["state"] = state
        if district is not None:
            params["district"] = district
        if cycle is not None:
            params["cycle"] = cycle
        if office is not None:
            params["office"] = office
        if election_full is not None:
            params["election_full"] = election_full
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if committee_id is not None:
            params["committee_id"] = committee_id
        if support_oppose is not None:
            params["support_oppose"] = support_oppose
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_e_efile(self, page: Optional[int] = None, per_page: Optional[int] = None, candidate_search: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, candidate_id: Optional[List[str]] = None, payee_name: Optional[List[str]] = None, image_number: Optional[List[str]] = None, support_oppose_indicator: Optional[List[str]] = None, min_expenditure_date: Optional[str] = None, max_expenditure_date: Optional[str] = None, min_dissemination_date: Optional[str] = None, max_dissemination_date: Optional[str] = None, min_expenditure_amount: Optional[int] = None, max_expenditure_amount: Optional[int] = None, spender_name: Optional[List[str]] = None, candidate_party: Optional[List[str]] = None, candidate_office: Optional[str] = None, candidate_office_state: Optional[List[str]] = None, candidate_office_district: Optional[List[str]] = None, most_recent: Optional[bool] = None, min_filed_date: Optional[str] = None, max_filed_date: Optional[str] = None, filing_form: Optional[List[str]] = None, is_notice: Optional[bool] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_e_efile operation"""
        url = f"{self._base_url}/v1/schedules/schedule_e/efile/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if candidate_search is not None:
            params["candidate_search"] = candidate_search
        if committee_id is not None:
            params["committee_id"] = committee_id
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if payee_name is not None:
            params["payee_name"] = payee_name
        if image_number is not None:
            params["image_number"] = image_number
        if support_oppose_indicator is not None:
            params["support_oppose_indicator"] = support_oppose_indicator
        if min_expenditure_date is not None:
            params["min_expenditure_date"] = min_expenditure_date
        if max_expenditure_date is not None:
            params["max_expenditure_date"] = max_expenditure_date
        if min_dissemination_date is not None:
            params["min_dissemination_date"] = min_dissemination_date
        if max_dissemination_date is not None:
            params["max_dissemination_date"] = max_dissemination_date
        if min_expenditure_amount is not None:
            params["min_expenditure_amount"] = min_expenditure_amount
        if max_expenditure_amount is not None:
            params["max_expenditure_amount"] = max_expenditure_amount
        if spender_name is not None:
            params["spender_name"] = spender_name
        if candidate_party is not None:
            params["candidate_party"] = candidate_party
        if candidate_office is not None:
            params["candidate_office"] = candidate_office
        if candidate_office_state is not None:
            params["candidate_office_state"] = candidate_office_state
        if candidate_office_district is not None:
            params["candidate_office_district"] = candidate_office_district
        if most_recent is not None:
            params["most_recent"] = most_recent
        if min_filed_date is not None:
            params["min_filed_date"] = min_filed_date
        if max_filed_date is not None:
            params["max_filed_date"] = max_filed_date
        if filing_form is not None:
            params["filing_form"] = filing_form
        if is_notice is not None:
            params["is_notice"] = is_notice
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_e_totals_by_candidate(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, candidate_id: Optional[List[str]] = None, election_full: Optional[bool] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_e_totals_by_candidate operation"""
        url = f"{self._base_url}/v1/schedules/schedule_e/totals/by_candidate/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if election_full is not None:
            params["election_full"] = election_full
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_f(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, candidate_id: Optional[List[str]] = None, payee_name: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, cycle: Optional[List[int]] = None, form_line_number: Optional[List[str]] = None, page: Optional[int] = None, per_page: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_f operation"""
        url = f"{self._base_url}/v1/schedules/schedule_f/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if candidate_id is not None:
            params["candidate_id"] = candidate_id
        if payee_name is not None:
            params["payee_name"] = payee_name
        if committee_id is not None:
            params["committee_id"] = committee_id
        if cycle is not None:
            params["cycle"] = cycle
        if form_line_number is not None:
            params["form_line_number"] = form_line_number
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_f_sub_id(self, sub_id: str, page: Optional[int] = None, per_page: Optional[int] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_f_sub_id operation"""
        url = f"{self._base_url}/v1/schedules/schedule_f/{sub_id}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_h4(self, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, report_year: Optional[List[int]] = None, report_type: Optional[List[str]] = None, activity_or_event: Optional[List[str]] = None, q_payee_name: Optional[List[str]] = None, payee_city: Optional[List[str]] = None, payee_zip: Optional[List[str]] = None, payee_state: Optional[List[str]] = None, q_disbursement_purpose: Optional[List[str]] = None, cycle: Optional[List[int]] = None, committee_id: Optional[List[str]] = None, last_payee_name: Optional[List[str]] = None, last_disbursement_purpose: Optional[List[str]] = None, last_event_purpose_date: Optional[str] = None, last_spender_committee_name: Optional[List[str]] = None, last_disbursement_amount: Optional[float] = None, administrative_voter_drive_activity_indicator: Optional[List[str]] = None, fundraising_activity_indicator: Optional[List[str]] = None, exempt_activity_indicator: Optional[List[str]] = None, direct_candidate_support_activity_indicator: Optional[List[str]] = None, administrative_activity_indicator: Optional[List[str]] = None, general_voter_drive_activity_indicator: Optional[List[str]] = None, public_comm_indicator: Optional[List[str]] = None, spender_committee_name: Optional[List[str]] = None, spender_committee_type: Optional[List[str]] = None, spender_committee_designation: Optional[List[str]] = None, form_line_number: Optional[List[str]] = None, per_page: Optional[int] = None, last_index: Optional[int] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_h4 operation"""
        url = f"{self._base_url}/v1/schedules/schedule_h4/"
        params = {}
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if report_year is not None:
            params["report_year"] = report_year
        if report_type is not None:
            params["report_type"] = report_type
        if activity_or_event is not None:
            params["activity_or_event"] = activity_or_event
        if q_payee_name is not None:
            params["q_payee_name"] = q_payee_name
        if payee_city is not None:
            params["payee_city"] = payee_city
        if payee_zip is not None:
            params["payee_zip"] = payee_zip
        if payee_state is not None:
            params["payee_state"] = payee_state
        if q_disbursement_purpose is not None:
            params["q_disbursement_purpose"] = q_disbursement_purpose
        if cycle is not None:
            params["cycle"] = cycle
        if committee_id is not None:
            params["committee_id"] = committee_id
        if last_payee_name is not None:
            params["last_payee_name"] = last_payee_name
        if last_disbursement_purpose is not None:
            params["last_disbursement_purpose"] = last_disbursement_purpose
        if last_event_purpose_date is not None:
            params["last_event_purpose_date"] = last_event_purpose_date
        if last_spender_committee_name is not None:
            params["last_spender_committee_name"] = last_spender_committee_name
        if last_disbursement_amount is not None:
            params["last_disbursement_amount"] = last_disbursement_amount
        if administrative_voter_drive_activity_indicator is not None:
            params["administrative_voter_drive_activity_indicator"] = administrative_voter_drive_activity_indicator
        if fundraising_activity_indicator is not None:
            params["fundraising_activity_indicator"] = fundraising_activity_indicator
        if exempt_activity_indicator is not None:
            params["exempt_activity_indicator"] = exempt_activity_indicator
        if direct_candidate_support_activity_indicator is not None:
            params["direct_candidate_support_activity_indicator"] = direct_candidate_support_activity_indicator
        if administrative_activity_indicator is not None:
            params["administrative_activity_indicator"] = administrative_activity_indicator
        if general_voter_drive_activity_indicator is not None:
            params["general_voter_drive_activity_indicator"] = general_voter_drive_activity_indicator
        if public_comm_indicator is not None:
            params["public_comm_indicator"] = public_comm_indicator
        if spender_committee_name is not None:
            params["spender_committee_name"] = spender_committee_name
        if spender_committee_type is not None:
            params["spender_committee_type"] = spender_committee_type
        if spender_committee_designation is not None:
            params["spender_committee_designation"] = spender_committee_designation
        if form_line_number is not None:
            params["form_line_number"] = form_line_number
        if per_page is not None:
            params["per_page"] = per_page
        if last_index is not None:
            params["last_index"] = last_index
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_schedules_schedule_h4_efile(self, page: Optional[int] = None, per_page: Optional[int] = None, image_number: Optional[List[str]] = None, min_image_number: Optional[str] = None, max_image_number: Optional[str] = None, payee_city: Optional[List[str]] = None, payee_zip: Optional[List[str]] = None, payee_state: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, last_disbursement_purpose: Optional[List[str]] = None, last_event_purpose_date: Optional[str] = None, min_date: Optional[str] = None, max_date: Optional[str] = None, last_disbursement_amount: Optional[float] = None, min_amount: Optional[float] = None, max_amount: Optional[float] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_schedules_schedule_h4_efile operation"""
        url = f"{self._base_url}/v1/schedules/schedule_h4/efile/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if image_number is not None:
            params["image_number"] = image_number
        if min_image_number is not None:
            params["min_image_number"] = min_image_number
        if max_image_number is not None:
            params["max_image_number"] = max_image_number
        if payee_city is not None:
            params["payee_city"] = payee_city
        if payee_zip is not None:
            params["payee_zip"] = payee_zip
        if payee_state is not None:
            params["payee_state"] = payee_state
        if committee_id is not None:
            params["committee_id"] = committee_id
        if last_disbursement_purpose is not None:
            params["last_disbursement_purpose"] = last_disbursement_purpose
        if last_event_purpose_date is not None:
            params["last_event_purpose_date"] = last_event_purpose_date
        if min_date is not None:
            params["min_date"] = min_date
        if max_date is not None:
            params["max_date"] = max_date
        if last_disbursement_amount is not None:
            params["last_disbursement_amount"] = last_disbursement_amount
        if min_amount is not None:
            params["min_amount"] = min_amount
        if max_amount is not None:
            params["max_amount"] = max_amount
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_state_election_office(self, page: Optional[int] = None, per_page: Optional[int] = None, state: str, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_state_election_office operation"""
        url = f"{self._base_url}/v1/state-election-office/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        params["state"] = state
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_totals_by_entity(self, page: Optional[int] = None, per_page: Optional[int] = None, cycle: int, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_totals_by_entity operation"""
        url = f"{self._base_url}/v1/totals/by_entity/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        params["cycle"] = cycle
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_totals_inaugural_committees_by_contributor(self, page: Optional[int] = None, per_page: Optional[int] = None, committee_id: Optional[List[str]] = None, contributor_name: Optional[List[str]] = None, cycle: Optional[List[int]] = None, sort: Optional[List[str]] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_totals_inaugural_committees_by_contributor operation"""
        url = f"{self._base_url}/v1/totals/inaugural_committees/by_contributor/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if committee_id is not None:
            params["committee_id"] = committee_id
        if contributor_name is not None:
            params["contributor_name"] = contributor_name
        if cycle is not None:
            params["cycle"] = cycle
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())

    def get_v1_totals_entity_type(self, entity_type: str, page: Optional[int] = None, per_page: Optional[int] = None, cycle: Optional[List[int]] = None, committee_designation: Optional[List[str]] = None, committee_id: Optional[List[str]] = None, committee_type: Optional[List[str]] = None, committee_state: Optional[List[str]] = None, filing_frequency: Optional[List[str]] = None, treasurer_name: Optional[List[str]] = None, min_disbursements: Optional[float] = None, max_disbursements: Optional[float] = None, min_receipts: Optional[float] = None, max_receipts: Optional[float] = None, min_last_cash_on_hand_end_period: Optional[float] = None, max_last_cash_on_hand_end_period: Optional[float] = None, min_last_debts_owed_by_committee: Optional[float] = None, max_last_debts_owed_by_committee: Optional[float] = None, sponsor_candidate_id: Optional[List[str]] = None, organization_type: Optional[List[str]] = None, min_first_f1_date: Optional[str] = None, max_first_f1_date: Optional[str] = None, sort: Optional[str] = None, sort_hide_null: Optional[bool] = None, sort_null_only: Optional[bool] = None, sort_nulls_last: Optional[bool] = None, api_key: Optional[str] = None) -> requests.Response:
        """get_v1_totals_entity_type operation"""
        url = f"{self._base_url}/v1/totals/{entity_type}/"
        params = {}
        if page is not None:
            params["page"] = page
        if per_page is not None:
            params["per_page"] = per_page
        if cycle is not None:
            params["cycle"] = cycle
        if committee_designation is not None:
            params["committee_designation"] = committee_designation
        if committee_id is not None:
            params["committee_id"] = committee_id
        if committee_type is not None:
            params["committee_type"] = committee_type
        if committee_state is not None:
            params["committee_state"] = committee_state
        if filing_frequency is not None:
            params["filing_frequency"] = filing_frequency
        if treasurer_name is not None:
            params["treasurer_name"] = treasurer_name
        if min_disbursements is not None:
            params["min_disbursements"] = min_disbursements
        if max_disbursements is not None:
            params["max_disbursements"] = max_disbursements
        if min_receipts is not None:
            params["min_receipts"] = min_receipts
        if max_receipts is not None:
            params["max_receipts"] = max_receipts
        if min_last_cash_on_hand_end_period is not None:
            params["min_last_cash_on_hand_end_period"] = min_last_cash_on_hand_end_period
        if max_last_cash_on_hand_end_period is not None:
            params["max_last_cash_on_hand_end_period"] = max_last_cash_on_hand_end_period
        if min_last_debts_owed_by_committee is not None:
            params["min_last_debts_owed_by_committee"] = min_last_debts_owed_by_committee
        if max_last_debts_owed_by_committee is not None:
            params["max_last_debts_owed_by_committee"] = max_last_debts_owed_by_committee
        if sponsor_candidate_id is not None:
            params["sponsor_candidate_id"] = sponsor_candidate_id
        if organization_type is not None:
            params["organization_type"] = organization_type
        if min_first_f1_date is not None:
            params["min_first_f1_date"] = min_first_f1_date
        if max_first_f1_date is not None:
            params["max_first_f1_date"] = max_first_f1_date
        if sort is not None:
            params["sort"] = sort
        if sort_hide_null is not None:
            params["sort_hide_null"] = sort_hide_null
        if sort_null_only is not None:
            params["sort_null_only"] = sort_null_only
        if sort_nulls_last is not None:
            params["sort_nulls_last"] = sort_nulls_last
        if api_key is not None:
            params["api_key"] = api_key
        return self._make_request("GET", url, params=params if params else None, headers=self.get_headers())