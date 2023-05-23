import sqlite3
conexao = sqlite3.connect('tabela_presenca.sqlite3')
cursor = conexao.cursor()

comando_sql = f""" CREATE TABLE if not exists Cadastro(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    nome VARCHAR(150),
                    cargo VARCHAR(50),
                    data VARCHAR(25), 
                    ch INTEGER,                  
                    FOREIGN KEY(data) REFERENCES PF(status)
                );"""
cursor.execute(comando_sql)

comando_sql = f""" CREATE TABLE if not exists Reuniao(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    duracao INTEGER,
                    horario VARCHAR(25),
                    data  VARCHAR(25),
                    FOREIGN KEY(duracao) REFERENCES Carga_Horaria(hc)
                );"""
cursor.execute(comando_sql)

comando_sql = f""" CREATE TABLE if not exists PF(
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    id_integ INTEGER,
                    id_reuniao INTEGER,
                    status VARCHAR(20),
                    FOREIGN KEY(id_integ) REFERENCES Cadastro(id),
                    FOREIGN KEY(id_reuniao) REFERENCES Reuniao(id)
                );"""
cursor.execute(comando_sql)



def cadastrar_integrantes(conexao):
    cursor = conexao.cursor()

    nome = input("Informe o nome do(a) integrante: ")
    cargo = input("Informe o cargo: ")
    print("Use esse modelo para a data: dd/mm/yyyy")
    data = input("Informe a data do cadastro do(a) integrante: ")

    comando_sql = f"INSERT INTO Cadastro(nome, ch, cargo, data) VALUES (?, ?, ?, ?)"
    values = [nome, 0,  cargo, data]
    cursor.execute(comando_sql, values)
    conexao.commit()

def cadastrar_tempo_reuniao(conexao):
    cursor = conexao.cursor()

    duracao = int(input("Informe(em minutos) a duração da reunião: "))
    print("Use esse modelo para as horas: hh:mm")
    horario = input("Informe o horário da reunião: ")
    print("Use esse modelo para a data: dd/mm/yyyy")
    data = input("Informe a data da reunião: ")

    comando_sql = f"INSERT INTO Reuniao(duracao, horario, data) VALUES (?, ?, ?)"
    values = [duracao, horario, data]
    cursor.execute(comando_sql, values)
    conexao.commit()

def cadastrar_pf(conexao):
    cursor = conexao.cursor()
    listar_nomes_cadastrados(conexao)

    id_integ = int(input("Informe o id do(a) integrante: "))
    listar_reunioes_cadastrados(conexao)

    id_reuniao = int(input("Informe o id da reunião: "))
    status = ''
    while status not in['presente', 'falta']:
        print("Digite 'presente' ou 'falta'!")
        status = input('Informe o status, se esse integrante teve presença ou falta nessa reunião: ').lower()

    comando_sql = f"INSERT INTO PF(id_integ, id_reuniao, status) VALUES (?, ?, ?)"
    values = [id_integ, id_reuniao, status]
    cursor.execute(comando_sql, values)
    calculo_ch(conexao, id_integ, id_reuniao, status)
    conexao.commit()

def calculo_ch(conexao, id_integ, id_reuniao, status):
    cursor = conexao.cursor()
    if status == 'presente':
        cursor.execute(f"SELECT duracao FROM Reuniao WHERE id = {id_reuniao}")
        tempo = cursor.fetchall()[0][0]
        
        cursor.execute(f"SELECT ch FROM Cadastro WHERE id = {id_integ}")
        tempo_anterior = cursor.fetchall()[0][0]
        

        cursor.execute(f"UPDATE Cadastro SET ch = {tempo_anterior + tempo} WHERE id = {id_integ}")
        conexao.commit()


def listar_reunioes_cadastrados(conexao):
    cursor = conexao.cursor()
    comando_sql = f"""SELECT * FROM Reuniao"""
    dados = cursor.execute(comando_sql)
    for dado in dados:
        print(dado)

def listar_nomes_cadastrados(conexao):
    cursor = conexao.cursor()
    comando_sql = f"""SELECT * FROM Cadastro"""
    dados = cursor.execute(comando_sql)
    for dado in dados:
        print(dado)
    


while True:
    print('---SISTEMA DE PRESENÇA DAS REUNIÕES---')
    print('\n 1) Cadastrar Integrantes', '\n 2) Informar duração reunião', '\n 3) Cadastrar Presença ou Falta', '\n 4) Listar nome(s) já cadastrado', '\n 0) Sair')
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
        listar_nomes_cadastrados(conexao)

    

conexao.commit()
conexao.close()
