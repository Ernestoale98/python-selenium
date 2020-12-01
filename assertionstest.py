#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


#Clase que hace referencia a la clase TestCase
class AssertionsTest(unittest.TestCase):

    #Ejecuta todo antes de hacer la prueba 
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = cls.driver
       driver.get("http://demo-store.seleniumacademy.com/")
       driver.maximize_window()
       driver.implicitly_wait(15)

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME,'q'))

    def test_languages_option(self):
        self.assertTrue(self.is_element_present(By.ID,'select-language'))    

    #Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


    #Funcion para saber si un elemento esta presente
    #How indica el tipo de selecto
    #What el valor del selector
    def is_element_present(self,how,what):
        try:
            self.driver.find_element(by=how,value=what)
        except NoSuchElementException as exeption:
            return False
        return True        






if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_wordl_report'))
