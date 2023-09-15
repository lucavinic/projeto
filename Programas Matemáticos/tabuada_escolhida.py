montar = int(input('digite o numero que deseja calcular a tabuada: '))
inicio = int(input('informe a partir de quanto calcular: '))
fim = int(input('informe até quanto calcular: '))
print(f'A tabuada do numéro {montar} de {inicio} até {fim} é: ')
for i in range(inicio, fim + 1):
    tentativa = montar * i
    print(i, 'x', montar, '=', tentativa)