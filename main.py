from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

  def setUp(self):
    self.browser = webdriver.Chrome()
    self.browser.implicitly_wait(5)

  def tearDown(self):
    self.browser.quit()

  def test_registration_1(self):
    link = "http://suninjuly.github.io/registration1.html"
    self.browser.get(link)

    input1 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group .form-control.first")
    input1.send_keys("Ivan")
    input2 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group .form-control.second")
    input2.send_keys("Petrov")
    input3 = self.browser.find_element(By.CSS_SELECTOR, "div.first_block div.form-group .form-control.third")
    input3.send_keys("malemal")

    button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

  def test_registration_2(self):
    link = "http://suninjuly.github.io/registration2.html"
    self.browser.get(link)

    input1 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.first")
    input1.send_keys("Ivan")
    input2 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.second")
    input2.send_keys("Petrov")
    input3 = self.browser.find_element(By.CSS_SELECTOR, ".first_block .form-control.third")
    input3.send_keys("malemal")

    button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

if __name__ == "__main__":
  unittest.main()
