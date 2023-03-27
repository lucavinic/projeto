digitos = int(input("Digite um número para contar seus dígitos : "))
contador = 0
while digitos != 0:
    digitos //= 10
    contador+= 1
print("Total de dígitos = ", contador)
