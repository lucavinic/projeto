nome = input('digite seu nome(mínimo 4 caracteres): ') 
idade = int(input('informe sua idade: '))
salario = float(input('informe seu salário: '))
sexo = input("Sexo ('f' para feminino ou 'm' para masculino): ")
civil = input("informe estado civil('s','c', 'v','d' ): ")
while len(nome) <= 3:
    print('poucos caracteres para o nome')
    nome = input('digite seu nome[mínimo 4 caracteres]: ')
while idade <= 0 or idade > 150:
    print('idade deve ser maior que 0 e menor que 150')
    idade = int(input('informe sua idade: '))
while salario <= 0:
    print('valor inválido, deve ser maior que 0')
    salario = float(input('informe seu salário: '))
print('com', idade, 'anos,', nome, 'recebeu um salário de: R$', salario)




