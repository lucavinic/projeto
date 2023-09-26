import pyautogui
import time
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

py = pyautogui

py.PAUSE = 0.3

py.press("win")
py.write("chrome")
py.press("enter")
time.sleep(1)
py.click(x=742, y=623, clicks=2)
py.write(link)
py.press("enter")
time.sleep(4)
py.click(x=779, y=457)
py.write("lucavinic@gmail.com")
py.press("tab")
py.write("tadandocerto")
py.press("tab")
py.press("enter") 

time.sleep(3)


import pandas as pd
tabela = pd.read_csv("c:/Users/Lucas/atividades/Jornada Python/produtos.csv")
print(tabela)

time.sleep(3)

for linha in tabela.index:
    py.click(x=756, y=300)
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario  = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]

    #preencher os campos
    py.write(str(codigo))
    py.press("tab")
    py.write(str(marca))
    py.press("tab")
    py.write(str(tipo))
    py.press("tab")
    py.write(str(categoria))
    py.press("tab")
    py.write(str(preco_unitario))
    py.press("tab")
    py.write(str(custo))
    py.press("tab")


    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        py.write(str(obs))

    py.press("tab") 
    py.press("enter")

    py.scroll(500000)
    