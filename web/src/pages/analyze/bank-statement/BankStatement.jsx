import GridTwoByOne from "@/components/features/gridrow/GridTwoByOne.jsx";
import { REPORT_DOC } from "../data.js";

const BankStatement = () => {
    return <GridTwoByOne data={REPORT_DOC.bank_statement} />;
};

export default BankStatement;
