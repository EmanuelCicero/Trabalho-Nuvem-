CREATE DATABASE projeto;



USE projeto;



CREATE TABLE users (

    user_id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(12),

    email VARCHAR(120)

);



INSERT INTO users (username, email) VALUES ('Maria', 'mariazinha@exemplo.com');

INSERT INTO users (username, email) VALUES ('Clodoado', 'clodo@exemplo.com');

INSERT INTO users (username, email) VALUES ('Clodovil', 'vil@exemplo.com');
