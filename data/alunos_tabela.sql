
CREATE DATABASE IF NOT EXISTS escola;

USE escola;

CREATE TABLE IF NOT EXISTS aluno (
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(255),
    data_nascimento DATE,
    situacao VARCHAR(255),
    PRIMARY KEY (id)

);