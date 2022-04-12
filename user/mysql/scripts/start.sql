ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY $ENTER_PW_HERE';
FLUSH PRIVILEGES;
SELECT user,authentication_string,plugin,host FROM mysql.user;
CREATE DATABASE user;
CREATE DATABASE book;

