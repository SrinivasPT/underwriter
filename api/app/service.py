from app.database import get_db_connection


# Add a new request to the queue
def add_request_to_queue(request_id, payload):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO request_queue (id, payload, status_code)
    VALUES (UNHEX(%s), %s, 'pending')
    """
    cursor.execute(query, (request_id, payload))
    conn.commit()
    cursor.close()
    conn.close()


# Get the status of a request
def get_request_status(request_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT id, status_code
    FROM request_queue
    WHERE id = UNHEX(%s)
    """
    cursor.execute(query, (request_id,))
    request = cursor.fetchone()
    cursor.close()
    conn.close()
    return request


# Add a response to a completed request
def add_response_to_request(request_id, response_payload):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO request_response (id, payload)
    VALUES (UNHEX(%s), %s)
    """
    cursor.execute(query, (request_id, response_payload))
    conn.commit()
    cursor.close()
    conn.close()


# Get the response for a completed request
def get_response_for_request(request_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    query = """
    SELECT id, payload
    FROM request_response
    WHERE id = UNHEX(%s)
    """
    cursor.execute(query, (request_id,))
    response = cursor.fetchone()
    cursor.close()
    conn.close()
    return response
