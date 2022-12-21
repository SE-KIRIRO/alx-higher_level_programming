-- a script that creates the database hbtn_0d_2 and the user user_0d_2
-- the user should have only select privilege in the database
-- if the database or the user exists the script should not fail.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost';

