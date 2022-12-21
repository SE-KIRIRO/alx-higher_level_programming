-- a script that creates the mysql user user_0d_1
-- the user should have all privileges on the server
-- the password should be user_0d_1_pwd
-- if the user already exists the script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost';

