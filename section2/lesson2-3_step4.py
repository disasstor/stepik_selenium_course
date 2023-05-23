import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

# time.sleep(2)

input_value = browser.find_element(By.ID, 'input_value').text

answer = browser.find_element(By.ID, 'answer')
answer.send_keys(calc(input_value))

button = browser.find_element(By.TAG_NAME, "button")
button.click()


time.sleep(10)

