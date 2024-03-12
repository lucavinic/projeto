from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time 



# Inicialize o WebDriver do Chrome
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.maximize_window()

# Navegue até o site
navegador.get('https://apps.fas.usda.gov/psdonline/app/index.html#/app/advQuery')


#Funções clicáveis
def selecionar_commodity(navegador, commodity_index):
    # Espera até que o elemento <select> seja carregado e visível
    elemento_select = WebDriverWait(navegador, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "select[ng-model='vm.criteria.commodities']"))
    )
    
    
    # Cria uma instância de Select usando o elemento encontrado
    select = Select(elemento_select)
    
    # Seleciona a opção pelo texto visível
    #select.select_by_visible_text(commodity_name)
    select.select_by_index(commodity_index)
    
def selecionar_atributos(navegador):
    # Espera até que o elemento <select> seja carregado e visível
    elemento_select = WebDriverWait(navegador, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "select[ng-model='vm.criteria.attributes']"))
    )
    
    
    # Cria uma instância de Select usando o elemento encontrado
    select = Select(elemento_select)
    
    # Seleciona a opção pelo texto visível
    #select.select_by_visible_text(commodity_name)
    select.select_by_value("number:88")
    
    
def selecionar_market(navegador):
    # Espera até que o elemento <select> seja carregado e visível
    elemento_select = WebDriverWait(navegador, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "select[ng-model='vm.criteria.marketYears']"))
    )
    
    
    # Cria uma instância de Select usando o elemento encontrado
    select = Select(elemento_select)
    
    # Seleciona a opção pelo texto visível
    #select.select_by_visible_text(commodity_name)
    select.select_by_value("number:2024")
    select.select_by_value("number:2023")
    
def selecionar_top(navegador):
    # Localizar o checkbox pelo seletor CSS usando o valor do atributo ng-model
    checkbox = navegador.find_element(By.CSS_SELECTOR, "input[type='checkbox'][ng-model='vm.criteria.chkTopCountry']")

    # Clicar no checkbox
    checkbox.click()
    
def selecionar_top5(navegador):
    # Espera até que o elemento <select> seja carregado e visível
    elemento_select = WebDriverWait(navegador, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "select[ng-model='vm.criteria.topCountryCount']"))
    )
    
    
    # Cria uma instância de Select usando o elemento encontrado
    select = Select(elemento_select)
    
    # Seleciona a opção pelo texto visível
    #select.select_by_visible_text(commodity_name)
    select.select_by_value("5")
    
def selecionar_run(navegador):
    # Clique no botão usando a classe
    run = '/html/body/div[2]/div[3]/div/div[2]/div[8]/div/button[1]'
    select_run = navegador.find_element(By.XPATH, run)
    select_run.click()
    
def selecionar_download(navegador):
    # Clique no botão usando a classe
    run = '/html/body/div[2]/div[3]/div/div[3]/div[1]/a[2]/i'
    select_run = navegador.find_element(By.XPATH, run)
    select_run.click()
    
def selecionar_back(navegador):
    # Clique no botão usando a classe
    run = '/html/body/div[2]/div[3]/div/div[3]/div[1]/a[1]/i'
    select_run = navegador.find_element(By.XPATH, run)
    select_run.click()
    
def selecionar_reset(navegador):
    # Clique no botão usando a classe
    run = '/html/body/div[2]/div[3]/div/div[2]/div[8]/div/button[2]'
    select_run = navegador.find_element(By.XPATH, run)
    select_run.click()
    
    
    
for index in range(62):
    # Selecione o primeiro elemento pelo índice
    selecionar_commodity(navegador, index)
    time.sleep(1)
    selecionar_atributos(navegador)
    selecionar_market(navegador)
    selecionar_top(navegador)
    selecionar_top5(navegador)
    time.sleep(1)
    selecionar_run(navegador)
    time.sleep(1)
    selecionar_download(navegador)
    selecionar_back(navegador)
    time.sleep(1)
    selecionar_reset(navegador)