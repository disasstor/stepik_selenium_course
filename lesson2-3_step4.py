import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

# input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
# input1.send_keys("Ivan")
#
# input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
# input2.send_keys("Petrov")
#
# input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
# input3.send_keys("ivanpetrov@test.ee")
#
# file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
# file.send_keys(file_path)

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

