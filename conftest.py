from selenium import webdriver
import pytest

from pages.login_page import LoginPage

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=chrome_options)
        driver.maximize_window()
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=firefox_options)
        driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def auth_driver(driver):
    login_page = LoginPage(driver)
    login_page.visit("https://stellarburgers.education-services.ru/login")
    login_page.auth()
    return driver
    
