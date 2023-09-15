while True:
    total = 0
    while True:
        preco = float(input("Digite o preço da mercadoria (ou 0 para encerrar a compra): "))
        if preco == 0:
            break
        total += preco
    
    print("Total da compra: R$ %.2f" % total)
    
    while True:
        dinheiro = float(input("Digite o valor em dinheiro fornecido pelo cliente: "))
        if dinheiro >= total:
            break
        print("O valor fornecido é insuficiente. Tente novamente.")
    
    troco = dinheiro - total
    print("Troco: R$ %.2f" % troco)
    
    opcao = input("Deseja realizar outra compra? (s/n): ")
    if opcao == "n":
        break