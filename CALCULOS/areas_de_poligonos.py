print('Exemplo de polígonos: triângulo, quadrado, retângulo, paralelogramo, trapézio')
a = input('informe qual polígono deseja calcular a área: ')
while True:
    if a == 'triângulo':
        b = float(input('qual a base do triângulo? '))
        c = float(input('qual a altura do triângulo? '))
        d = (b*c)/2
        print('A área do triângulo é = ', d)
        break
    elif a == 'quadrado':
        e = float(input('qual o lado do quadrado? '))
        f = e**2
        print('A área do quadrado é = ', f)
        break
    elif a == 'retângulo':
        h = float(input('qual a altura do retângulo? '))
        g = float(input('qual o comprimento do retângulo? '))
        i = h * g
        print('A área do retângulo é = ', i)
        break
    elif a == 'paralelogramo':
        j = float(input('qual a base do paralelogramo? '))
        k = float(input('qual a altura do paralelogramo? '))
        l = j * k
        print('A área do paralelogramo é = ', l)
        break
    
    elif a == 'trapézio':
        m = float(input('qual o valor da base menor? '))
        n = float(input('qual o valor da base maior? '))
        o = float(input('qual o valor da altura? '))
        p = (m + n) * o / 2
        print('A área do trapézio é = ', p)
        break
    
    else:
        print('o valor informado é inválido, por favor, informe o polígono corretamente')
        print('triângulo', 'quadrado', 'retângulo', 'paralelogramo', 'trapézio')
        a = input('informe qual polígono deseja calcular a área: ')
