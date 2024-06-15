import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Prueba de categorias ingresando en sus productos y añadiendo al carrito

class categories_navigation_unittest(unittest.TestCase):
    
    def setUp(self):        
        self.driver=webdriver.Chrome()    

    def test_cart(self):
        driver = self.driver 
        driver.get("http://opencart.abstracta.us/")        
        
        # Encuentro el menu de categorias
        # Esperar a que el elemento nav con id "menu" esté presente
        menu = driver.find_element(By.ID, "menu")

        # Obtener todos los enlaces dentro del elemento nav con id "menu"
        categorias = menu.find_elements(By.TAG_NAME, "a")
        print(categorias)
        time.sleep(1)
        # Iterar sobre cada enlace
        for categoria in categorias:
            # Hacer clic en el enlace para desplegar las subcategorías
            categoria.click()
            time.sleep(1)
            
            # Esperar a que aparezcan las subcategorías
            subcategorias = driver.find_element(By.CLASS_NAME, "dropdown-inner")            
            # Obtener los enlaces dentro de las subcategorías
            enlaces_subcategoria = subcategorias.find_elements(By.TAG_NAME, "a")
            
            # Iterar sobre cada enlace de la subcategoría
            for enlace in enlaces_subcategoria:
                # Obtener la URL del enlace
                enlace.click()
                time.sleep(2)
                try: 
                    # Busco todos los elementos con la clase 'product-thumb'
                    products = driver.find_elements(By.CLASS_NAME, 'product-thumb')                    
                    # Por cada producto encontrado voy a ingresar en cada uno de ellos
                    for product in products:
                        time.sleep(2)
                        prod = product.find_element(By.CLASS_NAME, 'image')                    
                        link_prod = prod.find_element(By.TAG_NAME, 'a')
                        link_prod.click()
                        time.sleep(3)
                        
                    # Hacer clic en el botón "Add to Cart"
                        try:
                            add_to_cart_button = driver.find_element(By.ID, 'button-cart')
                            add_to_cart_button.click()
                            time.sleep(3)
                            
                            print("Producto agregado al carrito")
                        except Exception:
                            print("No se encontró el botón 'Add to Cart'")

                    
                except Exception as e:
                    print(f"No se encontraron productos: {str(e)}")
                
                driver.back()
                time.sleep(1)                
                
            driver.back()
            time.sleep(1)
                        
            
        assert "No se encontro el elemento:" not in driver.page_source      
        
    def tareaDown(self):
        self.driver.close()
        
if __name__ == "__main__":
    unittest.main()
    
    