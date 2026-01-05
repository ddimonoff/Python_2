from selenium.webdriver.common.by import By


class Basket:
    def __init__(self, driver):
        self.driver = driver


    def basket_form(self, shop_log, shop_pass, value1, value2, value3):
        self.driver.get(f"https://www.saucedemo.com/cart.html"
                        f"?Username={shop_log}&password={shop_pass}")
        products = self.driver.find_elements(By.CLASS_NAME,
                                             "inventory_item_name")
        product_names = [product.text for product in products]
        assert product_names[0] == value1
        assert product_names[1] == value2
        assert product_names[2] == value3

        search_check = self.driver.find_element(By.XPATH,
                                                '//button[text()="Checkout"]')
        search_check.click()
