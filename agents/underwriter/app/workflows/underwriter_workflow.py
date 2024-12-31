from langgraph.graph import END, START, StateGraph
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import Graph
from langchain_openai import ChatOpenAI
from typing import Dict, Any, List
from pydantic import BaseModel

from app.services.loan_application import analyze_loan_application
from app.services.cibil_report import analyze_cibil_report
from app.services.bank_statement import analyze_bank_statement

load_dotenv()


# Define the state
class WorkflowState(BaseModel):
    id: str
    request_json: Dict[str, Any]  # Use Dict[str, Any] for JSON data
    bank_statement_response: List[Any]  # Use List[Any] for responses
    cibil_report_response: List[Any]  # Use List[Any] for responses
    loan_application_response: List[Any]  # Use List[Any] for responses


# Initialize LLM
# llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
llm = ChatGroq(model="llama-3.3-70b-versatile")


# Define nodes
def analyze_bank_statement_node(state: WorkflowState):
    """
    Analyze the bank statement and update the state.
    """
    bank_statement_data = state.request_json.get("bank_statement")

    response = analyze_bank_statement(bank_statement_data, llm)

    state.bank_statement_response = response

    return state


def analyze_cibil_report_node(state: WorkflowState):
    """
    Analyze the CIBIL report and update the state.
    """
    cibil_report_data = state.request_json.get("cibil_report")

    response = analyze_cibil_report(cibil_report_data, llm)

    state.cibil_report_response = response

    return state


def analyze_loan_application_node(state: WorkflowState):
    """
    Analyze the loan application and update the state.
    """
    policy_document = state.request_json.get("policy_document")
    bank_statement_data = state.request_json.get("bank_statement")
    cibil_report_data = state.request_json.get("cibil_report")
    bank_statement_response = state.bank_statement_response
    cibil_report_response = state.cibil_report_response

    response = analyze_loan_application(
        policy_document,
        bank_statement_data,
        cibil_report_data,
        bank_statement_response,
        cibil_report_response,
        llm,
    )

    state.loan_application_response = response

    return state


# Build the LangGraph workflow
workflow = StateGraph(WorkflowState)

# Add nodes
workflow.add_node("analyze_bank_statement", analyze_bank_statement_node)
workflow.add_node("analyze_cibil_report", analyze_cibil_report_node)
workflow.add_node("analyze_loan_application", analyze_loan_application_node)

# Define parallel execution for bank statement and CIBIL report analysis
workflow.add_edge(START, "analyze_bank_statement")
workflow.add_edge(START, "analyze_cibil_report")

workflow.add_edge("analyze_bank_statement", "analyze_loan_application")
workflow.add_edge("analyze_cibil_report", "analyze_loan_application")
workflow.add_edge("analyze_loan_application", END)

# Compile the workflow
compiled_workflow = workflow.compile()
