DROP DATABASE IF EXISTS `teste`;

CREATE DATABASE `teste`;

USE `teste`;

CREATE TABLE `alunos`(
      `id` BIGINT NOT NULL AUTO_INCREMENT,
      `name` VARCHAR(225) NOT NULL,
      `email` VARCHAR(225) NOT NULL UNIQUE,
      `cpf` VARCHAR(20) NOT NULL UNIQUE,
      `data_nascimento` VARCHAR(20) NOT NULL,
      PRIMARY KEY (id)
);