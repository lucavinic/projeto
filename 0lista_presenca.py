import sqlite3
conexao = sqlite3.connect('tabela_presenca.sqlite3')
cursor = conexao.cursor()

'''comando_sql = f""" CREATE TABLE Cadastro(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(150),
                    cargo VARCHAR(50),
                    data VARCHAR(25),                    
                    FOREIGN KEY(data) REFERENCES PF(status)
                );"""
cursor.execute(comando_sql)

comando_sql = f""" CREATE TABLE Reuniao(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    duracao INTEGER,
                    data  VARCHAR(25),
                    FOREIGN KEY(duracao) REFERENCES Carga_Horaria(hc)
                );"""
cursor.execute(comando_sql)

comando_sql = f""" CREATE TABLE PF(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(150),
                    data VARCHAR(25),
                    status VARCHAR(20),
                    FOREIGN KEY(status) REFERENCES Carga_Horaria(hc)
                );"""
cursor.execute(comando_sql)

comando_sql = f""" CREATE TABLE Carga_Horaria(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(150),
                    hc INTEGER
                );"""
cursor.execute(comando_sql) '''

def cadastrar_integrantes(conexao):
    cursor = conexao.cursor()

    nome = input("Informe o nome do(a) integrante: ")
    cargo = input("Informe o cargo: ")
    print("Use esse modelo para a data: dd/mm/yyyy")
    data = input("Informe a data do cadastro do(a) integrante: ")

    comando_sql = f"INSERT INTO Cadastro(nome, cargo, data) VALUES (?, ?, ?)"
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

def listar_nomes_cadastrados(conexao):
    cursor = conexao.cursor()
    comando_sql = f"""SELECT * FROM Cadastro WHERE nome"""
    
    cursor.execute(comando_sql)


while True:
    print('---SISTEMA DE PRESENÇA DAS REUNIÕES---')
    print('\n 1) Cadastrar Integrantes', '\n 2) Informar duração reunião', '\n 3) Cadastrar Presença ou Falta', '\n 4) Calcular Horário Complementar Individual', '\n 5) Listar nome(s) já cadastrado', '\n 0) Sair')
    opcao = int(input("O que você deseja?: "))

    if opcao == 0:
        print('FIM DO PROGRAMA!')
        break
    elif opcao == 1:
        cadastrar_integrantes(conexao)

    elif opcao == 2:
        cadastrar_tempo_reuniao(conexao)

    elif opcao == 3:
        cadastrar_pf(conexao)

    elif opcao == 4:
        cadastrar_ch(conexao)
    
    elif opcao == 5:
        listar_nomes_cadastrados(conexao)

    

conexao.commit()
conexao.close()
