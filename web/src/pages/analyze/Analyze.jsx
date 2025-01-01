import React, { useState, useEffect } from "react";
import styles from "./Analyze.module.css"; // Import CSS module
import VerticalTabs from "./vertical-tab/VerticalTabs";
import BankStatementAnalysis from "./bank-statement-analysis/BankStatementAnalysis";
import ChatWindow from "./chat-window/ChatWindow";
import LoanApplicationReview from "./loan-application-review/LoanApplicationReview";
import CibilReportAnalysis from "./cibil-report-analysis/CibilReportAnalysis";
import { useImmerReducer } from "use-immer";
import { pageReducer, PageContext, initialState } from "@/context/PageContext";

const Analyze = () => {
    initialState.data = { bank_statement_analysis: [], cibil_report_analysis: [], loan_application_review: [] };
    const [state, dispatch] = useImmerReducer(pageReducer, initialState);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await fetch("http://localhost:8000/api/loan-applications/2444A2609EC348DE8F894E160A7C2F83");
                let data = await response.json();
                data = JSON.parse(data.response);
                data.bank_statement_analysis = JSON.parse(data.bank_statement_response);
                data.cibil_report_analysis = JSON.parse(data.cibil_report_response);
                data.loan_application_review = JSON.parse(data.loan_application_response);
                dispatch({ type: "SET_DATA", payload: data }); // Update state with API data
            } catch (error) {
                console.error("Error fetching data:", error);
            }
        };

        fetchData();
    }, []);

    const [chatWidth, setChatWidth] = useState(40); // Default chat width in percentage
    const [isResizing, setIsResizing] = useState(false);

    // Handle mouse down to start resizing
    const handleMouseDown = (e) => {
        setIsResizing(true);
    };

    // Handle mouse move to update chat width
    const handleMouseMove = (e) => {
        if (isResizing) {
            const newWidth = ((window.innerWidth - e.clientX) / window.innerWidth) * 100;
            setChatWidth(Math.min(Math.max(newWidth, 20), 60)); // Limit width between 20% and 60%
        }
    };

    // Handle mouse up to stop resizing
    const handleMouseUp = () => {
        setIsResizing(false);
    };

    // Add event listeners for mouse move and mouse up
    useEffect(() => {
        if (isResizing) {
            window.addEventListener("mousemove", handleMouseMove);
            window.addEventListener("mouseup", handleMouseUp);
        } else {
            window.removeEventListener("mousemove", handleMouseMove);
            window.removeEventListener("mouseup", handleMouseUp);
        }

        // Cleanup event listeners on unmount
        return () => {
            window.removeEventListener("mousemove", handleMouseMove);
            window.removeEventListener("mouseup", handleMouseUp);
        };
    }, [isResizing]);

    return (
        <PageContext.Provider value={{ state, dispatch }}>
            <div className={styles.container}>
                <div className={styles.mainContent}>
                    {/* Content Sections */}
                    <VerticalTabs />
                    <div className={styles.contentSections} style={{ width: `${100 - chatWidth}%` }}>
                        {/* Bank Statement Section */}
                        <section id="bank-statement" className={styles.section}>
                            <div className={styles.sectionContent}>
                                <h3 className={styles.sectionTitle}>Bank Statement Analysis</h3>
                                <BankStatementAnalysis />
                            </div>
                        </section>

                        {/* CIBIL Report Section */}
                        <section id="cibil-report" className={styles.section}>
                            <div className={styles.sectionContent}>
                                <h3 className={styles.sectionTitle}>CIBIL Report Analysis</h3>
                                {<CibilReportAnalysis />}
                            </div>
                        </section>

                        {/* Loan Application Section */}
                        <section id="loan-application" className={styles.section}>
                            <div className={styles.sectionContent}>
                                <h3 className={styles.sectionTitle}>Loan Application Report</h3>
                                {<LoanApplicationReview />}
                            </div>
                        </section>
                    </div>

                    {/* Resizable Handle */}
                    <div className={styles.resizableHandle} onMouseDown={handleMouseDown} />

                    {/* Chat Window */}
                    <div className={styles.chatSection} style={{ width: `${chatWidth}%` }}>
                        <ChatWindow />
                    </div>
                </div>
            </div>
        </PageContext.Provider>
    );
};

export default Analyze;
