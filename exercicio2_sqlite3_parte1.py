import sqlite3
conexao = sqlite3.connect("exercicio2_python.sqlite3")
cursor = conexao.cursor()

cursor.execute(f"CREATE TABLE Eventos(id INT NOT NULL, titulo VARCHAR(100), data VARCHAR(20), local VARCHAR(100), referencia INT, PRIMARY KEY (id), FOREIGN KEY (referencia) REFERENCES Organizador (id));")

#cursor.execute(f"CREATE TABLE Organizador(id INT NOT NULL, nome VARCHAR(100), email VARCHAR(100), cpf VARCHAR(11), UNIQUE(email, cpf), PRIMARY KEY(id));")

conexao.commit()
conexao.close()