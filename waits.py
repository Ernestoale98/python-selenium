#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver

#Ayuda hacer referencia para interactuar
from selenium.webdriver.common.by import By
#Spected conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#Clase que hace referencia a la clase TestCase
class ExplicitWaitTest(unittest.TestCase):

#Ejecuta todo antes de hacer la prueba 
    def setUp(self):
       self.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = self.driver
       driver.get("http://demo-store.seleniumacademy.com/")
       

    def test_account_link(self):
        WebDriverWait
        self.assertEqual

#Cierre de ventana
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_wordl_report'))