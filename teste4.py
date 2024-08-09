import random

# Lista de palavras para escolher uma aleatória
palavras = ["python", "programacao", "computador", "linguagem", "desenvolvimento"]

# Escolhe uma palavra aleatória da lista
palavra_secreta = random.choice(palavras)

# Cria uma lista para armazenar as letras já descobertas
letras_descobertas = ["_"] * len(palavra_secreta)

# Variável para controlar se o usuário ganhou ou não
ganhou = False

print("Bem-vindo ao jogo de adivinhação de palavra!")
print("Você deve adivinhar a palavra letra por letra.")
print("Se você já souber a palavra, pode escrevê-la toda para ganhar!")

while not ganhou:
    # Mostra a palavra com as letras já descobertas
    print(" ".join(letras_descobertas))

    # Pede ao usuário que escolha uma letra ou escreva a palavra toda
    entrada_usuario = input("Escolha uma letra ou escreva a palavra toda: ")

    # Verifica se o usuário escreveu a palavra toda
    if len(entrada_usuario) == len(palavra_secreta):
        # Se sim, verifica se a palavra está correta
        if entrada_usuario == palavra_secreta:
            ganhou = True
            print("Parabéns! Você descobriu a palavra secreta:", palavra_secreta)
        else:
            print("A palavra está incorreta. Tente novamente!")
    else:
        # Se não, verifica se a letra escolhida está na palavra secreta
        if entrada_usuario in palavra_secreta:
            # Se sim, substitui o "_" pela letra escolhida na lista de letras descobertas
            for i, letra in enumerate(palavra_secreta):
                if letra == entrada_usuario:
                    letras_descobertas[i] = entrada_usuario
        else:
            print("A letra escolhida não está na palavra secreta.")

        # Verifica se a palavra foi completamente descoberta
        if "_" not in letras_descobertas:
            ganhou = True
            print("Parabéns! Você descobriu a palavra secreta:", palavra_secreta)