import { useContext } from "react";
import { PageContext } from "@/context/PageContext";
import GridTwoByOne from "@/components/features/gridrow/GridTwoByOne.jsx";

const LoanApplicationReview = () => {
    const { state, dispatch } = useContext(PageContext);
    return <GridTwoByOne data={state.data?.loan_application_review} />;
};

export default LoanApplicationReview;
