#from selenium import webdriver

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')

#assert 'Django' in browser.title

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
print('hello,django!!')

