from django.shortcuts import render

def inicio(request):
    dados = []
    dados.append(
        {
            'titulo': 'Titulo Legal 1',
            'categoria': 'Categoria 1',
            'Data': '30/08/2022',
        }
    )
    dados.append(
        {
          'titulo': 'Titulo Legal 2',
          'categoria': 'Categoria 2',
          'Data': '29/08/2022',  
        }
    )
    contexto = {
        'dados': dados
    }
    resposta = render(request, 'inicio.html', contexto)
    return resposta

def contato(request):
    return render (request, "contato.html")