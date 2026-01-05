from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def waiting_time(self, delay):
        search_input = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        search_input.clear()
        search_input.send_keys(delay)

    def number_button(self, value):
        search_but_n = self.driver.find_element(
            By.XPATH,
            '//span[@class="btn btn-outline-primary" and text()="{}"]'
            .format(value)
        )
        search_but_n.click()

    def arithmetic_operation(self, value):
        search_but_o = self.driver.find_element(
            By.XPATH,
            '//span[@class="operator btn btn-outline-success" and text()="{}"]'
            .format(value)
        )
        search_but_o.click()

    def equals(self, value):
        search_but_e = self.driver.find_element(
            By.XPATH,
            '//span[@class="btn btn-outline-warning" and text()="{}"]'
            .format(value)
        )
        search_but_e.click()

    def pauses_time(self, value, to_be):
        pauses = value + 5
        WebDriverWait(self.driver, pauses).until(
            EC.text_to_be_present_in_element((
                By.XPATH, '//div[@class="screen"]'), f'{to_be}')
        )

    def get_result(self):
        return self.driver.find_element(
            By.XPATH, '//div[@class="screen"]'
        ).text


    def quit(self):
        self.driver.quit()
