#Importar libreria con todas las pruebas
import unittest
#Ejecutador de pruebas
from pyunitreport import HTMLTestRunner
#Driver para comunicar con el navegador
from selenium import webdriver

#Pack para dropdown
from selenium.webdriver.support.ui import Select

#Clase que hace referencia a la clase TestCase
class SelectLanguage(unittest.TestCase):

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
            #el orden respeta como aparecen en la página
            exposed_options = ['English','French','German']
            #para almacenar las opciones que elijamos
            active_options = []
            #para acceder a las opciones del dropdown
            select_language = Select(self.driver.find_element_by_id('select-language'))
            #para comprobar que si esté la cantidad de  opciones correcta
            #'options' permite ingresar directamente a las opciones del dropdown
            self.assertEqual(3, len(select_language.options))

            print(select_language.options)

            for option in select_language.options:
                active_options.append(option.text)
            
            #verifico que la lista de opciones disponibles y activas sean indénticas
            self.assertListEqual(exposed_options,active_options)

            #vamos a verificar la palabra "English" sea la primera opción seleccionada del dropdown
            self.assertEqual('English', select_language.first_selected_option.text)

            #seleccionamos "German" por el texto visible
            select_language.select_by_visible_text('German')

            #verificamos que el sitio cambio a Alemán
            #preguntamos a selenium si la url del sitio contiene esas palabras
            self.assertTrue('store=german' in self.driver.current_url)

            select_language = Select(self.driver.find_elements_by_id('select-language'))
            select_language.select_by_index(0)

    #Cierre de ventana
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes',report_name='select_language_report'))
