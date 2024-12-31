import json


def analyze_loan_application(
    policy_document: str,
    bank_statement: str,
    cibil_report: str,
    bank_statement_analysis: list,
    cibil_report_analysis: list,
    llm,
):
    """Analyze the combined loan application using Step 1 outputs and raw documents."""

    prompt = f"""Analyze the following loan application for assessment against the policy:

Policy Document:
{policy_document}

Bank Statement Analysis (Individual Output):
{json.dumps(bank_statement_analysis)}

CIBIL Report Analysis (Individual Output):
{json.dumps(cibil_report_analysis)}

Bank Statement (Raw Data):
{json.dumps(bank_statement)}

CIBIL Report (Raw Data):
{json.dumps(cibil_report)}

Evaluate:
1. Eligibility: Determine the applicant's eligibility for Premium, Regular, or Business categories based on age, income, and credit score requirements.
2. Income Assessment: Cross-check salary credits in the bank statement with the declared income in the CIBIL report. Calculate the maximum eligible loan amount based on policy-defined multipliers.
3. Debt Burden Ratio (DBR): Calculate DBR using EMI obligations and income. Verify compliance with policy thresholds.
4. Risk Indicators: Identify risks based on findings from both individual analyses and raw data (e.g., high credit utilization, low balance, or irregular payments).
5. Alignment with Loan Policy: Verify that the requested loan amount, tenure, and interest rate are within policy guidelines.

For each area, provide a JSON object with these keys:
{{
    "area": "string",  # The analyzed parameter or area (e.g., 'Eligibility', 'Income Assessment', 'DBR')
    "value": "string or float",  # The computed value or classification (e.g., 'Premium', 750, 50%)
    "comments": ["string"]  # Detailed justification, including calculations or observations
}}

Ensure consistency between individual analyses and raw data while providing a holistic evaluation.
"""

    response = llm.invoke(prompt)

    return response.content.strip("```json").strip()
