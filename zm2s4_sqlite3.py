import sqlite3
conexao = sqlite3.connect('nova_tabela.sqlite3')
cursor = conexao.cursor()

comando_sql = f"""CREATE TABLE Categoria(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(50)
                );"""
cursor.execute(comando_sql)

comando_sql = f"""CREATE TABLE Tarefa(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                    nome VARCHAR(100), 
                    data VARCHAR(25), 
                    categoria INTEGER, 
                    status BOOL, 
                    FOREIGN KEY(categoria) REFERENCES Categoria(id)
                );"""
cursor.execute(comando_sql)

conexao.commit()
conexao.close()


