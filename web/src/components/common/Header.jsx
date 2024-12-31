import React from "react";

const Header = () => {
    return (
        <header>
            {/* Bootstrap Navbar */}
            <nav
                className="navbar navbar-expand-lg navbar-light bg-light"
                style={{ background: "linear-gradient(45deg,rgb(172, 186, 199) 0%,rgb(14, 32, 109) 100%)" }}
            >
                <div className="container-fluid">
                    {/* Logo */}
                    <a className="navbar-brand" href="/">
                        AccuLoan
                    </a>

                    {/* Toggle Button for Mobile */}
                    <button
                        className="navbar-toggler"
                        type="button"
                        data-bs-toggle="collapse"
                        data-bs-target="#navbarNav"
                        aria-controls="navbarNav"
                        aria-expanded="false"
                        aria-label="Toggle navigation"
                    >
                        <span className="navbar-toggler-icon"></span>
                    </button>

                    {/* Navbar Links */}
                    <div className="collapse navbar-collapse" id="navbarNav">
                        <ul className="navbar-nav ms-auto">
                            <li className="nav-item">
                                <a className="nav-link text-white" href="/">
                                    Home
                                </a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link text-white" href="/analyze">
                                    Analyze
                                </a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link text-white" href="/analyze1">
                                    Analyze One
                                </a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link text-white" href="/about">
                                    About
                                </a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link text-white" href="/contact">
                                    Contact
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    );
};

export default Header;
