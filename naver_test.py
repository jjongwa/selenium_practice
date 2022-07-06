from selenium import webdriver
chrome_path = 'C:\\Users\\troas\\Desktop\\selenium\\selenium_practice\\chromedriver.exe'
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_path, chrome_options=options)
URL = 'https://www.naver.com/'
driver.get(URL)