import React from "react";
import styles from "./Header.module.css";

const Header = () => {
    return (
        <header className={styles.header}>
            <h3 className={styles.logo}>AccuLoan</h3>
            <nav>
                <ul className={styles.navList}>
                    <li>
                        <a href="/" className={styles.navLink}>
                            Home
                        </a>
                    </li>
                    <li>
                        <a href="/analyze" className={styles.navLink}>
                            Analyze
                        </a>
                    </li>
                    <li>
                        <a href="/about" className={styles.navLink}>
                            About
                        </a>
                    </li>
                    <li>
                        <a href="/contact" className={styles.navLink}>
                            Contact
                        </a>
                    </li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
