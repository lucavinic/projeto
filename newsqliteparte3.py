import sqlite3
conexao = sqlite3.connect('novo_banco_dados.sqlite3')
cursor = conexao.cursor()

comandosql = f'''
    UPDATE evento SET data = ('20/11/2022');
'''
cursor.execute(comandosql)

conexao.commit()
conexao.close()