import React from "react";
import Header from "../header/Header";
import Footer from "../footer/Footer";

const Layout = ({ children }) => {
    return (
        <div className="d-flex flex-column min-vh-100">
            <Header />

            <main className="flex-grow-1">
                <div className="container-fluid">{children}</div>
            </main>

            <Footer />
        </div>
    );
};

export default Layout;
