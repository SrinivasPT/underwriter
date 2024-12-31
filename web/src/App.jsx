import React from "react";
import AppRoutes from "./routes";
import { Layout } from "./components";
import "bootstrap/dist/css/bootstrap.min.css"; // Bootstrap first
import "./index.css"; // Custom styles second

const App = () => {
    return (
        <Layout>
            <AppRoutes />
        </Layout>
    );
};

export default App;
