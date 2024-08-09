
def verificar_valor(valor):
    try:
        # Tenta converter o valor para um número
        num = float(valor)
        
        # Verifica se o número é inteiro
        if num.is_integer():
            print("O valor é um número inteiro.")
        else:
            print("O valor é um número flutuante.")
        
        # Verifica se o número é par ou ímpar
        if num % 2 == 0:
            print("O valor é par.")
        else:
            print("O valor é ímpar.")
    
    except ValueError:
        # Se o valor não for um número, imprime uma mensagem
        print("O valor informado não é um número.")

# Recebe o valor do usuário
valor = input("Digite um valor: ")

# Chama a função para verificar o valor
verificar_valor(valor)
