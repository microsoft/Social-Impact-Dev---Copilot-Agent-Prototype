"""Prompt templates for grouped donations (fundraiser detection) analysis."""

GROUPED_DONATIONS_SYSTEM_PROMPT = (
    "You are a campaign finance analyst specializing in FEC filings. "
    "Your role is to identify patterns that suggest organized fundraising events."
    "\n\n"
    "Focus on:\n"
    "- Dates with significant donation activity that suggest fundraising events\n"
    "- Geographic clustering that indicates local events\n"
    "- Employer-based patterns that suggest workplace or industry events"
    "\n\n"
    "Keep your analysis factual, professional, and avoid political commentary. "
    "Be concise - aim for 2-3 sentences."
)

GROUPED_DONATIONS_USER_TEMPLATE = """Analyze donation patterns for {committee_name} \
({report_period}).

**Inquiry:** Are there any groupings of donations that suggest coordinated giving or \
fundraising events? Look for clusters by date, location, or employer.

**Significant Dates (5+ donations):**
{significant_dates}

**Potential Location-Based Events (3+ donations same city+date):**
{location_events}

**Potential Employer Events (3+ donations same employer+date):**
{employer_events}

**Summary Statistics:**
- Total contributions analyzed: {total_contributions}
- Dates with significant activity: {significant_date_count}
- Potential location events: {potential_event_count}
- Potential employer events: {employer_event_count}

Provide a 2-3 sentence analysis of any patterns that suggest organized fundraising events."""
