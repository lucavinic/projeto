import sqlite3
conexao = sqlite3.connect("exercicio2_python.sqlite3")
cursor = conexao.cursor()
comandosql = f'''
    UPDATE Eventos SET local = 'goiania' WHERE id = 1;
'''
cursor.execute(comandosql)


conexao.commit()
conexao.close()