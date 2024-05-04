-- Active: 1714782933015@@127.0.0.1@3306@db
CREATE DATABASE my_collections;

USE my_collections;

CREATE TABLE my_movies(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Autor VARCHAR(100),
    Descripcion Varchar(500),
    FechadeEstreno VARCHAR(100)
);
