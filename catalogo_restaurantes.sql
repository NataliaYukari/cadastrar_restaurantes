CREATE DATABASE catalogo_restaurantes;
USE catalogo_restaurantes;

CREATE TABLE Categorias (
	id_categoria INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

CREATE TABLE Restaurantes (
	id_restaurante INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    localizacao VARCHAR(50) NOT NULL,
    nota INT NOT NULL,
    id_categoria INT NOT NULL,
    culinaria VARCHAR(50) NOT  NULL,
    preco VARCHAR(5) NOT NULL,
    
    
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);

INSERT INTO Categorias (nome) VALUES
("Familiar/Casual"),
("Fast food"),
("Café"),
("Luxo"),
("Clássico");

SELECT * FROM Restaurantes;

SELECT * FROM Categorias;