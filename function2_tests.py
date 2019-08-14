from selenium import webdriver

from selenium.webdriver.firefox.options import Options

firefox_options = Options()

firefox_options.add_argument('--headless')


browser = webdriver.Firefox(firefox_options=firefox_options)

browser.get('https://www.baidu.com')

print(browser.current_url)

print(browser.title)
