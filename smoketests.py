from unittest import TestLoader,TestSuite
from pyunitreport import HTMLTestRunner
from assertionstest import AssertionsTest
from searchtests import SearchTests

#Variables para cargar las pruebas

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)


#Crear suite

smoke_test = TestSuite([assertions_test,search_test])

#Crear el reporte
#Por objeto
kwargs = {
    "output":'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)