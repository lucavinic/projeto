('\t ---- PROGRAMA DE CONTABILIDADE ----')
def media(chave):
    qtd_meses = len(resultado_total)
    soma = 0
    for i in resultado_total:
        soma += i[chave]
    media = soma / qtd_meses
    return media

resultado_total = []
while True:
    print('Informe o que deseja executar no programa')
    print("Digite '1' para calcular o lucro através das vendas e gastos")
    print("Digite '2' para calcular a média das informações fornecidas da opção 1")
    print("Digite '3' para finalizar o programa")
    opcao = int(input('Digite a opção: '))
    if opcao == 1:
        mes = input('informe o mês que deseja inserir os dados: ').capitalize()
        gasto = float(input('Digite o gasto do mês: '))
        venda = float(input('Digite a venda do mês: '))
        lucro = venda - gasto
        if lucro > 0:
            print(f"Seu lucro é de: {lucro:.2f}")
        else:
            print("seu prejuizo é de: ", abs(lucro))

        total = {}
        total['Mês'] = mes
        total['Gasto'] = gasto
        total['Venda'] = venda
        total['Lucro'] = lucro
        resultado_total.append(total)
    elif opcao == 2:
        print(f"Média Gasto: {media('Gasto')}")
        print(f"Média Venda: {media('Venda')}")
        print(f"Média Lucro: {media('Lucro')}")
    else:
        print('FIM DO PROGRAMA')
        break
print(resultado_total)
