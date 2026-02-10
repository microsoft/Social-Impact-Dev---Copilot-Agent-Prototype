"""Constants for FEC data services."""

from typing import get_args

from fec_api_client.types import ReportTypeCode

# FEC quarterly report type codes (subset of ReportTypeCode)
# Q1: April Quarterly (covers January 1 - March 31)
# Q2: July Quarterly (covers April 1 - June 30)
# Q3: October Quarterly (covers July 1 - September 30)
# YE: Year-End (covers October 1 - December 31)
QUARTERLY_REPORT_TYPES: list[ReportTypeCode] = ["Q1", "Q2", "Q3", "YE"]

# All valid FEC report type codes (from ReportTypeCode Literal)
ALL_REPORT_TYPES: list[ReportTypeCode] = list(get_args(ReportTypeCode))
