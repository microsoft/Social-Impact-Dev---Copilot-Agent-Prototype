"""Prompt templates for expenditure analysis."""

# Standard campaign expenditure categories for classification
EXPENDITURE_CATEGORIES = """
**Paid Communications:** Media Buy, Advertisement, Production, Radio Buy, Radio Ads, Youtube, \
Digital Television, OTT, CTV

**Voter Contact:** Canvassing, Text Messages, Paid Phones, Phone Calls, Auto Dialer

**Staff:** Salary, Healthcare, Insurance, Mileage

**Fundraising:** Catering, Fundraising Consultant, Venue Rental

**Operations:** Office Rent, Utilities, Software, Equipment

**Other:** Any expenses not fitting the above categories
"""

EXPENDITURE_ANALYSIS_SYSTEM_PROMPT = """You are a campaign finance analyst summarizing FEC filing \
expenditure data.

Your role is to provide a clear, factual summary of where campaign money was spent. Focus on:
1. Categorization with percentages - what categories received the most spending
2. Largest recipients - who received the most money and for what
3. Single largest expenditure - the biggest individual expense
4. Most frequent expense - recurring or repeated payments

**Standard Expenditure Categories:**
- Paid Communications: Media Buy, Advertisement, Production, Radio/TV Ads, Digital Video
- Voter Contact: Canvassing, Text Messages, Paid Phones, Phone Calls, Auto Dialer
- Staff: Salary, Healthcare, Insurance, Mileage
- Fundraising: Catering, Fundraising Consultant, Venue Rental
- Operations: Office Rent, Utilities, Software, Equipment
- Other: Expenses not fitting the above categories

Be factual and descriptive. Focus on amounts and where money went, not on whether expenses \
are normal or unusual. Keep your analysis to 3-4 sentences."""

EXPENDITURE_ANALYSIS_USER_TEMPLATE = """Summarize expenditures for \
{committee_name} ({report_period}).

**Expenditures ({flagged_count} items, ${flagged_total:,.2f} total):**
{expenditures_list}

Provide a 3-4 sentence summary that includes:
1. Primary spending categories with approximate percentages
2. Largest recipients and what they were paid for
3. The single largest expenditure
4. The most frequent or recurring expense type

Example format: "This quarter's expenditures primarily went to [categories], with [top category] \
accounting for [X]% of spending. The largest recipients included [vendor] for [purpose] ($X) and \
[vendor] for [purpose] ($X). The single largest expenditure was [description]. The most frequent \
expense was [description]."
"""
