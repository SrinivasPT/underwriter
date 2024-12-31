import React from "react";
import styles from "./VerticalTabs.module.css"; // Import CSS module

const VerticalTabs = () => {
    // Function to handle smooth scrolling to a section
    const scrollToSection = (id) => {
        const section = document.getElementById(id);
        if (section) {
            section.scrollIntoView({ behavior: "smooth" });
        }
    };

    return (
        <div className={styles.sidebar}>
            {/* Tabs */}
            <ul className={styles.tabList}>
                <li
                    className={styles.tabItem}
                    onClick={() => scrollToSection("bank-statement")}
                    onMouseEnter={(e) => {
                        e.currentTarget.style.backgroundColor = "#34495e";
                    }}
                    onMouseLeave={(e) => {
                        e.currentTarget.style.backgroundColor = "transparent";
                    }}
                >
                    Bank Statement
                </li>
                <li
                    className={styles.tabItem}
                    onClick={() => scrollToSection("cibil-report")}
                    onMouseEnter={(e) => {
                        e.currentTarget.style.backgroundColor = "#34495e";
                    }}
                    onMouseLeave={(e) => {
                        e.currentTarget.style.backgroundColor = "transparent";
                    }}
                >
                    CIBIL Report
                </li>
                <li
                    className={styles.tabItem}
                    onClick={() => scrollToSection("loan-application")}
                    onMouseEnter={(e) => {
                        e.currentTarget.style.backgroundColor = "#34495e";
                    }}
                    onMouseLeave={(e) => {
                        e.currentTarget.style.backgroundColor = "transparent";
                    }}
                >
                    Loan Application
                </li>
            </ul>
        </div>
    );
};

export default VerticalTabs;
