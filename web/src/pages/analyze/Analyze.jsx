import React, { useState, useEffect } from "react";
import styles from "./Analyze.module.css"; // Import CSS module
import VerticalTabs from "./vertical-tab/VerticalTabs";
import BankStatement from "./bank-statement/BankStatement";

const Analyze = () => {
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
        <div className={styles.container}>
            {/* Vertical Tabs */}
            <VerticalTabs />

            {/* Main Content */}
            <div className={styles.mainContent}>
                {/* Content Sections */}
                <div className={styles.contentSections} style={{ width: `${100 - chatWidth}%` }}>
                    {/* Bank Statement Section */}
                    <section id="bank-statement" className={styles.section}>
                        <div className={styles.sectionContent}>
                            <h3 className={styles.sectionTitle}>Bank Statement Analysis</h3>
                            <BankStatement />
                        </div>
                    </section>

                    {/* CIBIL Report Section */}
                    <section id="cibil-report" className={styles.section}>
                        <div className={styles.sectionContent}>
                            <h5 className={styles.sectionTitle}>CIBIL Report Analysis</h5>
                            {/* <CibilReportAnalysis /> */}
                        </div>
                    </section>

                    {/* Loan Application Section */}
                    <section id="loan-application" className={styles.section}>
                        <div className={styles.sectionContent}>
                            <h5 className={styles.sectionTitle}>Loan Application Report</h5>
                            {/* <LoanApplicationReport /> */}
                        </div>
                    </section>
                </div>

                {/* Resizable Handle */}
                <div className={styles.resizableHandle} onMouseDown={handleMouseDown} />

                {/* Chat Window */}
                <div className={styles.chatWindow} style={{ width: `${chatWidth}%` }}>
                    <h2 className={styles.chatTitle}>Chat Window</h2>
                    <p>This is the chat area. Add your chat functionality here...</p>
                </div>
            </div>
        </div>
    );
};

export default Analyze;
