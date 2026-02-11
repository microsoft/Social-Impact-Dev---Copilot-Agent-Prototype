"""Prompt templates for report summary analysis."""

SUMMARY_SYSTEM_PROMPT = (
    "You are a helpful assistant that summarizes FEC campaign finance reports. "
    "Provide a clear, concise summary that highlights key financial information "
    "including total receipts, disbursements, and cash on hand. "
    "Keep the tone professional and factual."
)

SUMMARY_USER_TEMPLATE = """Please summarize this FEC filing:

Candidate/Committee: {display_name}
Committee: {committee_name}
Report Type: {report_type}
Form Type: {form_type}
Coverage Period: {coverage_start} to {coverage_end}
Filing Date: {receipt_date}
{financials}
Provide a brief 2-3 sentence summary of this campaign finance report."""
