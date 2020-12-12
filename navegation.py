#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver

#Para hacer pausas aunque no es recomendado
from time import sleep

#Clase que hace referencia a la clase TestCase
class CompareProducts(unittest.TestCase):

#Ejecuta todo antes de hacer la prueba 
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = cls.driver
       driver.get("https://google.com/")
       driver.maximize_window()
       driver.implicitly_wait(15)

#Caso de prueba para abrir platzi
    def test_browser_navegation(self):
        driver = self.driver
        searchField = driver.find_element_by_name('q')
        searchField.clear()
        searchField.send_keys('platzi')
        searchField.submit()

        #Regresar a pagina anterior
        driver.back()
        sleep(3)
        #Ir a la siguiente pagina
        driver.forward()
        sleep(3)
        #Regrescar pagina 
        driver.refresh()
        sleep(3)



#Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_wordl_report'))


#Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_wordl_report'))

