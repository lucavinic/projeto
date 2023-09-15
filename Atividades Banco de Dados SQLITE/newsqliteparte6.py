import sqlite3
conexao = sqlite3.connect('novo_banco_dados.sqlite3')
cursor = conexao.cursor()

comandosql = f'''
    SELECT COUNT(id) FROM selecoes
'''
dados = cursor.execute(comandosql)
for dado in dados:
    print(dado)

conexao.commit()
conexao.close()