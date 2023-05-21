from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))



try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    treasure_value = treasure.get_attribute("valuex")

    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(calc(treasure_value))

    input3 = browser.find_element(By.ID, 'robotCheckbox')
    input3.click()

    input4 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    input4.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
