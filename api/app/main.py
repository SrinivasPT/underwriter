from fastapi import FastAPI, HTTPException
from app.service import (
    add_request_to_queue,
    get_request_status,
    get_response_for_request,
)
import uuid
import json

app = FastAPI()


# Endpoint to submit a loan application
@app.post("/api/loan-applications")
async def create_loan_application(payload: dict):
    # Generate a unique request ID
    request_id = uuid.uuid4().hex
    # Add the request to the queue with "pending" status
    add_request_to_queue(request_id, json.dumps(payload))
    return {"status": "pending", "request_id": request_id}


# Endpoint to check the status of a loan application
@app.get("/api/loan-applications/{request_id}")
async def get_loan_application(request_id: str):
    # Fetch the request status from the database
    request = get_request_status(request_id)
    if not request:
        raise HTTPException(status_code=404, detail="Request not found")
    # If the request is still pending or processing
    if request["status_code"] != "completed":
        return {"status": request["status_code"]}
    # If the request is completed, fetch the response
    response = get_response_for_request(request_id)
    return {"status": "completed", "response": response["payload"]}
