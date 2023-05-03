import sqlite3
conexao = sqlite3.connect('novo_banco_dados.sqlite3')
cursor = conexao.cursor()

comandosql = f'''
    INSERT INTO evento VALUES (1, 'COPA DO MUNDO', 20/11/2022);
'''
cursor.execute(comandosql)

conexao.commit()
conexao.close()