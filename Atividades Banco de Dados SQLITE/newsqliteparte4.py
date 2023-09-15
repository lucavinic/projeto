import sqlite3
conexao = sqlite3.connect('novo_banco_dados.sqlite3')
cursor = conexao.cursor()

comando = f'''
    SELECT * FROM confrontos;
'''
dados = cursor.execute(comando)


for dado in dados:
    print(dado)


conexao.commit()
conexao.close()