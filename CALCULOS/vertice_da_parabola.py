print('Para que possamos calcular o valor do vértice precisamos ter ciência de algumas coisas.')
print("De forma resumida, precisamos saber o valor do 'a', 'b' e do delta")
a = input('Já possue o valor do Delta? s/n:' )
if a == 's':
    b = float(input("Qual o valor de 'a'?"  ))
    c = float(input("Qual o valor de 'b'?" ))
    d = float(input("Qual o valor do DELTA?" ))
    v1 = (-c)/2*b
    v = (-d)/4*b
    print('Os valores dos vértices são: ', v1, 'e', v)
else:
    print('Vamos primeiramente calcular o DELTA')
    e = float(input("Informe o valor do 'a':" ))
    f = float(input("Informe o valor do 'b':" ))
    g = float(input("Informe o valor do 'c':" ))
    h = f**2 - (4*e*g)
    print('O valor do seu DELTA é =', h)
    print('Agora vamos para o cáculo do vértice')
    b = float(input("Qual o valor de 'a'?"  ))
    c = float(input("Qual o valor de 'b'?" ))
    d = float(input("Qual o valor do DELTA?" ))
    v1 = (-c)/2*b
    v = (-d)/4*b
    print('Os valores dos vértices são: ', v1, 'e', v)
print('FIM DO PROGRAMA!')

