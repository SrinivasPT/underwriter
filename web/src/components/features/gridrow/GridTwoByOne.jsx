import React from "react";
import styles from "./GridTwoByOne.module.css"; // Import CSS module

const GridTwoByOne = ({ data }) => (
    <div className={styles.gridContainer}>
        {data.map((item, index) => (
            <div
                key={index}
                className={styles.gridItem}
                onMouseEnter={(e) => {
                    e.currentTarget.style.transform = "translateY(-0.125rem)";
                    e.currentTarget.style.boxShadow = "0 4px 15px rgba(0, 0, 0, 0.2)";
                }}
                onMouseLeave={(e) => {
                    e.currentTarget.style.transform = "translateY(0)";
                    e.currentTarget.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.1)";
                }}
            >
                {/* First Row: Area and Value */}
                <div className={styles.gridHeader}>
                    <div className={styles.area}>{item.area}</div>
                    <div className={styles.value}>{item.value}</div>
                </div>

                {/* Second Row: Comments */}
                <div className={styles.commentsContainer}>
                    <div className={styles.commentsBox}>
                        <ul className={styles.commentsList}>
                            {item.comments.map((comment, i) => (
                                <li key={i} className={styles.commentItem}>
                                    <span
                                        className={styles.commentIcon}
                                        onMouseEnter={(e) => {
                                            e.currentTarget.style.backgroundColor = "#6a11cb";
                                        }}
                                        onMouseLeave={(e) => {
                                            e.currentTarget.style.backgroundColor = "#2575fc";
                                        }}
                                    >
                                        ✓
                                    </span>
                                    <span className={styles.commentText}>{comment}</span>
                                </li>
                            ))}
                        </ul>
                    </div>
                </div>
            </div>
        ))}
    </div>
);

export default GridTwoByOne;
