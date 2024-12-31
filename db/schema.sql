CREATE TABLE request_queue (
    id              BINARY(16) PRIMARY KEY,
    payload         JSON NOT NULL,
    status_code     ENUM('pending', 'processing', 'completed', 'failed', 'cancelled') NOT NULL DEFAULT 'pending',
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE request_response(
	id              BINARY(16) PRIMARY KEY,
	payload			JSON
)
