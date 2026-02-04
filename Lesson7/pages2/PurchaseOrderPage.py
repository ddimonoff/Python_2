import allure
from selenium.webdriver.common.by import By


@allure.story("Заполнение формы")
class PurchaseOrder:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Заполнение формы заказа")
    def post_form(
            self, post_log, post_pass, value1, value2, value3, total_shop
            ):
        with allure.step("Открытие формы получателя"):
            self.driver.get(f"https://www.saucedemo.com/checkout-step-one.html"
                        f"?Username={post_log}&password={post_pass}")
        with allure.step("Заполнение поля Имя - " + value1):
            search_input: WebElement = self.driver.find_element(
                By.NAME, 'firstName')
            search_input.send_keys(value1)
        with allure.step("Заполнение поля Фамилия - " + value2):
            search_input: WebElement = self.driver.find_element(
                By.NAME, 'lastName')
            search_input.send_keys(value2)
        with allure.step("Заполнение поля Индекс - " + str(value3)):
            search_input: WebElement = self.driver.find_element(
                By.NAME, 'postalCode')
            search_input.send_keys(value3)
        with allure.step("Нажатие кнопки Continue"):
            search_button_log: WebElement = self.driver.find_element(
                By.NAME, 'continue')
            search_button_log.click()
        with allure.step("Возврат полученного результата"):
            result = self.driver.find_element(
                By.CLASS_NAME, "summary_total_label").text
            result = result[7:]
        with allure.step("Проверка результата"):
            assert result == total_shop

        with allure.step("Нажатие кнопки Finish"):
            search_finish_log: WebElement = self.driver.find_element(
                By.NAME, 'finish')
            search_finish_log.click()
