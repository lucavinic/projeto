a = float(input('informe o valor de a: '))
b = float(input('informe o valor de b: '))
c = float(input('informe o valor de c: '))
delta = ((b ** 2) - 4 * a * c)
while True:
    if delta < 0:
        print("Não há raiz real")
        break
    elif delta == 0:
        print("Só existe uma raiz")
        calculo1 = (-b) + ((b ** 2) - 4 * a * c) ** (1/2)
        resultado_1 = calculo1/(2 * a)
        print('Raiz 1 = ', (resultado_1) )
        break
    else:
        print("Há duas raízes")
        calculo1 = (-b) + ((b ** 2) - 4 * a * c) ** (1/2)
        calculo2 = (-b) - ((b ** 2) - 4 * a * c) ** (1/2)
        resultado_1 = calculo1/(2 * a)
        resultado_2 = calculo2/(2 * a)
        print('Raiz 1 = ', (resultado_1) )
        print('Raiz 2 = ', (resultado_2) )
        break