from requests_html import HTMLSession 
url = 'http://www.google.com.br/'
sessao = HTMLSession()
resposta = sessao.get(url)
print(resposta.text)
print(resposta.status_code)
