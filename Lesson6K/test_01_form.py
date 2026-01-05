from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.by import By


edge_driver_path = r"C:\Users\RWM20\OneDrive\Рабочий стол\Python_S\Python_2\edgedriver_win64\msedgedriver.exe"
driver = webdriver.Edge(service=EdgeService(edge_driver_path))


def test_01():
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.maximize_window()
    driver.implicitly_wait(5)
    name_form = ['first-name', 'last-name', 'address', 'zip-code', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
    user = ['Иван', 'Петров', 'Ленина, 55-3', '', 'Москва', 'Россия', 'test@skypro.com', '+7985899998787', 'QA', 'SkyPro']
    for i in range(len(name_form)):
        element = driver.find_element(By.NAME, name_form[i])
        element.send_keys(user[i])

    button_submit = driver.find_element(By.CSS_SELECTOR, 'button.btn')
    button_submit.click()

    red_color = driver.find_element(By.CSS_SELECTOR, 'div#zip-code')
    background_color = red_color.value_of_css_property("background-color")
    assert background_color == 'rgba(248, 215, 218, 1)'

    other_fields_id = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']

    for id in other_fields_id:
        green_color = driver.find_element(By.ID, id)
        background_color = green_color.value_of_css_property("background-color")
        assert background_color == 'rgba(209, 231, 221, 1)'

    driver.quit()
