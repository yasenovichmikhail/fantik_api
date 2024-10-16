import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def init_driver(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield web_driver
    web_driver.quit()
