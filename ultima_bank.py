resultado_total = []
for i in range(5):
    nome = input('digite seu nome: ').capitalize()
    cpf = int(input('digite seu CPF: '))
    idade = int(input('digite sua idade: '))
    total = {}
    total['Nome']  = nome
    total['CPF']   = cpf
    total['Idade'] = idade
    resultado_total.append(total)
print(resultado_total)
