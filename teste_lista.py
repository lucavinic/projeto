notas = []
quantidade_notas = int(input("Qual a quantidade de notas que deseja adicionar? "))
while quantidade_notas > 0:
    nota = float(input("Digite a nota: "))
    quantidade_notas -= 1
    if nota < 0 or nota > 10:
        print("Erro")
        break
    else:
        notas.append(nota)
    
print("A maior nota é",max(notas))
print("A menor nota é", min(notas))


#exemplo usando o .split
"""
# Este código recebe uma lista de números do usuário e imprime o maior e o menor número.
# Recebe uma lista de números do usuário.
numbers = input("Digite uma lista de números separados por vírgulas: ").split(",")
# Converte os números para float.
numbers = [float(number) for number in numbers]
# Imprime o maior e o menor número.
print("O maior número é", max(numbers))
print("O menor número é", min(numbers))
"""