import json


def analyze_cibil_report(cibil_report: str, llm):
    """Analyze the CIBIL report for loan assessment with detailed insights and regional factors."""

    prompt = f"""Analyze the following CIBIL report for loan assessment:

CIBIL Report: {json.dumps(cibil_report)}

Analyze:
1. Credit Score: Evaluate the CIBIL score and classify it as 'Poor', 'Fair', 'Good', or 'Excellent' based on industry benchmarks. Mention the threshold values used for classification and any regional or industry-specific considerations.
2. Payment History: Analyze the repayment history for loans and credit cards, identifying late payments, defaults, or irregularities. Highlight how these patterns affect creditworthiness.
3. Credit Utilization: Calculate the credit utilization ratio and determine if it is within acceptable limits (e.g., 30%-40%). Highlight any overutilization and its potential impact.
4. Account Mix: Analyze the mix of secured and unsecured loans and how it influences creditworthiness. Mention if the account mix is typical for the borrower's profile (e.g., industry or income bracket).
5. Hard Inquiries: Evaluate the frequency of hard inquiries over the past year, assess if they exceed acceptable limits, and explain the potential impact on the credit score.
6. Risk Indicators: Identify any patterns in the report (e.g., high outstanding balances, defaults, frequent inquiries) that suggest financial risk. Explain their implications on loan repayment capability.
7. Income-to-EMI Ratio: Calculate the ratio of monthly EMI obligations to the declared monthly income. Determine if it is within the acceptable threshold (e.g., <50%) and explain its implications.

For each area, ensure that:
- The `value` is directly derived from the provided CIBIL data and consistent with the `comments`.
- The `comments` provide detailed steps, calculations, or observations explaining how the `value` was determined.

Provide the response as an array of JSON objects, each with these keys:
{{
    "area": "string",  # The analyzed parameter or area (e.g., 'Credit Score', 'Payment History')
    "value": "string or float",  # The computed value or classification (e.g., 750, 'Good', 'Fair')
    "comments": ["string"]  # Detailed justification, including calculations or observations, ensuring consistency with the value
}}
"""

    response = llm.invoke(prompt)

    return response.content.strip("```json").strip()
