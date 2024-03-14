-- Create id_not_null table if it doesn't exist
CREATE TABLE IF NOT EXISTS id_not_null (
    -- This is the id column, which has a default value of 1
    id INT DEFAULT 1,
    -- This is the name column, which can be any string up to 256 characters
    name VARCHAR(256)
);
