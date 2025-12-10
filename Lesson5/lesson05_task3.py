from time import sleep   # задержка
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)
driver.get('http://the-internet.herokuapp.com/inputs')
sleep(1)
search_field = "input"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Sky")
sleep(1)
search_input.clear()
sleep(1)
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
search_input.send_keys("Pro")
sleep(2)
driver.quit()
