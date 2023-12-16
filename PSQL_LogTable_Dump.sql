CREATE TABLE log_table
(
    id_log_table     SERIAL PRIMARY KEY,
    log_uuid         VARCHAR(64),
    log_datetime     TIMESTAMP,
    ip_address       VARCHAR(32),
    http_method      VARCHAR(32),
    uri              VARCHAR(256),
    http_status_code INTEGER
);


/* Test request */
INSERT INTO log_table(log_uuid,
                      log_datetime,
                      ip_address,
                      http_method,
                      uri,
                      http_status_code)
VALUES (gen_random_uuid(),
        CURRENT_TIMESTAMP,
        '192.168.1.1',
        'GET',
        '/example',
        200);


/* Check log_table */
SELECT *
FROM log_table;


/* Test rows count in table */
SELECT COUNT(*)
FROM log_table;


/* Create new database, if needed */
/*
CREATE DATABASE test_db;
\c test_db;
CREATE SCHEMA test_schema;
*/


/* Create new user, if needed */
/*
CREATE ROLE test_user WITH LOGIN PASSWORD 'qwerty';
GRANT CONNECT, CREATE ON DATABASE test_db TO test_user;
GRANT USAGE ON SCHEMA test_schema TO test_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA test_schema TO test_user;
*/
