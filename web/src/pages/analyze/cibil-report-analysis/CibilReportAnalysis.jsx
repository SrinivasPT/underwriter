import { useContext } from "react";
import { PageContext } from "@/context/PageContext";
import GridTwoByOne from "@/components/features/gridrow/GridTwoByOne.jsx";

const CibilReportAnalysis = () => {
    const { state, dispatch } = useContext(PageContext);
    return <GridTwoByOne data={state.data?.cibil_report_analysis} />;
};

export default CibilReportAnalysis;
