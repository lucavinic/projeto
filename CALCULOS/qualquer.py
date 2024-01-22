valor_total = float(input("Informe o valor total que deseja gastar: "))
anos_iniciais = int(input("Informe a quantidade de anos iniciais: "))
gastos_mensais = float(input("Informe a quantidade que deseja gastar por mês: "))

anos_totais = 0
gastos_acumulados = 0

while gastos_acumulados < valor_total:
    anos_totais += 1
    gastos_mensais_desse_ano = 0
    
    if anos_totais == 1:
        gastos_mensais_desse_ano = gastos_mensais * (12 - anos_iniciais)
    else:
        gastos_mensais_desse_ano = gastos_mensais * 12
    
    gastos_acumulados += gastos_mensais_desse_ano

print(f"Você precisará de {anos_totais} anos para gastar esse valor total.")