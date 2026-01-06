from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Autorize:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com")


    def log_name(self, value_log, value_pass):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
            )
        self.driver.maximize_window()
        search_input = self.driver.find_element(By.CSS_SELECTOR, '#user-name')
        search_input.send_keys(value_log)
        search_input = self.driver.find_element(By.CSS_SELECTOR, '#password')
        search_input.send_keys(value_pass)
        search_button_log = self.driver.find_element(
            By.CSS_SELECTOR, '#login-button'
            )
        search_button_log.click()
