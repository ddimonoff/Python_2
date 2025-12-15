from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)


def test_03():
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    search_input = driver.find_element(By.CSS_SELECTOR, '#user-name')
    search_input.send_keys("standard_user")

    search_input = driver.find_element(By.CSS_SELECTOR, '#password')
    search_input.send_keys("secret_sauce")

    search_button_log = driver.find_element(By.CSS_SELECTOR, '#login-button')
    search_button_log.click()

    search_button_1 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack')
    search_button_1.click()

    search_button_2 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt')
    search_button_2.click()

    search_button_3 = driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie')
    search_button_3.click()

    search_button_basket = driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')
    search_button_basket.click()

    search_button_next = driver.find_element(By.CSS_SELECTOR, '#checkout')
    search_button_next.click()

    search_input = driver.find_element(By.CSS_SELECTOR, '#first-name')
    search_input.send_keys("Дмитрий")

    search_input = driver.find_element(By.CSS_SELECTOR, '#last-name')
    search_input.send_keys("Шмидт")

    search_input = driver.find_element(By.CSS_SELECTOR, '#postal-code')
    search_input.send_keys(446201)

    search_button = driver.find_element(By.CSS_SELECTOR, '#continue')
    search_button.click()

    result = driver.find_element(By.XPATH, "//div[@class='summary_total_label' and text()='58.29']").text
    result = result[7:]
    assert result == "$58.29"

    driver.quit()
