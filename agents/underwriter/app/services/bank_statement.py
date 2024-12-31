import json


def analyze_bank_statement(bank_statement: str, llm):
    """Use LLM to analyze banking behavior"""

    prompt = f"""Analyze the following bank statement for loan assessment:

Bank Statement: {json.dumps(bank_statement)}

Analyze:
1. Salary credits consistency: Calculate the consistency of monthly salary credits by analyzing regularity, amounts, and gaps between credits.
2. EMI payments behavior: Assess the regularity, amounts, and their proportion to income or balance. Highlight any irregular or delayed payments.
3. Balance maintenance: Compute the average balance over the statement period and assess whether it is adequate based on income and withdrawals.
4. Transaction patterns: Identify any unusual or risky transaction behaviors such as frequent high withdrawals or low remaining balance.
5. Risk indicators: List any transaction patterns or account behaviors that suggest financial risks.

For each area, ensure that:
- The `value` is derived directly from the provided data and justified explicitly in the `comments`.
- The `comments` include detailed steps, calculations, or observations that explain how the `value` was determined.

Provide the response as an array of JSON objects, each with these keys (important: Do not include any additional text or markdown formatting):
{{
    "area": "string",  # The analyzed parameter or area (e.g., 'Salary Consistency', 'EMI Behavior')
    "value": "string or float",  # The computed value or classification (e.g., 0.85, 'Irregular')
    "comments": ["string"]  # Justification for the value, including calculations or logic used
}}
"""

    response = llm.invoke(prompt)

    return response.content.strip("```json").strip()
