import allure
from selenium.webdriver.common.by import By


@allure.story("Корзина")
class Basket:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Проверка наличия товаров в корзине")
    @allure.epic("Магазин")
    def basket_form(self, shop_log, shop_pass, value1, value2, value3):
        with allure.step("Открытие страницы Корзина"):
            self.driver.get(f"https://www.saucedemo.com/cart.html"
                        f"?Username={shop_log}&password={shop_pass}")
        products = self.driver.find_elements(By.CLASS_NAME,
                                             "inventory_item_name")
        product_names = [product.text for product in products]
        with allure.step("Tовар " + product_names[0] + " выбран"):
            assert product_names[0] == value1
        with allure.step("Tовар " + product_names[1] + " выбран"):
            assert product_names[1] == value2
        with allure.step("Tовар " + product_names[2] + " выбран"):
            assert product_names[2] == value3

        with allure.step("Нажатие кнопки Checkout"):
            search_check = self.driver.find_element(
                By.XPATH, '//button[text()="Checkout"]')
        search_check.click()
