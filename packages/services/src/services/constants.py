"""Constants for FEC data services.

FEC Electronic Filing Format v8.5
=================================

This module contains column headers for parsing FEC electronic filing CSV exports.
Headers are aligned with FEC e-filing specification version 8.5.

Column Types
------------
Each header is a tuple of (name, type) where type is one of:
- "text": Default text field
- "currency": Dollar amount (formatted as $X,XXX.XX)
- "date": Date field (YYYYMMDD format, displayed as MM/DD/YYYY)
- "id": Identifier field (committee ID, transaction ID, etc.)

See Also
--------
- FEC Electronic Filing: https://www.fec.gov/help-candidates-and-committees/filing-reports/electronic-filing/
- FEC Data Dictionary: https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/
- FEC Forms: https://www.fec.gov/help-candidates-and-committees/forms/
"""

from typing import Literal, get_args

from fec_api_client.types import ReportTypeCode

#: Column type for FEC headers
ColumnType = Literal["text", "currency", "date", "id"]

#: Header definition: (column_name, column_type)
HeaderDef = tuple[str, ColumnType]

#: FEC quarterly report type codes (subset of :data:`ReportTypeCode`).
#:
#: - Q1: April Quarterly (covers January 1 - March 31)
#: - Q2: July Quarterly (covers April 1 - June 30)
#: - Q3: October Quarterly (covers July 1 - September 30)
#: - YE: Year-End (covers October 1 - December 31)
#:
#: See Also: https://www.fec.gov/help-candidates-and-committees/dates-and-deadlines/
QUARTERLY_REPORT_TYPES: list[ReportTypeCode] = ["Q1", "Q2", "Q3", "YE"]

#: All valid FEC report type codes (from :data:`ReportTypeCode` Literal).
ALL_REPORT_TYPES: list[ReportTypeCode] = list(get_args(ReportTypeCode))

# =============================================================================
# FEC CSV Headers - Electronic Filing Format v8.5
#
# These headers map to FEC e-filing CSV exports. Column order matches the
# official FEC specification for version 8.5.
#
# References:
#   - FEC E-Filing Specification: https://www.fec.gov/resources/cms-content/documents/fecfrm.pdf
#   - FEC CSV Sources (archived): https://github.com/newsdev/fec-csv-sources
#   - FEC Raw Data: https://www.fec.gov/data/browse-data/?tab=bulk-data
# =============================================================================

#: Header record (HDR) - File metadata present at the start of every FEC filing.
#:
#: See Also:
#:   - Column Source: https://github.com/newsdev/fec-csv-sources/blob/master/hdr.csv
#:   - FEC Filing Format: https://www.fec.gov/resources/cms-content/documents/fecfrm.pdf
HDR_COLUMNS: list[HeaderDef] = [
    ("Record Type", "text"),
    ("EF Type", "text"),
    ("FEC Version", "text"),
    ("Software Name", "text"),
    ("Software Version", "text"),
    ("Name Delimiter", "text"),
    ("Report ID", "id"),
    ("Report Number", "text"),
    ("Comment", "text"),
]

#: Header names only (for backwards compatibility)
HDR_HEADERS: list[str] = [col[0] for col in HDR_COLUMNS]

#: Form 3 (F3/F3N) headers - Campaign finance report summary for House/Senate candidates.
#:
#: Form 3 is filed by principal campaign committees of House and Senate candidates.
#: Form 3N is the notification of multicandidate status.
#:
#: See Also:
#:   - Column Source: https://github.com/newsdev/fec-csv-sources/blob/master/F3.csv
#:   - Form 3 Instructions: https://www.fec.gov/resources/cms-content/documents/fecfrm3i.pdf
#:   - Form 3 PDF: https://www.fec.gov/resources/cms-content/documents/fecfrm3.pdf
F3_COLUMNS: list[HeaderDef] = [
    ("Form Type", "text"),
    ("Committee ID", "id"),
    ("Committee Name", "text"),
    ("Change of Address", "text"),
    ("Street 1", "text"),
    ("Street 2", "text"),
    ("City", "text"),
    ("State", "text"),
    ("ZIP", "text"),
    ("Election State", "text"),
    ("Election District", "text"),
    ("Report Code", "text"),
    ("Election Code", "text"),
    ("Election Date", "date"),
    ("State of Election", "text"),
    ("Coverage From Date", "date"),
    ("Coverage Through Date", "date"),
    ("Treasurer Last Name", "text"),
    ("Treasurer First Name", "text"),
    ("Treasurer Middle Name", "text"),
    ("Treasurer Prefix", "text"),
    ("Treasurer Suffix", "text"),
    ("Date Signed", "date"),
    ("Total Contributions (No Loans) - Period", "currency"),
    ("Total Contribution Refunds - Period", "currency"),
    ("Net Contributions - Period", "currency"),
    ("Total Operating Expenditures - Period", "currency"),
    ("Total Offset to Operating Expenditures - Period", "currency"),
    ("Net Operating Expenditures - Period", "currency"),
    ("Cash on Hand Close of Period", "currency"),
    ("Debts To", "currency"),
    ("Debts By", "currency"),
    ("Individual Contributions Itemized - Period", "currency"),
    ("Individual Contributions Unitemized - Period", "currency"),
    ("Total Individual Contributions - Period", "currency"),
    ("Political Party Contributions - Period", "currency"),
    ("PAC Contributions - Period", "currency"),
    ("Candidate Contributions - Period", "currency"),
    ("Total Contributions - Period", "currency"),
    ("Transfers From Authorized - Period", "currency"),
    ("Candidate Loans - Period", "currency"),
    ("Other Loans - Period", "currency"),
    ("Total Loans - Period", "currency"),
    ("Offset to Operating Expenditures - Period", "currency"),
    ("Other Receipts - Period", "currency"),
    ("Total Receipts - Period", "currency"),
    ("Operating Expenditures - Period", "currency"),
    ("Transfers to Authorized - Period", "currency"),
    ("Candidate Loan Repayments - Period", "currency"),
    ("Other Loan Repayments - Period", "currency"),
    ("Total Loan Repayments - Period", "currency"),
    ("Refunds to Individuals - Period", "currency"),
    ("Refunds to Party Committees - Period", "currency"),
    ("Refunds to Other Committees - Period", "currency"),
    ("Total Refunds - Period", "currency"),
    ("Other Disbursements - Period", "currency"),
    ("Total Disbursements - Period", "currency"),
    ("Cash on Hand Beginning of Period", "currency"),
    ("Total Receipts This Period", "currency"),
    ("Subtotals", "currency"),
    ("Total Disbursements This Period", "currency"),
    ("Cash on Hand Close", "currency"),
    ("Total Contributions (No Loans) - Cycle", "currency"),
    ("Total Contribution Refunds - Cycle", "currency"),
    ("Net Contributions - Cycle", "currency"),
    ("Total Operating Expenditures - Cycle", "currency"),
    ("Total Offset to Operating Expenditures - Cycle", "currency"),
    ("Net Operating Expenditures - Cycle", "currency"),
    ("Individual Contributions Itemized - Cycle", "currency"),
    ("Individual Contributions Unitemized - Cycle", "currency"),
    ("Total Individual Contributions - Cycle", "currency"),
    ("Political Party Contributions - Cycle", "currency"),
    ("PAC Contributions - Cycle", "currency"),
    ("Candidate Contributions - Cycle", "currency"),
    ("Total Contributions - Cycle", "currency"),
    ("Transfers From Authorized - Cycle", "currency"),
    ("Candidate Loans - Cycle", "currency"),
    ("Other Loans - Cycle", "currency"),
    ("Total Loans - Cycle", "currency"),
    ("Offset to Operating Expenditures - Cycle", "currency"),
    ("Other Receipts - Cycle", "currency"),
    ("Total Receipts - Cycle", "currency"),
    ("Operating Expenditures - Cycle", "currency"),
    ("Transfers to Authorized - Cycle", "currency"),
    ("Candidate Loan Repayments - Cycle", "currency"),
    ("Other Loan Repayments - Cycle", "currency"),
    ("Total Loan Repayments - Cycle", "currency"),
    ("Refunds to Individuals - Cycle", "currency"),
    ("Refunds to Party Committees - Cycle", "currency"),
    ("Refunds to Other Committees - Cycle", "currency"),
    ("Total Refunds - Cycle", "currency"),
    ("Other Disbursements - Cycle", "currency"),
    ("Total Disbursements - Cycle", "currency"),
]

#: Header names only (for backwards compatibility)
F3_HEADERS: list[str] = [col[0] for col in F3_COLUMNS]

#: Schedule A headers (v8.5) - Itemized receipts/contributions.
#:
#: Schedule A reports itemized contributions and other receipts. Common form types:
#:
#: - SA11AI: Individual contributions
#: - SA11B: Political party contributions
#: - SA11C: PAC contributions
#: - SA12: Transfers from affiliated committees
#: - SA14: Offsets to operating expenditures
#: - SA15: Other receipts
#:
#: See Also:
#:   - Column Source: https://github.com/newsdev/fec-csv-sources/blob/master/SchA.csv
#:   - Schedule A Instructions: https://www.fec.gov/resources/cms-content/documents/fecfrm3i.pdf
#:   - Contributions Data: https://www.fec.gov/campaign-finance-data/contributions-individuals-file-description/
SCHEDULE_A_COLUMNS: list[HeaderDef] = [
    ("Form Type", "text"),
    ("Committee ID", "id"),
    ("Transaction ID", "id"),
    ("Back Reference Transaction ID", "id"),
    ("Back Reference Schedule", "text"),
    ("Entity Type", "text"),
    ("Organization Name", "text"),
    ("Last Name", "text"),
    ("First Name", "text"),
    ("Middle Name", "text"),
    ("Prefix", "text"),
    ("Suffix", "text"),
    ("Street 1", "text"),
    ("Street 2", "text"),
    ("City", "text"),
    ("State", "text"),
    ("ZIP", "text"),
    ("Election Code", "text"),
    ("Election Other Description", "text"),
    ("Contribution Date", "date"),
    ("Contribution Amount", "currency"),
    ("Contribution Aggregate", "currency"),
    ("Contribution Purpose Description", "text"),
    ("Contributor Employer", "text"),
    ("Contributor Occupation", "text"),
    ("Donor Committee FEC ID", "id"),
    ("Donor Committee Name", "text"),
    ("Donor Candidate FEC ID", "id"),
    ("Donor Candidate Last Name", "text"),
    ("Donor Candidate First Name", "text"),
    ("Donor Candidate Middle Name", "text"),
    ("Donor Candidate Prefix", "text"),
    ("Donor Candidate Suffix", "text"),
    ("Donor Candidate Office", "text"),
    ("Donor Candidate State", "text"),
    ("Donor Candidate District", "text"),
    ("Conduit Name", "text"),
    ("Conduit Street 1", "text"),
    ("Conduit Street 2", "text"),
    ("Conduit City", "text"),
    ("Conduit State", "text"),
    ("Conduit ZIP", "text"),
    ("Memo Code", "text"),
    ("Memo / Earmark Info", "text"),
    ("Reference Code", "text"),
]

#: Header names only (for backwards compatibility)
SCHEDULE_A_HEADERS: list[str] = [col[0] for col in SCHEDULE_A_COLUMNS]

#: Schedule B headers (v8.5) - Itemized disbursements/expenditures.
#:
#: Schedule B reports itemized disbursements and operating expenditures. Common form types:
#:
#: - SB17: Operating expenditures
#: - SB20A: Refunds of contributions to individuals
#: - SB20B: Refunds to political party committees
#: - SB21: Other disbursements
#: - SB23: Contribution refunds to political committees
#:
#: See Also:
#:   - Column Source: https://github.com/newsdev/fec-csv-sources/blob/master/SchB.csv
#:   - Schedule B Instructions: https://www.fec.gov/resources/cms-content/documents/fecfrm3i.pdf
#:   - Disbursements Data: https://www.fec.gov/campaign-finance-data/operating-expenditures-file-description/
SCHEDULE_B_COLUMNS: list[HeaderDef] = [
    ("Form Type", "text"),
    ("Committee ID", "id"),
    ("Transaction ID", "id"),
    ("Back Reference Transaction ID", "id"),
    ("Back Reference Schedule", "text"),
    ("Entity Type", "text"),
    ("Payee Organization Name", "text"),
    ("Payee Last Name", "text"),
    ("Payee First Name", "text"),
    ("Payee Middle Name", "text"),
    ("Payee Prefix", "text"),
    ("Payee Suffix", "text"),
    ("Payee Street 1", "text"),
    ("Payee Street 2", "text"),
    ("Payee City", "text"),
    ("Payee State", "text"),
    ("Payee ZIP", "text"),
    ("Election Code", "text"),
    ("Election Other Description", "text"),
    ("Expenditure Date", "date"),
    ("Expenditure Amount", "currency"),
    ("Semi-Annual Refunded Bundled Amount", "currency"),
    ("Expenditure Purpose Description", "text"),
    ("Category Code", "text"),
    ("Beneficiary Committee FEC ID", "id"),
    ("Beneficiary Committee Name", "text"),
    ("Beneficiary Candidate FEC ID", "id"),
    ("Beneficiary Candidate Last Name", "text"),
    ("Beneficiary Candidate First Name", "text"),
    ("Beneficiary Candidate Middle Name", "text"),
    ("Beneficiary Candidate Prefix", "text"),
    ("Beneficiary Candidate Suffix", "text"),
    ("Beneficiary Candidate Office", "text"),
    ("Beneficiary Candidate State", "text"),
    ("Beneficiary Candidate District", "text"),
    ("Conduit Name", "text"),
    ("Conduit Street 1", "text"),
    ("Conduit Street 2", "text"),
    ("Conduit City", "text"),
    ("Conduit State", "text"),
    ("Conduit ZIP", "text"),
    ("Memo Code", "text"),
    ("Memo / Earmark Info", "text"),
    ("Reference Code", "text"),
]

#: Header names only (for backwards compatibility)
SCHEDULE_B_HEADERS: list[str] = [col[0] for col in SCHEDULE_B_COLUMNS]

#: Mapping of FEC form type prefixes to their column definitions (with types).
#:
#: Used to dynamically select the appropriate headers and types based on the form type
#: prefix in the first column of each CSV row (e.g., "SA11AI" matches "SA").
#:
#: See Also: https://www.fec.gov/campaign-finance-data/e-filing-parse-tool/
FORM_TYPE_COLUMNS: dict[str, list[HeaderDef]] = {
    "HDR": HDR_COLUMNS,
    "F3": F3_COLUMNS,
    "SA": SCHEDULE_A_COLUMNS,
    "SB": SCHEDULE_B_COLUMNS,
}

#: Mapping of FEC form type prefixes to their column headers (names only).
FORM_TYPE_HEADERS: dict[str, list[str]] = {
    "HDR": HDR_HEADERS,
    "F3": F3_HEADERS,
    "SA": SCHEDULE_A_HEADERS,
    "SB": SCHEDULE_B_HEADERS,
}
