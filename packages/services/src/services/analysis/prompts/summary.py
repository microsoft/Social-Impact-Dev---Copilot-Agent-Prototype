"""Prompt templates for report summary analysis."""

SUMMARY_SYSTEM_PROMPT = (
    "You are a helpful assistant that summarizes FEC campaign finance reports. "
    "Provide a clear, concise summary that highlights key financial information "
    "and notable patterns from the extracted statistics. "
    "Keep the tone professional and factual. "
    "Do not repeat the raw numbers - synthesize them into insights."
)

SUMMARY_USER_TEMPLATE = """Please summarize this FEC filing:

Candidate/Committee: {display_name}
Committee: {committee_name}
Report Type: {report_type}
Form Type: {form_type}
Coverage Period: {coverage_start} to {coverage_end}
Filing Date: {receipt_date}

**Financial Overview:**
{financials}

**Extracted Analysis Statistics:**
{analysis_stats}

Provide a brief 2-3 sentence summary of this campaign finance report, highlighting \
the most notable patterns from the statistics above."""


# Template for formatting analysis statistics for the summary prompt
# Note: This template is not currently used - formatting is done in service.py
ANALYSIS_STATS_TEMPLATE = """
- Max Out Donors ($3,500): {max_out_count} donors, ${max_out_total:,.2f}
- Geography: {in_state_pct:.1f}% in-state, {out_state_pct:.1f}% out-of-state
- Donor Size: {small_pct:.1f}% from small donors ($25 or less), {big_pct:.1f}% from larger donors
- Funding Sources: {individuals_pct:.1f}% individuals, {pacs_pct:.1f}% PACs, \
{parties_pct:.1f}% parties
- Flagged Expenditures: {flagged_count} items flagged (${flagged_total:,.2f})
"""
