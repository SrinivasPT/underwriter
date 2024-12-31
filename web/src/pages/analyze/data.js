export const REPORT_DOC = {
    bank_statement: [
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
};
