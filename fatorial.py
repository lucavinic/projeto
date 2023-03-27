num = int(input("Digite um número inteiro: "))
while num < 0:
    print("Não é possível calcular o fatorial de um número negativo.")
    num = int(input("Digite um número inteiro: "))
else:
    if num == 0 or num == 1:
        print("O fatorial de", num, "é 1")
    else:
        fatorial = 1
        for i in range(2, num + 1):
            fatorial *= i
        print("O fatorial de", num, "é", fatorial)