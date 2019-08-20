from selenium import webdriver

from selenium.webdriver.firefox.options import Options

import unittest
import time

class NewVistorTest(unittest.TestCase):
    def setUp(self):
       self.firefox_options = Options()
#        self.firefox_optiions.add_argument('--headless')
       self.firefox_options.headless = True 
       self.browser = webdriver.Firefox(firefox_options=self.firefox_options)
    
    def tearDown(self):
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://127.0.0.1:8000')
        print(self.browser.current_url)       
        self.assertIn('To-Do',self.browser.title)
       # self.browser.get('http://172.31.13.15:8080/ESPOS65_MariaDB/')
       # print(self.browser.current_url)
       # self.assertIn('WEB-RMIS',self.browser.title)
        print(self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)
        print(header_text)
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'),'Enter a to-do item')
        inputbox.send_keys('Buy peacock feather')
        inputbox.send_keys(keys.ENTER)
        time.sleep(1)
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows))
        print(row.text)


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

