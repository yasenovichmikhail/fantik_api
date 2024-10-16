import time
from selenium.common import NoSuchElementException, TimeoutException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()
        self.driver.get('https://tikitop.io')

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
        return element

    def clear_data(self, field, len_value):
        for i in range(len_value):
            field.send_keys("\b")

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, locator, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            return True
        return False

    def get_title(self):
        return self.driver.title

    def go_back(self):
        self.driver.back()

    def refresh(self):
        self.driver.refresh()

    def screenshot(self, file_name='screenshot.png'):
        self.driver.save_screenshot(file_name)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_iframe(self, iframe):
        self.driver.switch_to.frame(iframe)

    def switch_out_iframe(self):
        self.driver.switch_to.default_content()

    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)


