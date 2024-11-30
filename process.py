from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
# Inicia o driver com o serviço correto
def iniciar(domain):
    # Caminho para o ChromeDriver
    service = Service("/home/axl/bots/chromedriver")
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.registro.br/")
    pesquisa = driver.find_element(By.ID, "is-avail-field")
    pesquisa.clear()#limpando a barra de pesquisa
    pesquisa.send_keys(f"{domain}")
    pesquisa.send_keys(Keys.RETURN)
    sleep(6)
    print(driver.title)
    driver.quit()