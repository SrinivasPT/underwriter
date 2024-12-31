# app/main.py
from fastapi import FastAPI
from apscheduler.schedulers.background import BackgroundScheduler
from app.batch.processor import process_pending_requests

app = FastAPI()

# Initialize scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(
    process_pending_requests, "interval", seconds=30
)  # Poll every 30 seconds
scheduler.start()


@app.on_event("shutdown")
def shutdown_event():
    scheduler.shutdown()
