CREATE TABLE Eventos(
    id INT NOT NULL AUTOINCREMENT,
    titulo VARCHAR(100),
    data VARCHAR(20),
    local VARCHAR(100),
    referencia VARCHAR(100)
        PRIMARY KEY (id), 
        FOREIGN KEY (referencia) REFERENCES Organizador (id)
);


CREATE TABLE Organizador(
    id INT NOT NULL AUTOINCREMENT,
    nome VARCHAR(100),
    email VARCHAR(100),
    cpf VARCHAR(11)
        UNIQUE(cpf, email)
        PRIMARY KEY (id)
);