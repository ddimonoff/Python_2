from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def test_02():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver.maximize_window()
    driver.implicitly_wait(5)
    search_input = driver.find_element(By.CSS_SELECTOR, '#delay')
    delay_value = 45
    search_input.clear()
    search_input.send_keys(delay_value)

    search_but7 = driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='7']")
    search_but7.click()
    search_but_S = driver.find_element(By.XPATH, "//span[@class='operator btn btn-outline-success' and text()='+']")
    search_but_S.click()
    search_but8 = driver.find_element(By.XPATH, "//span[@class='btn btn-outline-primary' and text()='8']")
    search_but8.click()
    search_but_R = driver.find_element(By.XPATH, "//span[@class='btn btn-outline-warning' and text()='=']")
    search_but_R.click()
    delay_value = delay_value * 5
    driver.implicitly_wait(delay_value)
    result = driver.find_element(By.XPATH, "//div[@class='screen' and text()='15']").text

    assert result == "15"

    driver.quit()
