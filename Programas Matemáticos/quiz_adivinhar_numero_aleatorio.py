from random import randint
numero = randint(1, 20)
tentativa = 10
while tentativa > 0:
    chute = int(input('digite um valor para tentar adivinhar o número["entre 1 e 20"]: ')) 
    diferenca = numero - chute 
    if numero == chute:
        print('Parabéns, você acertou!') 
        break
    elif diferenca <= 2 and diferenca >= -2:
        print('Você errou, mas está bem próximo do valor!')
    elif numero > chute:
        print('Você ainda não acertou, o número é maior. Tente novamente.')
    else:
        print('Você ainda não acertou, o número é menor. Tente novamente.')
    tentativa = tentativa - 1
print('o número era: ', numero)
print('Fim do programa!')