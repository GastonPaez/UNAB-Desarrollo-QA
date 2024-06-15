from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Prueba para login

EMAIL = 'mail@mail.com'
PASSWORD = 'Prueba1234'

# Configura las opciones del navegador Chrome
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')  # Ignora errores de certificado SSL
driver = webdriver.Chrome(options=chrome_options)

driver.maximize_window()
driver.get('http://opencart.abstracta.us/index.php?route=account/login') # Login page
time.sleep(2)

driver.find_element(by=By.NAME, value='email').send_keys(EMAIL)
time.sleep(2)

driver.find_element(by=By.NAME, value='password').send_keys(PASSWORD)
time.sleep(2)

submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]')
submit_button.click()
time.sleep(4)