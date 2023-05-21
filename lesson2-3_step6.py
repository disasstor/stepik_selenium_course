import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/redirect_accept.html"
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

input_value = browser.find_element(By.ID, "input_value").text

input2 = browser.find_element(By.ID, 'answer')
input2.send_keys(calc(input_value))

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)
