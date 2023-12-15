CREATE TABLE test_schema.test_table
(
    id_test_table    SERIAL PRIMARY KEY,
    log_uuid         VARCHAR(64),
    log_datetime     TIMESTAMP,
    ip_address       VARCHAR(32),
    http_method      VARCHAR(32),
    uri              VARCHAR(256),
    http_status_code INTEGER
);

/* Test request */
INSERT INTO test_schema.test_table(log_uuid,
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
