import allure

from locators.locators import ConstructorPageLocators, OrderPageLocators
from pages.base_page import BasePage


class ConstructorPage(BasePage):
    @allure.step('Переход на страницу Конструктор заказов')
    def click_constructor_button(self):
        self.click(locator=OrderPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Переход на страницу Лента заказов')
    def click_order_button(self):
        self.click(locator=ConstructorPageLocators.ORDERS_BUTTON)

    @allure.step('Клик на ингредиент')
    def click_on_ingredient(self):
        self.click(ConstructorPageLocators.INGREDIENT)

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_popup_is_visible(self):
        self.check_visible(locator=ConstructorPageLocators.INGREDIENT_POPUP)

    @allure.step('Закрытие попапа с деталями ингриндиента')
    def click_cross_popup_button(self):
        self.click(ConstructorPageLocators.CROSS_POPUP_BUTTON)

    @allure.step('Проверяем, что закрылся попап с деталями ингриндиента')
    def check_invisibility_ingredient_details(self):
        return self.check_not_visible(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP)

    @allure.step('Проверяем, что есть попап с деталями ингриндиента')
    def check_displayed_ingredient_details(self):
        self.check_visible(ConstructorPageLocators.INGREDIENT_DETAILS_POPUP)
    
    @allure.step('Получаем значение счетчика ингредиента')
    def get_count_value(self):
        return self.get_element_text(ConstructorPageLocators.INGREDIENT_COUNTER)
    
    @allure.step('Добавить ингриндиент в заказ')
    def add_ingrindient_to_order(self):
        self.drag_and_drop_on_element(ConstructorPageLocators.INGREDIENT, ConstructorPageLocators.ORDER_BASKET)

    @allure.step('Клик на кнопку сделать заказ')
    def click_create_order_button(self):
        element = self.get_locator(locator=ConstructorPageLocators.CREATE_ORDER_BUTTON)
        self.scroll_to_center(element)
        self.click_to(ConstructorPageLocators.CREATE_ORDER_BUTTON)

    @allure.step('Проверяем, что есть попап с номером заказа')
    def check_visible_popup_with_order_id(self):
        self.check_visible(ConstructorPageLocators.ORDER_IDENTIFICATE)

    @allure.step('Получить номер заказа')
    def get_order_id(self):
        self.check_visible(ConstructorPageLocators.ORDER_IDENTIFICATE)
        order_id = self.get_element_text(ConstructorPageLocators.ORDER_ID)
        while order_id == '9999':
            order_id = self.get_element_text(ConstructorPageLocators.ORDER_ID)
        return f"{order_id}"

    @allure.step('Закрыть попап с номером заказа')
    def click_close_modal_order(self):
        self.wait_element_will_clickable(locator=ConstructorPageLocators.CLOSE_MODAL_ORDER, timeout=15)
        self.click_to(locator=ConstructorPageLocators.CLOSE_MODAL_ORDER)
        self.check_not_visible(locator=ConstructorPageLocators.CLOSE_MODAL_ORDER)
