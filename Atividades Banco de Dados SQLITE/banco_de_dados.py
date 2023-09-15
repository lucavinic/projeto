import sqlite3
conexao = sqlite3.connect("meu_banco.sqlite3")
cursor = conexao.cursor()
#cursor.execute(f"CREATE TABLE Categoria(id INT NOT NULL, nome VARCHAR(50), PRIMARY KEY (id) );")
cursor.execute(f"INSERT INTO Categoria VALUES (2, 'Sherlon');")
conexao.commit()
conexao.close()