from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Lesson7.pages1.CalculatorPage import CalculatorPage


def test_calculator():
    brauser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    calculator_page = CalculatorPage(brauser)
    delay = 45      # время задержки
    calculator_page.waiting_time(delay)
    calculator_page.number_button('7')      # первое значение
    calculator_page.arithmetic_operation('+')     # арифметическое действие
    calculator_page.number_button('8')      # второе значение
    calculator_page.equals('=')         # знак равно
    to_be = "15"         # ожидаемый результат
    calculator_page.pauses_time(delay, to_be)
    as_is = calculator_page.get_result()
    calculator_page.quit()
    assert as_is == to_be
