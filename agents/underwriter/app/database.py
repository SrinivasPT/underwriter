import mysql.connector
import os
from dotenv import load_dotenv
import logging
import socket
import time
from app.workflows.underwriter_workflow import compiled_workflow

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

# Unique identifier for the current instance
INSTANCE_ID = socket.gethostname()  # Or use a unique ID for each instance


def get_db_connection():
    """
    Create and return a MySQL database connection using environment variables.
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT")),  # Ensure port is an integer
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
        )
        return connection
    except Exception as e:
        logger.error(f"Error connecting to the database: {e}")
        raise


def process_pending_requests():
    """Poll the database for pending requests, process them, and update the status."""
    connection = None
    request = None
    try:
        # Connect to the database
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Fetch and lock the oldest pending request
        cursor.execute(
            """
            SELECT HEX(id) AS id, payload
            FROM request_queue
            WHERE status_code = 'pending' AND locked_by IS NULL
            ORDER BY created_at ASC
            LIMIT 1
            FOR UPDATE SKIP LOCKED
            """
        )
        request = cursor.fetchone()

        if request:
            logger.info(f"Processing request ID: {request['id']}")

            # Lock the request for the current instance
            cursor.execute(
                """
                UPDATE request_queue
                SET locked_by = %s, status_code = 'processing', updated_at = NOW()
                WHERE id = UNHEX(%s)
                """,
                (INSTANCE_ID, request["id"]),
            )
            connection.commit()

            # Run the workflow (ensure compiled_workflow is defined or imported)
            payload = request["payload"]
            result = compiled_workflow.invoke(payload)

            # Update the request with the result and mark as completed
            cursor.execute(
                """
                UPDATE request_queue
                SET status_code = 'completed', locked_by = NULL, updated_at = NOW()
                WHERE id = UNHEX(%s)
                """,
                (request["id"],),
            )
            connection.commit()

            # Insert the response into the request_response table
            cursor.execute(
                """
                INSERT INTO request_response (id, response)
                VALUES (UNHEX(%s), %s)
                """,
                (request["id"], result),
            )
            connection.commit()

            logger.info(f"Completed processing request ID: {request['id']}")
            return True  # Indicate that a record was processed
        else:
            logger.info("No pending requests found.")
            return False  # Indicate that no records were processed
    except Exception as e:
        logger.error(f"Error processing request: {e}")
        if request and connection:
            # Release the lock and revert status to pending on error
            cursor.execute(
                """
                UPDATE request_queue
                SET status_code = 'pending', locked_by = NULL, updated_at = NOW()
                WHERE id = UNHEX(%s)
                """,
                (request["id"],),
            )
            connection.commit()
        return False  # Indicate that processing failed
    finally:
        if connection:
            cursor.close()
            connection.close()


def poll_and_process():
    """
    Poll the database every 5 minutes and process pending records in a loop.
    """
    while True:
        try:
            # Process pending records in a loop
            while process_pending_requests():
                logger.info("Found pending records. Processing...")

            # No more pending records found, wait for 5 minutes
            logger.info("No pending records found. Resuming polling in 5 minutes...")
            time.sleep(300)  # Sleep for 5 minutes (300 seconds)
        except Exception as e:
            logger.error(f"Unexpected error in poll_and_process: {e}")
            logger.info("Restarting the polling loop after an error...")
            time.sleep(300)  # Sleep for 5 minutes before retrying


# Start the polling and processing loop
if __name__ == "__main__":
    poll_and_process()
