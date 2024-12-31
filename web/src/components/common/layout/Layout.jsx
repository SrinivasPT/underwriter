import React from "react";
import Header from "../header/Header";
import Footer from "../footer/Footer";

const Layout = ({ children }) => {
    return (
        <div className="d-flex flex-column vh-100">
            {/* Fixed Header */}
            <header className="flex-shrink-0 bg-light" style={{ height: "82px" }}>
                <Header />
            </header>

            {/* Scrollable Main Content */}
            <main className="flex-grow-1 d-flex flex-column overflow-auto">
                <div className="container">{children}</div>
            </main>

            {/* Fixed Footer */}
            <footer className="flex-shrink-0 bg-light" style={{ height: "40px" }}>
                <Footer />
            </footer>
        </div>
    );
};

export default Layout;
