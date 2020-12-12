#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver


#Clase que hace referencia a la clase TestCase
class CompareProducts(unittest.TestCase):

#Ejecuta todo antes de hacer la prueba 
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = cls.driver
       driver.get("http://demo-store.seleniumacademy.com/")
       driver.maximize_window()
       driver.implicitly_wait(15)

#Caso de prueba para abrir platzi
    def test_compare_products_removal_alert(self):
        driver = self.driver
        searchField = driver.find_element_by_name('q')
        searchField.clear()

        searchField.send_keys('tee')
        searchField.submit()

        driver.find_element_by_class_name('link-compare').click()

        driver.find_element_by_link_text("Clear All").click()

        alert = driver.switch_to_alert()
        alert_text = alert.text

        get_attribute

        self.assertEqual('Are you sure you would like to remove all products from your comparison?',alert_text)

        alert.accept()




#Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='hello_wordl_report'))

