from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

# Inicializa o serviço do GeckoDriver
service = Service(GeckoDriverManager().install())

# Inicializa o navegador Firefox
navegador = webdriver.Firefox(service=service)

# Abre uma página da web
navegador.get('https://www.hashtagtreinamentos.com/cursos-hashtag-treinamentos')
time.sleep(1)

# Preenchendo nome, email e enviando o cadastro
navegador.find_element(By.ID, 'firstname').send_keys("Teste")
navegador.find_element(By.ID, 'email').send_keys("lixeira_21@yahoo.com.br")
navegador.find_element(By.XPATH, '/html/body/footer/div/div/div[1]/div[3]/div/form/button').click()
