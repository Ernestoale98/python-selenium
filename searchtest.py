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
       driver.get("http://demo-store.seleniumacademy.com/")
       driver.maximize_window()
       driver.implicitly_wait(15)

    #Get element by id
    def test_get_by_id(self):
        search_field = self.driver.find_element_by_id("search");
        
    #Get element by name        
    def test_get_by_name(self):
        search_field = self.driver.find_element_by_name("q");
       
    #Get element by class name        
    def test_get_by_class(self):
        search_field = self.driver.find_element_by_class_name("input-text");  

    #Get button and verify if is enable
    def test_verify_button(self):
        button = self.driver.find_element_by_class_name("button")

    #Banner list     
    def test_promos_list(self):
        banner = self.driver.find_element_by_class_name("promos")
        banner_list = banner.find_elements_by_tag_name('img')
        self.assertEqual(3,len(banner_list))

    #Get element by Xpath
    def test_by_xpath(self):
        element = self.driver.find_element_by_xpath('//*[@id="search_autocomplete"]')    

#Get element css selector
    def test_by_xpath(self):
        element = self.driver.find_element_by_css_selector('div.header-minicart span.icon')



    #Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='search_test_report'))
