import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.story("Авторизация")
class Autorize:
    def __init__(self, driver):
        self.driver = driver
        with allure.step("Открытие страницы авторизации"):
            self.driver.get("https://www.saucedemo.com")

    @allure.step("Авторизация по данным логин: "
                 "{value_log}, пароль: {value_pass}")
    @allure.epic("Магазин")
    def log_name(self, value_log, value_pass):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, 'user-name'))
            )
        self.driver.maximize_window()
        with allure.step("Введение логина " + value_log):
            search_input = self.driver.find_element(
                By.CSS_SELECTOR, '#user-name'
            )
            search_input.send_keys(value_log)
        with allure.step("Введение пароля " + value_pass):
            search_input = self.driver.find_element(
                By.CSS_SELECTOR, '#password'
            )
            search_input.send_keys(value_pass)
        with allure.step("Нажатие кнопки Login"):
            search_button_log = self.driver.find_element(
                By.CSS_SELECTOR, '#login-button'
                )
        search_button_log.click()
