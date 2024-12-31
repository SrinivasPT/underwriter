import GridTwoByOne from "@/components/features/gridrow/GridTwoByOne.jsx";
import { REPORT_DOC } from "../data.js";

const LoanApplicationReview = () => {
    return <GridTwoByOne data={REPORT_DOC.loan_application_review} />;
};

export default LoanApplicationReview;
