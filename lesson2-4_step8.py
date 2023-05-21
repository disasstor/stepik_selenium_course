import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

button = browser.find_element(By.TAG_NAME, "button")
button.click()

input_value = browser.find_element(By.ID, 'input_value').text

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(calc(input_value))

button = browser.find_element(By.CSS_SELECTOR, '[id="solve"]')
button.click()

time.sleep(10)

# assert "successful" in message.text