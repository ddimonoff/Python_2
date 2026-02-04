import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages2.AutorizePage import Autorize
from pages2.ProductsPage import Products
from pages2.BasketPage import Basket
from pages2.PurchaseOrderPage import PurchaseOrder


@allure.title("Он-лайн магазин")
@allure.severity("blocker")
@allure.epic("Магазин")
@allure.feature("CREATE")
@allure.description("Тест проверяет корректность "
                    "создания заказа в он-лайн магазине")
def test_shop():
    brauser = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    autorize_page = Autorize(brauser)
    shop_log = "standard_user"
    shop_pass = "secret_sauce"
    autorize_page.log_name(shop_log, shop_pass)
    products_page = Products(brauser)
    prod1 = "Sauce Labs Backpack"
    prod2 = "Sauce Labs Bolt T-Shirt"
    prod3 = "Sauce Labs Onesie"
    products_page.prod_select(shop_log, shop_pass, prod1, prod2, prod3)
    basket_page = Basket(brauser)
    basket_page.basket_form(shop_log, shop_pass, prod1, prod2, prod3)
    purchase_order_page = PurchaseOrder(brauser)
    first_name = "Дмитрий"
    last_name = "Шмидт"
    post_index = 446201
    total_shop = "$58.29"
    purchase_order_page.post_form(
        shop_log, shop_pass, first_name, last_name, post_index, total_shop
    )

    brauser.quit()
