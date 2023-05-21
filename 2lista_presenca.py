import sqlite3

def cadastrar_integrantes(conexao):
    cursor = conexao.cursor()

    nome = input("Informe o nome do(a) integrante: ")
    cargo = input("Informe o cargo: ")
    print("Use esse modelo para a data: dd/mm/yyyy")
    data = input("Informe a data do cadastro do(a) integrante: ")

    comando_sql = f"INSERT INTO Presenca(nome, cargo, data) VALUES (?, ?, ?)"
    values = [nome, cargo, data]
    cursor.execute(comando_sql, values)
    conexao.commit()

def cadastrar_tempo_reuniao(conexao):
    cursor = conexao.cursor()

    duracao = int(input("Informe(em minutos) a duração da reunião: "))
    print("Use esse modelo para a data: dd/mm/yyyy")
    data = input("Informe a data da reunião: ")

    comando_sql = f"INSERT INTO Reuniao(duracao, data) VALUES (?, ?)"
    values = [duracao, data]
    cursor.execute(comando_sql, values)
    conexao.commit()

def cadastrar_pf(conexao):
    cursor = conexao.cursor()

    nome = input("Informe o nome do(a) integrante: ")
    print("Use esse modelo para a data: dd/mm/yyyy")
    data = input("Informe a data da reunião atual: ")
    print("")
    status = input('Informe o status, se esse integrante teve presença ou falta nessa reunião: ')

    comando_sql = f"INSERT INTO PF(nome, data, status) VALUES (?, ?, ?)"
    values = [nome, data, status]
    cursor.execute(comando_sql, values)
    conexao.commit()

def cadastrar_ch(conexao):
    cursor = conexao.cursor()

    nome = input("Informe o nome do(a) integrante: ")
    
