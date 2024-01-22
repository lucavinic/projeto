from datetime import datetime

def lista_cadastros(nomes, nascimentos, codigos):
    lista_de_cadastros = []
    
    for i in range(len(nomes)):
        # Obter a idade do cliente
        nascimento = datetime.strptime(nascimentos[i], '%d/%m/%Y')
        idade = (datetime.now() - nascimento).days // 365
        
        # Adicionar o cadastro na lista apenas se a idade for maior que 30 anos
        if idade > 30:
            cadastro = (nomes[i], nascimentos[i], codigos[i])
            lista_de_cadastros.append(cadastro)
    
    return lista_de_cadastros

nomes = ['João', 'Maria', 'Pedro', 'Arthur']
nascimentos = ['15/06/1990', '20/01/1980', '15/05/1985', '27/07/2005']
codigos = ['123456', '134567', '145678', '123457']

lista_de_cadastros = lista_cadastros(nomes, nascimentos, codigos)
print(lista_de_cadastros)