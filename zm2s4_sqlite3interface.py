import sqlite3
#import zm2s4_sqlite3funcoes #importar a biblioteca, mas demanda que coloquemos nome do arquivo.func
from zm2s4_sqlite3funcoes import *
conexao = sqlite3.connect('nova_tabela.sqlite3')


while True:
    print('\t ---SISTEMA GERENCIAMENTO DE TAREFAS---') 
    print('\n 1)Cadastrar Tarefas', '\n 2)Listar Tarefas', '\n 3)Listar tarefas por data', '\n 4) Deletar tarefa', '\n 5) Atualizar Tarefa', '\n 6) Listar categorias', '\n 7) Deletar categoria', '\n 0) Sair') 
    opcao = int(input("O que você deseja?: "))
    
    if opcao == 0:
        print('PROGRAMA FINALIZADO!')
        break
    elif opcao == 1:
        cadastrar_tarefa(conexao)
    elif opcao == 2:
        listar_tarefas(conexao)
    elif opcao == 3:
        data = input("Digite a data desejada: ")
        listar_tarefas(conexao, data)
    elif opcao == 4:
        deletar_tarefa(conexao)
    elif opcao == 5:
        atualizar_tarefa(conexao)
    elif opcao == 6:
        listar_categorias(conexao)
    elif opcao == 7:
        deletar_categoria(conexao)
    else:
        print("Opção inválida!")
    

conexao.close()
        