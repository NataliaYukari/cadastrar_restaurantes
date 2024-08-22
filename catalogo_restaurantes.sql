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

SELECT nome, localizacao, nota, id_categoria, culinaria, preco 
FROM Restaurantes WHERE nome = "Subway";

UPDATE Restaurantes
SET	nome = "Burger King", localizacao = "Shopping Bouleavrd",
 nota = 4, id_categoria = 2, culinaria = "Lanches", preco = "$"
WHERE nome = "Burger King ";

SELECT * FROM Categorias;