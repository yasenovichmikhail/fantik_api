import time

from tikitop.Pages.BasePage import BasePage
from tikitop.Pages.locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

    def open_login_form(self):
        self.click(locator=LoginPageLocators.SIGNUP_BUTTON)

    def click_sign_up_tab(self):
        self.click(locator=LoginPageLocators.SIGNUP_TAB)

    def click_login_tab(self):
        self.click(locator=LoginPageLocators.LOGIN_TAB)

    def set_email(self, email):
        self.send_keys(locator=LoginPageLocators.INPUT_EMAIL,
                       text=email)

    def set_password(self, password):
        self.send_keys(locator=LoginPageLocators.INPUT_PASSWORD,
                       text=password)

    def click_login_btn(self):
        self.click(LoginPageLocators.LOGIN_BUTTON)



