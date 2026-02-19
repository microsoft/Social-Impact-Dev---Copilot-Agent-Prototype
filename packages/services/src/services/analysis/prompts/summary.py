"""Prompt templates for report summary analysis."""

SUMMARY_SYSTEM_PROMPT = """You are a campaign finance analyst providing insightful summaries \
of FEC filings. Your summaries should:

1. Provide context about who is filing (candidate, party, office sought)
2. Highlight the most significant financial patterns
3. Note any unusual or noteworthy aspects of the fundraising
4. Be professional, factual, and accessible to general readers

Synthesize the data into meaningful insights rather than just repeating numbers. \
Consider the political context when relevant (e.g., incumbent vs challenger, \
election timing, geographic patterns)."""

SUMMARY_USER_TEMPLATE = """Please summarize this FEC filing:

**Filing Information:**
Committee: {committee_name}
Report Type: {report_type}
Form Type: {form_type}
Coverage Period: {coverage_start} to {coverage_end}
Filing Date: {receipt_date}

**Committee Details:**
{committee_context}

**Associated Candidate(s):**
{candidate_context}

**Financial Overview:**
{financials}

**Analysis Statistics:**
{analysis_stats}

Provide a 3-4 sentence summary that:
1. Identifies who this committee supports and what office they're seeking
2. Summarizes the key financial takeaways (receipts, spending, cash position)
3. Highlights the most notable patterns from the analysis (donor geography, \
funding sources, any unusual items)
4. Provides brief context if relevant (e.g., competitive race, primary vs general)"""


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
