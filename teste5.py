def letra_mais_repetida(palavra):
    # Cria um dicionário vazio para contar as letras
    contagem = {}

    # Percorre cada caractere na palavra
    for char in palavra:
        # Verifica se o caractere é uma letra (ignora espaços, pontuações, etc.)
        if char.isalpha():
            # Converte a letra para minúscula para não contar maiúsculas e minúsculas separadamente
            char = char.lower()
            # Se a letra já está no dicionário, incrementa o contador
            if char in contagem:
                contagem[char] += 1
            # Se a letra não está no dicionário, adiciona com contador 1
            else:
                contagem[char] = 1


    # Encontra a letra mais repetida
    letra_mais_repetida = max(contagem, key=contagem.get)

    return letra_mais_repetida

# Pede a palavra ao usuário
palavra = input("Digite uma palavra: ")

# Chama a função e imprime o resultado
print("A letra mais repetida é:", letra_mais_repetida(palavra))