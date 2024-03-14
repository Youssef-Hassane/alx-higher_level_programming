-- This SQL script creates the 'hbtn_0d_usa' database and the 'cities' table.
-- The 'cities' table contains information about US cities.

-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create the 'cities' table if it doesn't exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    -- Define the primary key (id)
    PRIMARY KEY(id),

    -- Define the id column, which is the primary key
    id       INT          NOT NULL AUTO_INCREMENT,

    -- Define the state_id column, which is a foreign key referencing the 'states' table
    state_id INT          NOT NULL,

    -- Define the name column, which stores the name of the city
    name     VARCHAR(256) NOT NULL,

    -- Define the foreign key constraint
    FOREIGN KEY(state_id)
    REFERENCES hbtn_0d_usa.states(id)
);
