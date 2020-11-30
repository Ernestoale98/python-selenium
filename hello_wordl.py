#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver


#Clase que hace referencia a la clase TestCase
class HellowWorld(unittest.TestCase):

#Ejecuta todo antes de hacer la prueba 
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = cls.driver
       driver.implicitly_wait(10)

#Caso de prueba para abrir platzi
    def test_hello_word(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

#Caso de prueba para abrir facebook
    def test_hello_facebook(self):
        driver = self.driver
        driver.get('https://www.facebook.com')

#Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_wordl_report'))


#Para correr las pruebas en una solo ventana de Chrome
#Es necesario usar el decorador
#classMethod en las funciones setUp y tearDown
#y remplazarlo por self
#ademas de agregarle el nombre de Class a las funciones

