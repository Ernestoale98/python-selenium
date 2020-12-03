#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver


#Clase que hace referencia a la clase TestCase
class RegisterNewUser(unittest.TestCase):

    #Ejecuta todo antes de hacer la prueba 
    @classmethod
    def setUpClass(cls):
       cls.driver = webdriver.Chrome(executable_path=r'./chromedriver')
       driver = cls.driver
       driver.get("http://demo-store.seleniumacademy.com/")
       driver.maximize_window()
       driver.implicitly_wait(15)

    #Crear nuevo usuario
    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/a').click()
        driver.find_element_by_link_text('Log In').click()

        create_account_button = driver.find_element_by_xpath('//*[@id="login-form"]/div/div[1]/div[2]/a')
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()

        self.assertEqual('Create New Customer Account',driver.title)
        
        #Obtener elementos del form
        first_name = driver.find_element_by_id('firstname')
        middle_name = driver.find_element_by_id('middlename')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        submit_button = driver.find_element_by_xpath('//*[@id="form-validate"]/div[2]/button/span/span')
        
        #Verificar que el form este activo
        self.assertTrue(first_name.is_enabled()
                        and middle_name.is_enabled()
                        and last_name.is_enabled()
                        and email_address.is_enabled()
                        and password.is_enabled()
                        and confirm_password.is_enabled()
                        and news_letter_subscription.is_enabled()
                        and submit_button.is_enabled())

        #Mandar info al formulario
        first_name.send_keys('Test')
        middle_name.send_keys('Test')
        last_name.send_keys('Test')
        driver.implicitly_wait(1)
        email_address.send_keys('Test')
        password.send_keys('Test')
        confirm_password.send_keys('Test')
        driver.implicitly_wait(1)
        submit_button.click()
        

    #Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='search_test_report'))
