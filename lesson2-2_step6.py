import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

input_value = browser.find_element(By.ID, "input_value").text

input2 = browser.find_element(By.ID, 'answer')
browser.execute_script("return arguments[0].scrollIntoView(true);", input2)
input2.send_keys(calc(input_value))

input3 = browser.find_element(By.ID, 'robotCheckbox')
browser.execute_script("return arguments[0].scrollIntoView(true);", input3)
input3.click()

input4 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
browser.execute_script("return arguments[0].scrollIntoView(true);", input4)
input4.click()

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
