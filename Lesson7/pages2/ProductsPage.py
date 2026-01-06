from selenium.webdriver.common.by import By


class Products:
    def __init__(self, driver):
        self.driver = driver


    def prod_select(
            self, shop_log, shop_pass, value1, value2, value3
            ):
        self.driver.get(f"https://www.saucedemo.com/inventory.html"
                        f"?Username={shop_log}&password={shop_pass}")
        products = [value1, value2, value3]
        for product in products:
            search_prod = self.driver.find_element(
                By.XPATH, f'//div[text()="{product}"]/ancestor::'
                f'div[@class="inventory_item"]//button'
                )
            search_prod.click()
