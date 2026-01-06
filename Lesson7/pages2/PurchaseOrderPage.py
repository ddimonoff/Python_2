from selenium.webdriver.common.by import By


class PurchaseOrder:
    def __init__(self, driver):
        self.driver = driver


    def post_form(
            self, post_log, post_pass, value1, value2, value3, total_shop
            ):
        self.driver.get(f"https://www.saucedemo.com/checkout-step-one.html"
                        f"?Username={post_log}&password={post_pass}")
        search_input: WebElement = self.driver.find_element(By.NAME,
                                                            'firstName')
        search_input.send_keys(value1)
        search_input: WebElement = self.driver.find_element(By.NAME,
                                                            'lastName')
        search_input.send_keys(value2)
        search_input: WebElement = self.driver.find_element(By.NAME,
                                                            'postalCode')
        search_input.send_keys(value3)
        search_button_log: WebElement = self.driver.find_element(By.NAME,
                                                                 'continue')
        search_button_log.click()
        result = self.driver.find_element(By.CLASS_NAME,
                                          "summary_total_label").text
        result = result[7:]
        assert result == total_shop
