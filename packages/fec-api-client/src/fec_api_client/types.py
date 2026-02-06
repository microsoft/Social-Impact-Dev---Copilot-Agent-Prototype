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
