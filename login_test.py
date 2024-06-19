from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Lista de credenciales para probar
credentials = [
    {"EMAIL": 'mail@mail.com', "PASSWORD": 'Prueba1234'},
    {"EMAIL": 'aargento@mail.com', "PASSWORD": 'Prueba1234'}
]

# Configura las opciones del navegador Chrome
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')  # Ignora errores de certificado SSL
driver = webdriver.Chrome(options=chrome_options)
# URL de la página de login
login_url = 'https://opencart.abstracta.us/index.php?route=account/login'

# Función para probar el login, la limpieza del input con .clear() nos permite realizar varias pruebas en caso de fallo.
def login_test(email, password):
    driver.get(login_url)
    time.sleep(2)
    
    driver.find_element(by=By.NAME, value='email').clear()
    driver.find_element(by=By.NAME, value='email').send_keys(email)
    time.sleep(2)
    
    driver.find_element(by=By.NAME, value='password').clear()
    driver.find_element(by=By.NAME, value='password').send_keys(password)
    time.sleep(2)
    
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]')
    submit_button.click()
    time.sleep(4)
    
    
    
    try:
        account_dashboard = driver.find_element(By.LINK_TEXT, 'Logout')
        print(f"La prueba de inicio de sesion ha sido exitosa con el usuario: {email}")
    except:
        print(f"Se ha producido un error al iniciar sersion con el usuario: {email}")

# Realiza las pruebas con todas las credenciales incorporadas
for creds in credentials:
    login_test(creds['EMAIL'], creds['PASSWORD'])


driver.quit()
