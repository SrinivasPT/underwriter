request_json = {"id": "08FCE8E87C644DE0A2DA879D4FF554EF"}
request_json["bank_statement"] = {
    "bankStatement": {
        "accountDetails": {
            "accountHolderName": "John Doe",
            "accountNumber": "ICICI9876543210",
            "ifscCode": "ICIC0001234",
            "branch": "Andheri East, Mumbai",
            "accountType": "Savings",
            "statementPeriod": {"startDate": "2024-03-01", "endDate": "2024-08-31"},
            "currency": "INR",
            "openingBalance": 100000.0,
            "closingBalance": 40000.0,
        },
        "transactionSummary": {
            "totalDeposits": 300000.0,
            "totalWithdrawals": 360000.0,
            "numberOfTransactions": 60,
        },
        "transactions": [
            {
                "transactionDate": "2024-03-05",
                "transactionDescription": "Salary Credit - TCS Pvt Ltd",
                "referenceNumber": "SAL1234567890",
                "transactionType": "Credit",
                "amount": 75000.0,
                "balanceAfterTransaction": 175000.0,
            },
            {
                "transactionDate": "2024-03-10",
                "transactionDescription": "ATM Withdrawal",
                "referenceNumber": "ATM1234567890",
                "transactionType": "Debit",
                "amount": 50000.0,
                "balanceAfterTransaction": 125000.0,
            },
            {
                "transactionDate": "2024-03-15",
                "transactionDescription": "Online Purchase - Flipkart",
                "referenceNumber": "ORD1234567890",
                "transactionType": "Debit",
                "amount": 30000.0,
                "balanceAfterTransaction": 95000.0,
            },
            {
                "transactionDate": "2024-03-20",
                "transactionDescription": "EMI Payment - Home Loan HDFC",
                "referenceNumber": "EMI1234567890",
                "transactionType": "Debit",
                "amount": 25000.0,
                "balanceAfterTransaction": 70000.0,
            },
            {
                "transactionDate": "2024-04-05",
                "transactionDescription": "Salary Credit - TCS Pvt Ltd",
                "referenceNumber": "SAL9876543210",
                "transactionType": "Credit",
                "amount": 70000.0,
                "balanceAfterTransaction": 140000.0,
            },
            {
                "transactionDate": "2024-04-15",
                "transactionDescription": "Utility Payment - Electricity",
                "referenceNumber": "BILL1234567890",
                "transactionType": "Debit",
                "amount": 20000.0,
                "balanceAfterTransaction": 120000.0,
            },
            {
                "transactionDate": "2024-05-05",
                "transactionDescription": "Salary Credit - TCS Pvt Ltd",
                "referenceNumber": "SAL1357924680",
                "transactionType": "Credit",
                "amount": 80000.0,
                "balanceAfterTransaction": 200000.0,
            },
            {
                "transactionDate": "2024-05-20",
                "transactionDescription": "EMI Payment - Home Loan HDFC",
                "referenceNumber": "EMI4680135792",
                "transactionType": "Debit",
                "amount": 40000.0,
                "balanceAfterTransaction": 160000.0,
            },
            {
                "transactionDate": "2024-06-05",
                "transactionDescription": "Salary Credit - TCS Pvt Ltd",
                "referenceNumber": "SAL0987654321",
                "transactionType": "Credit",
                "amount": 60000.0,
                "balanceAfterTransaction": 220000.0,
            },
            {
                "transactionDate": "2024-06-25",
                "transactionDescription": "Medical Expenses",
                "referenceNumber": "MED1234567890",
                "transactionType": "Debit",
                "amount": 50000.0,
                "balanceAfterTransaction": 170000.0,
            },
            {
                "transactionDate": "2024-07-05",
                "transactionDescription": "Salary Credit - TCS Pvt Ltd",
                "referenceNumber": "SAL6789012345",
                "transactionType": "Credit",
                "amount": 50000.0,
                "balanceAfterTransaction": 220000.0,
            },
            {
                "transactionDate": "2024-07-10",
                "transactionDescription": "Vacation Expenses",
                "referenceNumber": "VAC4567890123",
                "transactionType": "Debit",
                "amount": 60000.0,
                "balanceAfterTransaction": 160000.0,
            },
            {
                "transactionDate": "2024-08-05",
                "transactionDescription": "Salary Credit - TCS Pvt Ltd",
                "referenceNumber": "SAL8765432109",
                "transactionType": "Credit",
                "amount": 40000.0,
                "balanceAfterTransaction": 200000.0,
            },
            {
                "transactionDate": "2024-08-20",
                "transactionDescription": "EMI Payment - Home Loan HDFC",
                "referenceNumber": "EMI1234567890",
                "transactionType": "Debit",
                "amount": 60000.0,
                "balanceAfterTransaction": 140000.0,
            },
            {
                "transactionDate": "2024-08-31",
                "transactionDescription": "Miscellaneous Expenses",
                "referenceNumber": "MISC0987654321",
                "transactionType": "Debit",
                "amount": 100000.0,
                "balanceAfterTransaction": 40000.0,
            },
        ],
    }
}
request_json["cibil_report"] = {
    "reportDetails": {
        "reportID": "CIBIL9876543210",
        "generatedDate": "2024-12-01T10:15:30Z",
        "reportType": "Individual",
        "currency": "INR",
    },
    "personalDetails": {
        "name": "John Doe",
        "dateOfBirth": "1990-01-15",
        "gender": "Male",
        "PAN": "ABCDE1234F",
        "AadhaarNumber": "1234-5678-1234",
        "contactDetails": {
            "email": "john.doe@example.com",
            "phoneNumber": "+91-9876543210",
        },
        "address": [
            {
                "type": "Permanent",
                "line1": "Flat 401, Shanti Residency",
                "line2": "Sector 15, Navi Mumbai",
                "city": "Mumbai",
                "state": "Maharashtra",
                "pincode": "400705",
                "country": "India",
            },
            {
                "type": "Current",
                "line1": "Plot No 12, Green Park",
                "line2": "Andheri East",
                "city": "Mumbai",
                "state": "Maharashtra",
                "pincode": "400093",
                "country": "India",
            },
        ],
    },
    "employmentDetails": {
        "employmentType": "Salaried",
        "employerName": "TCS Pvt Ltd",
        "income": {
            "monthlyIncome": 75000,
            "currency": "INR",
            "lastUpdated": "2024-12-01",
        },
    },
    "creditSummary": {
        "totalCreditLimit": 1000000,
        "totalOutstanding": 450000,
        "creditUtilization": 45.0,
        "numberOfAccounts": 2,
        "numberOfDefaults": 0,
        "oldestAccountDate": "2015-01-15",
        "mostRecentAccountDate": "2023-08-01",
        "averageAccountAgeMonths": 72,
    },
    "scoreDetails": {
        "CIBILScore": 780,
        "scoreRange": "300-900",
        "scoreGrade": "Excellent",
    },
}
request_json[
    "policy_document"
] = """
# Consumer Finance Programs & Guidelines

## Program Categories
| Category                | Age Eligibility | Monthly Income         | Target Audience                          |
|-------------------------|-----------------|------------------------|------------------------------------------|
| Premium Salary Account  | 24 - 60 years  | Net Salary ₹30,000+   | MNC, PSU, & Top-Tier Pvt Employees       |
| Regular Income          | 23 - 62 years  | Gross Income ₹40,000+ | Govt, Pvt Ltd, Professionals             |
| Business Owner          | 28 - 65 years  | L3M Avg Credits ₹1L+  | SMEs, Startups, & Retailers              |

## Eligibility Matrix
| Parameter               | Premium                  | Regular                  | Business                |
|-------------------------|--------------------------|--------------------------|-------------------------|
| Credit Score (CIBIL)    | Min 750                 | Min 700                 | Min 725                |
| Work Experience         | 12M (Current: 6M)       | 24M (Current: 9M)       | Business Vintage: 36M  |
| Residence Stability     | ≥12M Any Type           | ≥18M Any Type           | ≥24M Self-Owned        |

## Loan Product Structure
| Component               | Premium                 | Regular                 | Business               |
|-------------------------|--------------------------|--------------------------|-------------------------|
| Loan Range              | ₹1L - ₹20L              | ₹50K - ₹15L             | ₹2L - ₹25L             |
| Tenure Options          | 12-84 months           | 12-72 months           | 12-60 months           |
| Interest Band           | 10% - 16%              | 12% - 20%              | 14% - 24%              |
| Processing Fee          | 1% - 2.5%              | 1.5% - 3%              | 2% - 4%                |

## Income Assessment
| Category   | Method              | Multiplier | Maximum Limit |
|------------|---------------------|------------|---------------|
| Premium    | Fixed Salary        | 20x        | ₹20L          |
| Regular    | Gross Income        | 15x        | ₹15L          |
| Business   | Avg Monthly Credits | 15x        | ₹25L          |

## Debt Burden Ratio (DBR)
| Category   | DBR Limit | Add-Ons                    |
|------------|-----------|----------------------------|
| Premium    | 55%       | +5% for Own House          |
| Regular    | 50%       | +3% for No Other Loans     |
| Business   | 45%       | Not Applicable             |

## Banking Parameters
| Parameter                  | Threshold            | Impact                 | Action                 |
|----------------------------|----------------------|------------------------|------------------------|
| Avg Monthly Balance        | >₹50K               | Rate Benefit: -0.5%    | Preferential Processing|
| Transactions (Credit)      | ≥12/month           | +10% Loan Limit        | Incentivized Processing|
| Inward Cheque Bounces      | None in 12M         | Critical               | Rejected               |

## Restricted Segments
| Restricted Business Types                |
|------------------------------------------|
| Betting, Gaming, & Gambling              |
| Crypto & Digital Currencies              |
| Non-Profits, Religious Organizations     |
| Real Estate Broking                      |
| Defense Personnel                        |
| High-Risk Export/Import Businesses       |

## Loan Processing Workflow
| Step                   | Details                                               |
|------------------------|-------------------------------------------------------|
| Eligibility Check      | Automated CIBIL & DBR Validation                      |
| Income Verification    | Analyze salary slips, bank statements, and tax returns|
| Approval Matrix        | Premium: Pre-approved for listed corporates/PSUs      |
|                        | Regular: Standard credit evaluation process           |
|                        | Business: Financial and vintage verification mandatory|
| Disbursement           | Funds credited within 24 hours for pre-approved loans |

## Documentation Requirements
| Category   | ID Proof          | Income Proof           | Bank Statement  | Residence Proof     |
|------------|-------------------|------------------------|-----------------|---------------------|
| Premium    | PAN, Aadhaar      | Salary Slips, Form 16  | Last 6 Months   | Any Valid Document  |
| Regular    | PAN, Aadhaar      | Salary Slips, Form 16  | Last 6 Months   | Any Valid Document  |
| Business   | PAN, Aadhaar      | GST Returns, IT Returns| Last 12 Months  | Property Documents  |

"""
