from typing import Literal

# FEC report type codes for API parameters
ReportTypeCode = Literal[
    "Q1",  # April Quarterly
    "Q2",  # July Quarterly
    "Q3",  # October Quarterly
    "YE",  # Year-End
    "M1",  # January Monthly
    "M2",  # February Monthly
    "M3",  # March Monthly
    "M4",  # April Monthly
    "M5",  # May Monthly
    "M6",  # June Monthly
    "M7",  # July Monthly
    "M8",  # August Monthly
    "M9",  # September Monthly
    "M10",  # October Monthly
    "M11",  # November Monthly
    "M12",  # December Monthly
    "12P",  # Pre-Primary
    "12G",  # Pre-General
    "30P",  # Post-Primary
    "30G",  # Post-General
    "30R",  # Post-Runoff
    "30S",  # Post-Special
    "TER",  # Termination Report
]

# Human-readable names for report type codes
REPORT_TYPE_NAMES: dict[ReportTypeCode, str] = {
    "Q1": "April Quarterly (Q1)",
    "Q2": "July Quarterly (Q2)",
    "Q3": "October Quarterly (Q3)",
    "YE": "Year End (YE)",
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
    "12P": "12-Day Pre-Primary (12P)",
    "12G": "12-Day Pre-General (12G)",
    "30P": "30-Day Post-Primary (30P)",
    "30G": "30-Day Post-General (30G)",
    "30R": "30-Day Post-Runoff (30R)",
    "30S": "30-Day Post-Special (30S)",
    "TER": "Termination Report",
}


def format_report_type(report_type: str | None) -> str:
    """Format report type code to human-readable name.

    Args:
        report_type: Report type code (e.g., "YE", "Q1").

    Returns:
        Human-readable name (e.g., "Year End (YE)"), or the original code if unknown.
    """
    if not report_type:
        return "Unknown"
    return REPORT_TYPE_NAMES.get(report_type, report_type)  # type: ignore[arg-type]
