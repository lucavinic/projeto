from tkinter import *
from Projeto_lista_presenca import*
root = Tk()

def cadastrar_integrantes_button():
    cadastrar_integrantes(conexao)

def cadastrar_tempo_reuniao_button():
    cadastrar_tempo_reuniao(conexao)

def cadastrar_pf_button():
    cadastrar_pf(conexao)

def listar_nomes_cadastrados_button():
    listar_nomes_cadastrados(conexao)

label = Label(root, text='---SISTEMA DE PRESENÇA DAS REUNIÕES---')
label.pack()

button1 = Button(root, text='1) Cadastrar Integrantes', command=cadastrar_integrantes_button)
button1.pack()

button2 = Button(root, text='2) Informar duração reunião', command=cadastrar_tempo_reuniao_button)
button2.pack()

button3 = Button(root, text='3) Cadastrar Presença ou Falta', command=cadastrar_pf_button)
button3.pack()

button4 = Button(root, text='4) Listar nome(s) já cadastrado', command=listar_nomes_cadastrados_button)
button4.pack()

root.mainloop()









