print('Exemplo de polígonos: cubo, prisma, pirâmide, esfera, cilindro')
a = input('informe qual poliedro deseja calcular a área: ')
while True:
    if a == 'cubo':
        b = float(input('qual o lado do cubo? '))
        d = 6 * b**2
        print('A área do cubo é = ', d)
        break
    elif a == 'prisma':
        e = float(input('qual o perímetro da base do prisma? '))
        c = float(input('qual a base do prisma? '))
        f = float(input('qual a altura do prisma? '))
        w = 2*c + (e * f)
        print('A área do prisma é = ', w)
        break
    elif a == 'pirâmide':
        h = float(input('qual o perímetro da base da pirâmide? '))
        g = float(input('qual o valor do apótema da pirâmide? '))
        i = float(input('qual a área da base da pirâmide? '))
        z = (h * g)/2 + (i)
        print('A área da pirâmide é = ', z)
        break
    elif a == 'esfera':
        j = float(input('qual o raio da esfera? '))
        l = 4 * 3.14 * j**2
        print('A área da esfera é = ', l)
        break
    
    elif a == 'cilindro':
        m = float(input('qual o raio do cilindro? '))
        n = float(input('qual a altura do cilindro? '))
        p = (2 * 3.14 * m**2) + (2 * 3.14 * m * n)
        print('A área do trapézio é = ', p)
        break
    
    else:
        print('o valor informado é inválido, por favor, informe o polígono corretamente')
        print('cubo, prisma, pirâmide, esfera, cilindro')
        break