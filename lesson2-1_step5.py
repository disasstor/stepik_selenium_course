from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    input_value = browser.find_element(By.ID, 'input_value')

    input2 = browser.find_element(By.CLASS_NAME, 'form-control')
    input2.send_keys(calc(input_value.text))

    input3 = browser.find_element(By.ID, 'robotCheckbox')
    input3.click()

    input4 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    input4.click()

    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(30)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

