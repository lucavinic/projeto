numero = int(input('digite um número: '))
while numero < 1 or numero > 10:
    print('Ops, número inválido, tente novamente!')
    numero = int(input('digite um número: '))
else:
    print('Parabéns. O número estava entre o intervalo de 1 a 10')
print('FIM DO PROGRAMA')