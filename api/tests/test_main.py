from fastapi.testclient import TestClient
import pytest
from app.main import app  # Import your FastAPI app
import uuid

# Create a TestClient instance
client = TestClient(app)


# @pytest.mark.skip(reason="Under development")
def test_create_loan_application():
    # Test data
    payload = {
        "id": str(uuid.uuid4()),
        "bank_statement": {"data": "sample"},
        "cibil_report": {"score": 750},
        "pan": {"number": "ABCDE1234F"},
        "aadhaar": {"number": "123456789012"},
        "loan_application": {"amount": 100000},
    }

    # Make a POST request to the endpoint
    response = client.post("/api/loan-applications", json=payload)

    # Assert the response
    assert response.status_code == 200
    assert "request_id" in response.json()
    assert response.json()["status"] == "pending"


# @pytest.mark.skip(reason="Under development")
def test_get_loan_application_pending():
    # Create a new loan application to get its ID
    payload = {
        "id": str(uuid.uuid4()),
        "bank_statement": {"data": "sample"},
        "cibil_report": {"score": 750},
        "pan": {"number": "ABCDE1234F"},
        "aadhaar": {"number": "123456789012"},
        "loan_application": {"amount": 100000},
    }
    create_response = client.post("/api/loan-applications", json=payload)
    request_id = create_response.json()["request_id"]

    # Make a GET request to check the status
    response = client.get(f"/api/loan-applications/{request_id}")

    # Assert the response
    assert response.status_code == 200
    assert response.json()["status"] == "pending"


def test_get_loan_application_not_found():
    # Use a random UUID that doesn't exist in the database
    random_request_id = uuid.uuid4().hex

    # Make a GET request to check the status
    response = client.get(f"/api/loan-applications/{random_request_id}")

    # Assert the response
    assert response.status_code == 404
    assert response.json()["detail"] == "Request not found"
