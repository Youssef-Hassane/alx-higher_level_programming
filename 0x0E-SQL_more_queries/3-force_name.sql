-- If the table force_name already exists, your script should not fail
-- The database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
