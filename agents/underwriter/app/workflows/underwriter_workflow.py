import time
from langgraph.graph import END, START, StateGraph
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from typing import Annotated, Dict, Any, List, TypedDict

from pydantic import BaseModel

from app.services.loan_application import analyze_loan_application
from app.services.cibil_report import analyze_cibil_report
from app.services.bank_statement import analyze_bank_statement

import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()


# Define the state
class WorkflowState(TypedDict):
    id: str
    request_json: Dict[str, Any]  # Use Dict[str, Any] for JSON data
    bank_statement_response: List[Any]  # Use List[Any] for responses
    cibil_report_response: List[Any]  # Use List[Any] for responses
    loan_application_response: List[Any]  # Use List[Any] for responses


# Initialize LLM
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, max_retries=2)
# llm = ChatGroq(model="llama-3.3-70b-versatile", max_retries=3, retry_delay=10)


# Define nodes
def analyze_bank_statement_node(
    state: WorkflowState,
) -> Annotated[Dict[str, Any], "bank_statement_response"]:
    """
    Analyze the bank statement and update the state.
    """
    logger.info("Analyzing the bank statement...")
    bank_statement_data = state["request_json"].get("bank_statement")

    time.sleep(1)  # 1-second delay

    response = analyze_bank_statement(bank_statement_data, llm)
    logger.info(response)

    return {"bank_statement_response": response}


def analyze_cibil_report_node(
    state: WorkflowState,
) -> Annotated[Dict[str, Any], "cibil_report_response"]:
    """
    Analyze the CIBIL report and update the state.
    """
    logger.info("Analyzing the Cibil Report...")
    cibil_report_data = state["request_json"].get("cibil_report")

    time.sleep(2)  # 1-second delay

    response = analyze_cibil_report(cibil_report_data, llm)
    logger.info(response)

    return {"cibil_report_response": response}


def analyze_loan_application_node(
    state: WorkflowState,
) -> Annotated[Dict[str, Any], "loan_application_response"]:
    """
    Analyze the loan application and update the state.
    """
    logger.info("Analyzing the loan application...")

    policy_document = state["request_json"].get("policy_document")
    bank_statement_data = state["request_json"].get("bank_statement")
    cibil_report_data = state["request_json"].get("cibil_report")
    bank_statement_response = state["bank_statement_response"]
    cibil_report_response = state["cibil_report_response"]

    time.sleep(3)  # 1-second delay

    response = analyze_loan_application(
        policy_document,
        bank_statement_data,
        cibil_report_data,
        bank_statement_response,
        cibil_report_response,
        llm,
    )
    logger.info(response)

    return {"loan_application_response": response}


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
