
use test;
INSERT INTO users (name, email) VALUES ('Alice', 'ace@example.com');

select * from users;

ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'Test@123';
FLUSH PRIVILEGES;
