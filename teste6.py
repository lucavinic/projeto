#    lista_nomes = ['Isabel', 'Leticia', 'Carlos', 'Antônio', 'José']

 #   nome_tamanho = [nome for nome in lista_nomes if len(nome) > 6]

#    print(nome_tamanho)

def mistura_palavras(*args):
    return ' '.join(args)


print(mistura_palavras('uma', 'frase', 'dividida', 'em', 'seis', 'parte'))
