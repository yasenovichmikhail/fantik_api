import time
from tikitop.Tests.test_base import BaseTest
from tikitop.Pages.LoginPage import LoginPage
from config.config import *
from selenium import webdriver


class TestLogin(BaseTest):

    def test_login(self):
        page = LoginPage(self.driver)
        page.open_login_form()
        page.click_login_tab()
        page.set_email(EMAIL_TIKITOP)
        page.set_password(PASSWORD)
        page.click_login_btn()
        time.sleep(5)
