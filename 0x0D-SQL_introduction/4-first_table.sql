-- SQL script to create the table first_table if it doesn't exist

-- Connect to the MySQL server and create the table if it doesn't exist
/* This script creates the table first_table if it doesn't already exist */

USE hbtn_0c_0; -- Replace dbname with the name of the current database

CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);
