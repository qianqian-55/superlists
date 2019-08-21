from selenium import webdriver

from selenium.webdriver.firefox.options import Options

import unittest

class NewVistorTest(unittest.TestCase):
    def setUp(self):
       self.firefox_options = Options()
#        self.firefox_optiions.add_argument('--headless')
       self.firefox_options.headless = True 
       self.browser = webdriver.Firefox(firefox_options=self.firefox_options)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://c.biancheng.net/python/')
        print(self.browser.current_url)       
        self.assertIn('Python',self.browser.title)
       # self.browser.get('http://172.31.13.15:8080/ESPOS65_MariaDB/')
       # print(self.browser.current_url)
       # self.assertIn('WEB-RMIS',self.browser.title)
        print(self.browser.title)

        self.fail('finish the test!')

if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main(warnings ='ignore')






















#from selenium import webdriver

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

#assert 'Django' in browser.title

##****************************

#from selenium import webdriver
#from selenium.webdriver.firefox.options import Options

#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)
#print('hello,django!!')

