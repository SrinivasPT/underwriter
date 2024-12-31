import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "@/pages/home/Home";
import About from "@/pages/about/About";
import Analyze from "@/pages/analyze/Analyze";
import Analyze1 from "@/pages/analyze/Analyze1";

const AppRoutes = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/analyze" element={<Analyze />} />
                <Route path="/analyze1" element={<Analyze1 />} />
                <Route path="/about" element={<About />} />
                {/* <Route path="*" element={<NotFound />} /> */}
            </Routes>
        </Router>
    );
};

export default AppRoutes;
