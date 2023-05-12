import sqlite3

def cadastrar_tarefa(conexao):
    cursor = conexao.cursor()

    tarefa = input('Informe o nome da tarefa que deseja incluir: ')
    data = input("Digite a data: ")
    status = bool(input("Digite o status: "))

    comando_sql = f"INSERT INTO Tarefa(nome, data, status) VALUES (?, ?, ?)"
    values = [tarefa, data, status]
    cursor.execute(comando_sql, values)
    conexao.commit()

def listar_tarefas(conexao, data=None):
    cursor = conexao.cursor()
    if data == None:

        comando_sql = f"""SELECT * FROM Tarefa"""
    else:
        comando_sql = f"""SELECT * FROM Tarefa WHERE data = '{data}'"""

    # Obtenha os resultados da consulta
    cursor.execute(comando_sql)
    dados = cursor.fetchall()
    # Obtenha o número de registros na tabela
    num_registros = len(dados)
    print("Tamanho: ", num_registros)
 
    if num_registros == 0:
        print('Não há dado(s) a ser retornado!')
    else:
        for dado in dados:
            print(dado)

   
        
    


def deletar_tarefa(conexao):
    cursor = conexao.cursor()

    tarefa = int(input)('Informe a tarefa, pelo id, que deseja deletar: ')
    comando_sql = f"""DELETE FROM Tarefa WHERE ={tarefa}"""
    cursor.execute(comando_sql)
    conexao.commit()

def atualizar_tarefa(conexao):
    cursor = conexao.cursor()
    id = int(input('informe, pela id, qual tarefa será atualizada: '))
    tarefa = input("Digite a tarefa: ")
    data = input("Digite a data: ")
    status = bool(input("Digite o status: "))

    at1 = f"""UPDATE Tarefa SET nome = '{tarefa}' WHERE id = {id}"""
    at2 = f"""UPDATE Tarefa SET data = '{data}' WHERE id = {id}"""
    at3 = f"""UPDATE Tarefa SET status = {status} WHERE id = {id}"""
    


