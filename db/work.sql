/*
DELETE FROM request_queue
SELECT HEX(id) id, payload, status_code, created_at, updated_at FROM request_queue;
SELECT id, status_code FROM request_queue WHERE id = UNHEX('08FCE8E87C644DE0A2DA879D4FF554EF')

UPDATE request_queue SET updated_at = NULL, locked_by = NULL, status_code = 'pending'

*/

SELECT HEX(id) AS ID, payload, status_code, locked_by, created_at, updated_at FROM request_queue