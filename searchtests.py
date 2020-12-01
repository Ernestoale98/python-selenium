#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver


#Clase que hace referencia a la clase TestCase
class SearchTests(unittest.TestCase):

    #Ejecuta todo antes de hacer la prueba 
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = cls.driver
       driver.get("http://demo-store.seleniumacademy.com/")
       driver.maximize_window()
       driver.implicitly_wait(15)

    
    def test_search_field(self):
        driver = self.driver
        #Obtener la barra de busqueda
        search_field = driver.find_element_by_name("q")
        #Limpiar la barra de busqueda
        search_field.clear()
        #Enviar texto al input
        search_field.send_keys('tee')
        #Enviar busqueda
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        #Obtener la barra de busqueda
        search_field = driver.find_element_by_name("q")
        #Limpiar la barra de busqueda
        search_field.clear()
        #Enviar texto al input
        search_field.send_keys('salt shaker')
        #Enviar busqueda
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1,len(products))

    #Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='search_test_report'))
