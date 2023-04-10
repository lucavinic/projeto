CREATE TABLE Tarefas (
    id INT NOT NULL AUTOINCREMENT,
    nome VARCHAR(100),
    data VARCHAR(20),
    categoria INT,
    status BOOL,
        PRIMARY KEY (id),
        FOREIGN KEY (categoria) REFERENCES Categorias (id)
);

CREATE TABLE Categorias (
    id INT NOT NULL AUTOINCREMENT,
    nome VARCHAR(100),
        PRIMARY KEY (id)
);