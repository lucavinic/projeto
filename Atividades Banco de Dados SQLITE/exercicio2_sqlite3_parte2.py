import sqlite3
conexao = sqlite3.connect("exercicio2_python.sqlite3")
# INSERT INTO Eventos VALUES (3, 'show', '14/02/2023', 'santa catarina', 2);
cursor = conexao.cursor()
comandosql = f'''
    INSERT INTO Organizador VALUES (2, 'Sherlon', 'sherlon@gmail', '456254');
'''
cursor.execute(comandosql)

#cursor.execute(f"CREATE TABLE Eventos(id INT NOT NULL, titulo VARCHAR(100), data VARCHAR(20), local VARCHAR(100), referencia INT, PRIMARY KEY (id), FOREIGN KEY (referencia) REFERENCES Organizador (id));")

#cursor.execute(f"CREATE TABLE Organizador(id INT NOT NULL, nome VARCHAR(100), email VARCHAR(100), cpf VARCHAR(11), UNIQUE(email, cpf), PRIMARY KEY(id));")

conexao.commit()
conexao.close()