from selenium import webdriver

from selenium.webdriver.firefox.options import Options

firefox_options = Options()

firefox_options.add_argument('--headless')


browser = webdriver.Firefox(firefox_options=firefox_options)

#browser.get('https://www.baidu.com')
#browser.get('http://172.31.13.15:8080/ESPOS65_MariaDB/')
browser.get('http://c.biancheng.net/python/')
print(browser.current_url)

print(browser.title)
