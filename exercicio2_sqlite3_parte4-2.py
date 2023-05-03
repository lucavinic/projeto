import sqlite3
conexao = sqlite3.connect("exercicio2_python.sqlite3")
cursor = conexao.cursor()
novo_local = input('Digite o novo local: ')
comandosql = f'''
    UPDATE Eventos SET local = '{novo_local}' WHERE id = 1;
'''
cursor.execute(comandosql)


conexao.commit()
conexao.close()