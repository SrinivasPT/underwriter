import { useContext } from "react";
import { PageContext } from "@/context/PageContext";
import GridTwoByOne from "@/components/features/gridrow/GridTwoByOne.jsx";

const BankStatementAnalysis = () => {
    const { state, dispatch } = useContext(PageContext);

    return <GridTwoByOne data={state.data?.bank_statement_analysis} />;
};

export default BankStatementAnalysis;
