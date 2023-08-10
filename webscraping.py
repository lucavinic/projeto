from requests_html import HTMLSession
sessao = HTMLSession()
url = 'https://www.imovelweb.com.br/apartamentos-venda-porto-alegre-rs.html?utm_source=google&utm_medium=cpc&utm_campaign=Search_Sale_PA_tipo-inmueble_KW&utm_content=Apartamentos&utm_term=apartamentos%20a%20venda%20em%20pa&iv_=__iv_p_1_a_16391250159_g_139535555011_w_kwd-303867041974_h_9101249_ii__d_c_v__n_g_c_584162787969_k_apartamentos%20a%20venda%20em%20pa_m_b_l__t__e__r__vi__'
resposta = sessao.get(url)
links = resposta.html.find('postings-container')
anuncios = []
for link in links:
    url_imoveis = link.attrs['href']
    resposta_imoveis = sessao.get(url_imoveis)
    titulo = resposta_imoveis.html.find('h1', first = True).text
    preco = resposta_imoveis.html.find('h2', first = True).text
    anuncios.append({
        'url': url_imoveis,
        'titulo': titulo,
        'preco': preco
    })
print(anuncios)

    