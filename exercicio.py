n = int(input("Digite o número de termos: "))
h = 0

for i in range(1, n+1):
    h += 1/i

print(f"O valor de H com {n} termos é: {h:.4f}")


