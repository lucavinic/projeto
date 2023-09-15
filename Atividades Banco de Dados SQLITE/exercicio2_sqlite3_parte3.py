import sqlite3
conexao = sqlite3.connect("exercicio2_python.sqlite3")
cursor = conexao.cursor()
comandosql = f'''
    SELECT * FROM Eventos;
'''
dados = cursor.execute(comandosql)
for dado in dados:
    print(dado)

conexao.commit()
conexao.close()