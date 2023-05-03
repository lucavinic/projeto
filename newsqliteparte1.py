import sqlite3
conexao = sqlite3.connect('novo_banco_dados.sqlite3')
cursor = conexao.cursor()

cursor.execute(f"CREATE TABLE evento(id NOT NULL, nome VARCHAR(50), data VARCHAR(20), PRIMARY KEY(id));")

cursor.execute(f"CREATE TABLE selecoes(id NOT NULL, nome_selecao VARCHAR(50), PRIMARY KEY(id), FOREIGN KEY(nome_selecao) REFERENCES confrontos(confronto));")

cursor.execute(f"CREATE TABLE confrontos(id NOT NULL, confronto VARCHAR(200), data VARCHAR(20), PRIMARY KEY(id));")

conexao.commit()
conexao.close()