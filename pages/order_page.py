from locators.locators import OrderPageLocators
from pages.base_page import BasePage

import allure


class OrderPage(BasePage):
    @allure.step('Получить текущее количество заказов за все время')
    def get_current_count_all_time_orders(self):
        element = self.get_locator(locator=OrderPageLocators.CURRENT_COUNT_ORDERS_ALL)
        self.scroll_to_center(element)
        return int(self.get_element_text(locator=OrderPageLocators.CURRENT_COUNT_ORDERS_ALL))
    
    @allure.step('Получить текущее количество заказов за сегодня')
    def get_current_count_today_orders(self):
        element = self.get_locator(locator=OrderPageLocators.CURRENT_COUNT_ORDERS_TODAT)
        self.scroll_to_center(element)
        return int(self.get_element_text(locator=OrderPageLocators.CURRENT_COUNT_ORDERS_TODAT))
    
    @allure.step('Получаем номер заказа в работе')
    def get_user_order_in_progress(self):
        return self.get_element_text(OrderPageLocators.NUMBER_IN_PROGRESS)
    
    @allure.step('Получаем номер заказа')
    def get_user_order(self, orders_numbers):
        order_refactor = f'0{orders_numbers}'
        self.wait_for_text_to_be_present_in_element(OrderPageLocators.NUMBER_IN_PROGRESS, 15, order_refactor)
        return order_refactor