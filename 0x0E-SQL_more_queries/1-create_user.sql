-- Create the MySQL server user user_0d_1
-- Grant all privileges on the MySQL server to user_0d_1
-- Set user_0d_1s password to user_0d_1_pwd
-- Do not fail if user_0d_1 already exists
CREATE USER 
    IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL 
    ON *.* 
    TO user_0d_1@localhost;
FLUSH PRIVILEGES;
