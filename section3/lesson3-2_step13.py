import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestAuth(unittest.TestCase):
    def test_log_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.first_class > input')
        last_name = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.second_class > input')
        email = browser.find_element(By.CSS_SELECTOR, 'div.first_block > div.form-group.third_class > input')

        name.send_keys("Ivan")
        last_name.send_keys("Petrov")
        email.send_keys("ivanpetrov@test.ee")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(5)
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_text, "Welcome text was not appeared or was changed")
        time.sleep(3)
        browser.quit()

    def test_log_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        name = browser.find_element(By.CSS_SELECTOR, "input:required.first")
        last_name = browser.find_element(By.CLASS_NAME, "second:required")
        email = browser.find_element(By.CLASS_NAME, "third:required")

        name.send_keys("Madiyar")
        last_name.send_keys("Uchiha")
        email.send_keys("madi@gmail.com")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        time.sleep(5)
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        expected_text = "Congratulations! You have successfully registered!"

        self.assertEqual(welcome_text, expected_text, "Welcome text was not appeared or was changed")
        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()