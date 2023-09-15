import sqlite3
conexao = sqlite3.connect("exercicio2_python.sqlite3")
cursor = conexao.cursor()
comandosql = f'''
   DELETE FROM Eventos WHERE id = 3;
'''
cursor.execute(comandosql)


conexao.commit()
conexao.close()