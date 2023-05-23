import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'lesson2-2_step8.txt')


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)

input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]')
input1.send_keys("Ivan")

input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]')
input2.send_keys("Petrov")

input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]')
input3.send_keys("ivanpetrov@test.ee")

file = browser.find_element(By.CSS_SELECTOR, "[name='file']")
file.send_keys(file_path)

button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)
