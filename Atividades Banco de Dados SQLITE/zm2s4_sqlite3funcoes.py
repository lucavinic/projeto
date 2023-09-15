import sqlite3

def cadastrar_tarefa(conexao):
    cursor = conexao.cursor()

    tarefa = input('Informe o nome da tarefa que deseja incluir: ')
    data = input("Digite a data: ")
    status = bool(input("Digite o status: "))
    listar_categorias(conexao)
    opcao = int(input("Digite '1' para selecionar categoria existente e '2' para cadastrar uma nova categoria"))
    if opcao == 1:
        categoria = int(input('Digite o id da categoria a ser cadastrado: '))
    elif opcao == 2:
        cadastrar_categorias(conexao)
        listar_categorias(conexao)
        categoria = int(input('Digite o id da categoria a ser cadastrado: '))

    comando_sql = f"INSERT INTO Tarefa(nome, data, status, categoria) VALUES (?, ?, ?, ?)"
    values = [tarefa, data, status, categoria]
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

    conexao.commit()
    

def listar_categorias(conexao):
    cursor = conexao.cursor()
    comando_sql = f"SELECT * FROM Categoria"

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


def cadastrar_categorias(conexao):
    cursor = conexao.cursor()
    
    nome = input('Informe o nome da categoria que deseja incluir: ')


    comando_sql = f"INSERT INTO Categoria(nome) VALUES (?)"
    values = [nome]
    cursor.execute(comando_sql, values)
    conexao.commit()


def deletar_categoria(conexao):
    cursor = conexao.cursor()
    listar_categorias(conexao)
    id = int(input('Informe a categoria, pelo id, que deseja deletar: '))
    comando_sql = f"""DELETE FROM Categoria WHERE id = {id}"""
    cursor.execute(comando_sql)
    conexao.commit()







