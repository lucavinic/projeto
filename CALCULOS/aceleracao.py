#primeiramente precisa saber qual informação o usuário está precisando sobre M.R.U ou M.R.U.V
print("Ex: velocidade média, aceleração, velocidade inicial/final, etc")
duvida_usuario = input("O que você está querendo encontrar? ")
while True:
    if duvida_usuario == 'velocidade média':
        print("Observação: informe o espaço percorrido em metros")
        espaco = float(input("Qual o espaço percorrido pelo transporte ou pessoa? "))
        print("Observação: informe o tempo em segundos")
        tempo = float(input("Em quanto tempo ele percorreu o trajeto? "))
        velo_media = espaco/tempo
        print(f"A velocidade média foi de {velo_media:.2f}m/s")
        break
    elif duvida_usuario == 'aceleração':
        pergunta1 = input("já tem informação sobre a velocidade inicial? ")
        pergunta2 = input("já tem informação sobre a velocidade final? ")
        pergunta3 = input("já tem informação sobre o tempo percorrido? ")
        if pergunta1 == "sim" and pergunta2 == "sim" and pergunta3 == "sim":
            velo_inicial = float(input("Informe a velocidade inicial: "))
            velo_final = float(input("Informe a velocidade final: "))
            tempo = float(input("Informe o tempo percorrido: "))
            calculo_aceleracao = velo_final/tempo - velo_inicial
            print(f"A aceleração é: {calculo_aceleracao:.2f} m/s^2")
            break
    else: 
        break
