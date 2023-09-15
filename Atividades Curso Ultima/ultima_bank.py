resultado_total = []
for i in range(5):
    nome = input()
    cpf = input()
    idade = int(input())
    total = {}
    total['Nome']  = nome
    total['CPF']   = cpf
    total['Idade'] = idade
    resultado_total.append(total)

for i in range(5):
    print("Cliente:", resultado_total[i]["Nome"], "CPF:", resultado_total[i]["CPF"], "Idade:", resultado_total[i]["Idade"])