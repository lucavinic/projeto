import sqlite3

conexao = sqlite3.connect('tabela_presenca.sqlite3')


while True:
    print('---SISTEMA DE PRESENÇA DAS REUNIÕES---')
    print('\n 1) Cadastrar Integrantes', '\n 2) Informar duração reunião', '\n 3) Cadastrar Presença ou Falta', '\n 4) Calcular Horário Complementar Individual', '\n 0) Sair')
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

conexao.close()
