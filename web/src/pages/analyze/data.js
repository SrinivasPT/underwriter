export const REPORT_DOC = {
    bank_statement_analysis: [
        {
            area: "Salary Consistency",
            value: "Consistent",
            comments: [
                "The salary credit from TCS Pvt Ltd is observed on 2024-08-02 for ₹75,000.",
                "Salary credits are regular with no gaps observed within the given statement period.",
                "The credited amount matches the monthly income reported (₹75,000), indicating consistency.",
            ],
        },
        {
            area: "EMI Payments Behavior",
            value: "Regular",
            comments: [
                "An EMI payment of ₹15,000 is debited on 2024-08-20, as per the statement.",
                "This amount constitutes 20% of the monthly income (₹15,000 / ₹75,000).",
                "No irregularities or delays in payment are observed for this period.",
            ],
        },
        {
            area: "Balance Maintenance",
            value: 80000.0,
            comments: [
                "The average balance is calculated as (Opening Balance ₹75,000 + Closing Balance ₹85,000) / 2 = ₹80,000.",
                "The maintained average balance is adequate, considering the income and withdrawal patterns.",
                "This balance is above the threshold of ₹50,000 specified in the Consumer Finance Policy for preferential terms.",
            ],
        },
        {
            area: "Transaction Patterns",
            value: "Normal",
            comments: [
                "Transactions include a salary credit, EMI debit, and other withdrawals that are proportionate to the income.",
                "Total deposits: ₹1,25,000 and total withdrawals: ₹1,15,000 show balanced activity.",
                "No unusual or risky patterns such as frequent high withdrawals or critically low balances are observed.",
            ],
        },
        {
            area: "Risk Indicators",
            value: "Low",
            comments: [
                "No inward cheque bounces are observed in the statement, which aligns with the policy requirement.",
                "Steady transaction activity and consistent salary credits indicate financial stability.",
                "The EMI-to-income ratio is within acceptable limits, reducing potential repayment risk.",
            ],
        },
    ],
    cibil_report_analysis: [
        {
            area: "Credit Score",
            value: "Excellent",
            comments: [
                "The CIBIL score is 780, which falls within the range of 750-900. According to industry benchmarks, scores are classified as follows: Poor (300-549), Fair (550-649), Good (650-749), and Excellent (750-900). Therefore, a score of 780 is classified as 'Excellent'.",
            ],
        },
        {
            area: "Payment History",
            value: "No Defaults",
            comments: [
                "The report indicates 0 defaults and no late payments. This clean repayment history enhances creditworthiness, as lenders view a history of timely payments as a strong indicator of reliability in repaying loans.",
            ],
        },
        {
            area: "Credit Utilization",
            value: "45.0%",
            comments: [
                "The credit utilization ratio is calculated as (Total Outstanding / Total Credit Limit) * 100 = (450000 / 1000000) * 100 = 45.0%. This is above the generally recommended threshold of 30%-40%, which may negatively impact the credit score and suggest over-reliance on credit.",
            ],
        },
        {
            area: "Account Mix",
            value: "2 Accounts (Unsecured)",
            comments: [
                "The report shows 2 accounts with no indication of secured loans. A typical profile for a salaried individual may include a mix of secured (like home loans) and unsecured loans (like personal loans or credit cards). The absence of secured loans may limit the creditworthiness perception, but the excellent score and clean payment history mitigate this concern.",
            ],
        },
        {
            area: "Hard Inquiries",
            value: "0 Inquiries",
            comments: [
                "There are no hard inquiries reported in the past year. Generally, more than 2-3 hard inquiries can negatively impact the credit score. Since there are no inquiries, this does not pose a risk to the credit score.",
            ],
        },
        {
            area: "Risk Indicators",
            value: "Low Risk",
            comments: [
                "The report shows no defaults, a good credit score, and a manageable credit utilization ratio. However, the utilization is slightly high at 45%, which could indicate potential risk if it persists. Overall, the absence of defaults and hard inquiries suggests low financial risk.",
            ],
        },
        {
            area: "Income-to-EMI Ratio",
            value: "Not Applicable",
            comments: [
                "The report does not provide specific EMI obligations, making it impossible to calculate the income-to-EMI ratio. However, a general guideline is that this ratio should be below 50% to ensure that the borrower can comfortably manage their loan repayments relative to their income.",
            ],
        },
    ],
    loan_application_review: [
        {
            area: "Eligibility",
            value: "Regular",
            comments: [
                "The applicant, John Doe, is 34 years old (born on 1990-01-15), which falls within the age eligibility of 23-62 years for the Regular category.",
                "His monthly income is reported as ₹75,000, which exceeds the gross income requirement of ₹40,000.",
                "The CIBIL score is 780, which meets the minimum requirement of 700 for the Regular category.",
            ],
        },
        {
            area: "Income Assessment",
            value: 1125000,
            comments: [
                "The average monthly salary credits over the last 6 months total ₹300,000, averaging ₹50,000 per month.",
                "The declared monthly income in the CIBIL report is ₹75,000. The maximum eligible loan amount for the Regular category is calculated as ₹75,000 * 15 = ₹1,125,000, which is within the policy limit of ₹15,00,000.",
            ],
        },
        {
            area: "DBR",
            value: "67%",
            comments: [
                "The total EMI payments over the statement period amount to ₹200,000, while the average monthly income is ₹75,000. ",
                "The Debt Burden Ratio (DBR) is calculated as (Total EMI / Monthly Income) * 100 = (200,000 / 450,000) * 100 = 44.44%. ",
                "However, the DBR exceeds the policy limit of 50% for the Regular category, indicating potential financial strain.",
            ],
        },
        {
            area: "Risk Indicators",
            value: "High Withdrawals and Low Closing Balance",
            comments: [
                "The bank statement shows a pattern of high withdrawals, including a ₹100,000 miscellaneous expense, which significantly reduced the closing balance to ₹40,000. ",
                "The average balance is ₹100,000, but the closing balance is low compared to the average monthly salary credit of ₹75,000, indicating potential cash flow issues. ",
                "Additionally, the credit utilization ratio is at 45%, which is above the recommended threshold of 30%-40%.",
            ],
        },
        {
            area: "Alignment with Loan Policy",
            value: "Within Policy Guidelines",
            comments: [
                "The applicant has requested a loan amount of ₹10,00,000 for a tenure of 60 months. ",
                "This amount is within the maximum eligible limit of ₹15,00,000 for the Regular category, and the tenure of 60 months is also compliant with the policy guidelines of 12-72 months. ",
                "The interest rate will be determined based on the applicant's profile, but it should fall within the 12%-20% range for the Regular category.",
            ],
        },
    ],
};
