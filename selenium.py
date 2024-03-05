import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

py = pyautogui

# Inicialize o WebDriver do Chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

# Navegue até o site
navegador.get('https://apps.fas.usda.gov/psdonline/app/index.html#/app/advQuery')

# Defina a lista de nomes usando o XPath fornecido
nomes_xpath = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[1]/select'
market_years24 = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[4]/select/option[1]'
market_years23 = '/html/body/div[2]/div[3]/div/div[2]/div[2]/div[4]/select/option[2]'
countries = '/html/body/div[2]/div[3]/div/div[2]/div[4]/div[3]/select/option[2]'

# Encontre o elemento select correspondente ao XPath
select_element = navegador.find_element(By.XPATH, nomes_xpath)
select_years1 = navegador.find_element(By.XPATH, market_years24)
select_years2 = navegador.find_element(By.XPATH, market_years23)
select_country = navegador.find_element(By.XPATH, countries)

# Obtenha a lista de opções desse elemento select
opcoes = select_element.find_elements(By.TAG_NAME, 'option')

# Iterar sobre cada opção
for opcao in opcoes:
    # Clique nela para selecioná-la
    opcao.click() 
    py.click(x=675, y=515, clicks=2)
    select_years.click()
    select_years1.click()
    select_years2.click()
    countries.click()