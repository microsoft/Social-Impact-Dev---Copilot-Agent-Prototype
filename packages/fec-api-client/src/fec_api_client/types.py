"""FEC API type definitions.

Types and utilities for working with FEC form types and report types.
See: https://api.open.fec.gov/developers/
"""

from typing import Literal

# Trusted FEC domains for file downloads (SSRF protection)
FEC_DOWNLOAD_DOMAINS = frozenset({"docquery.fec.gov", "www.fec.gov", "fec.gov"})

# -----------------------------------------------------------------------------
# Form Types (determines CSV structure)
# Note: Forms can have suffixes: N=new, A=amended, T=termination (e.g., F3A)
# -----------------------------------------------------------------------------

FormTypeCode = Literal[
    "F1",
    "F1M",
    "F2",
    "F3",
    "F3P",
    "F3X",
    "F3L",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F13",
    "F24",
    "F99",
    "FRQ",
]

FORM_TYPE_NAMES: dict[str, str] = {
    "F1": "Statement of Organization",
    "F1M": "Notification of Multicandidate Status",
    "F2": "Statement of Candidacy",
    "F3": "Report of Receipts and Disbursements (House/Senate)",
    "F3P": "Report of Receipts and Disbursements (Presidential)",
    "F3X": "Report of Receipts and Disbursements (PAC/Party)",
    "F3L": "Report of Contributions Bundled by Lobbyists",
    "F4": "Report for Convention Committee",
    "F5": "Report of Independent Expenditures",
    "F6": "48 Hour Notice of Contributions/Loans Received",
    "F7": "Report of Communication Costs",
    "F8": "Debt Settlement Plan",
    "F9": "24 Hour Notice of Electioneering Communications",
    "F13": "Report of Donations for Inaugural Committee",
    "F24": "24/48 Hour Report of Independent Expenditures",
    "F99": "Miscellaneous Text",
    "FRQ": "Request for Additional Information",
}


def get_base_form_type(form_type: str | None) -> str | None:
    """Extract base form type (e.g., F3A -> F3, F3XN -> F3X)."""
    if not form_type:
        return None
    normalized = form_type.strip('"').upper()
    # Check longest matches first (F3X before F3, F1M before F1)
    for code in sorted(FORM_TYPE_NAMES.keys(), key=lambda x: len(x), reverse=True):
        if normalized.startswith(code):
            return code
    return normalized


def format_form_type(form_type: str | None) -> str:
    """Format form type code to human-readable name."""
    if not form_type:
        return "Unknown"
    base_type = get_base_form_type(form_type)
    return FORM_TYPE_NAMES.get(base_type, form_type) if base_type else form_type


# -----------------------------------------------------------------------------
# Report Types (determines which filings to fetch)
# -----------------------------------------------------------------------------

ReportTypeCode = Literal[
    # Quarterly
    "Q1",
    "Q2",
    "Q3",
    "YE",
    "Q2S",
    "QYE",
    # Monthly
    "M1",
    "M2",
    "M3",
    "M4",
    "M5",
    "M6",
    "M7",
    "M8",
    "M9",
    "M10",
    "M11",
    "M12",
    "MSA",
    # Election
    "12P",
    "12G",
    "30P",
    "30G",
    "30R",
    "30S",
    # Other
    "48",
    "TER",
]

REPORT_TYPE_NAMES: dict[str, str] = {
    "Q1": "April Quarterly (Q1)",
    "Q2": "July Quarterly (Q2)",
    "Q3": "October Quarterly (Q3)",
    "YE": "Year-End (YE)",
    "Q2S": "July Quarterly / Semi-Annual (Q2S)",
    "QYE": "Quarterly Semi-Annual Year-End (QYE)",
    "M1": "January Monthly (M1)",
    "M2": "February Monthly (M2)",
    "M3": "March Monthly (M3)",
    "M4": "April Monthly (M4)",
    "M5": "May Monthly (M5)",
    "M6": "June Monthly (M6)",
    "M7": "July Monthly (M7)",
    "M8": "August Monthly (M8)",
    "M9": "September Monthly (M9)",
    "M10": "October Monthly (M10)",
    "M11": "November Monthly (M11)",
    "M12": "December Monthly (M12)",
    "MSA": "Monthly Semi-Annual (MSA)",
    "12P": "12-Day Pre-Primary (12P)",
    "12G": "12-Day Pre-General (12G)",
    "30P": "30-Day Post-Primary (30P)",
    "30G": "30-Day Post-General (30G)",
    "30R": "30-Day Post-Runoff (30R)",
    "30S": "30-Day Post-Special (30S)",
    "48": "48-Hour Report of Independent Expenditures",
    "TER": "Termination Report",
}


def format_report_type(report_type: str | None) -> str:
    """Format report type code to human-readable name."""
    if not report_type:
        return "Unknown"
    return REPORT_TYPE_NAMES.get(report_type, report_type)
