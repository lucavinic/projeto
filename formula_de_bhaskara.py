a = float(input('informe o valor de a: '))
b = float(input('informe o valor de b: '))
c = float(input('informe o valor de c: '))
calculo1 = (-b) + ((b ** 2) - 4 * a * c) ** (1/2)
calculo2 = (-b) - ((b ** 2) - 4 * a * c) ** (1/2)
if calculo1 % 2 == 0 and calculo2 % 2 == 0:
    print('Raiz 1 = ', (calculo2/2) * (-1))
    print('Raiz 2 = ', (calculo1/2) * (-1))

else:
    print('Raiz 1 = ', calculo2 * (-1))
    print('Raiz 2 = ', calculo1 * (-1))