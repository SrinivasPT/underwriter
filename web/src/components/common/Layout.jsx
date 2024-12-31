import React from "react";
import Header from "./Header";
import Footer from "./Footer";

const Layout = ({ children }) => {
    return (
        <div className="d-flex flex-column min-vh-100">
            <Header />

            <main className="flex-grow-1">
                <div className="container-fluid px-0 py-0">{children}</div>
            </main>

            <Footer />
        </div>
    );
};

export default Layout;
