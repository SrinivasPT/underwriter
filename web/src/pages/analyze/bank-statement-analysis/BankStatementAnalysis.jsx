import GridTwoByOne from "@/components/features/gridrow/GridTwoByOne.jsx";
import { REPORT_DOC } from "../data.js";

const BankStatementAnalysis = () => {
    return <GridTwoByOne data={REPORT_DOC.bank_statement_analysis} />;
};

export default BankStatementAnalysis;
