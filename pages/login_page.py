from data.data import AuthData
from pages.base_page import BasePage
import allure

from locators.locators import LoginPageLocators, ConstructorPageLocators


class LoginPage(BasePage):
    @allure.step('Заполнить поле с почтой')
    def fill_email(self):
        self.fill(locator=LoginPageLocators.EMAIL_INPUT, text=AuthData.LOGIN)

    @allure.step('Заполнить поле с паролем')
    def fill_password(self):
        self.fill(locator=LoginPageLocators.PASSWORD_INPUT, text=AuthData.PASSWORD)

    @allure.step('Клик на кнопку логина')
    def click_login_button(self):
        self.click(locator=LoginPageLocators.LOGIN_BUTTON)
        self.wait_element_will_visible(locator=ConstructorPageLocators.INGREDIENT, timeout=10)

    @allure.step('Авторизация')
    def auth(self):
        self.fill_email()
        self.fill_password()
        self.click_login_button()