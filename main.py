import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


class loggin_unittest(unittest.TestCase):
    
    def setUp(self):        
        self.driver=webdriver.Chrome()    

    def test_buscar(self):
        driver = self.driver 
        driver.get("http://opencart.abstracta.us/")        
        elemento = driver.find_element(By.NAME, 'search')
        elemento.send_keys("mac")
        elemento.send_keys(Keys.RETURN)
        time.sleep(4)
        
        # Busco todos los elementos con la clase 'product-thumb'
        products = driver.find_elements(By.CLASS_NAME, 'product-thumb')
    
        # Por cada producto encontrado voy a ingresar en cada uno de ellos
        for product in products:
            
            prod = product.find_element(By.CLASS_NAME, 'image')                    
            link_prod = prod.find_element(By.TAG_NAME, 'a')
            link_prod.click()
            time.sleep(3)
            driver.back()            
            
        assert "No se encontro el elemento:" not in driver.page_source      
        
    def tareaDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()