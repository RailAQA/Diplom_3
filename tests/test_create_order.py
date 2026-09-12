from pages.order_page import OrderPage
from pages.constructor_page import ConstructorPage

import allure

from tools.routes import AppRoute

class TestCreateOrder:
    @allure.title('при создании нового заказа счётчик «Выполнено за сегодня» увеличивается')
    def test_today_orders_counter(self, auth_driver):
        order_page = OrderPage(driver=auth_driver)
        order_page.visit(AppRoute.ORDER)
        current_value = order_page.get_current_count_today_orders()

        main_page = ConstructorPage(driver=auth_driver)
        main_page.visit(url=AppRoute.BASE)
        main_page.add_ingrindient_to_order()
        main_page.click_create_order_button()

        order_page.visit(AppRoute.ORDER)
        actual_value = order_page.get_current_count_today_orders()
        assert actual_value > current_value

    @allure.title('при создании нового заказа счётчик Выполнено за все время увеличивается')
    def test_all_days_orders_counter(self, auth_driver):
        order_page = OrderPage(driver=auth_driver)
        order_page.visit(AppRoute.ORDER)
        current_value = order_page.get_current_count_all_time_orders()

        main_page = ConstructorPage(driver=auth_driver)
        main_page.visit(url=AppRoute.BASE)
        main_page.add_ingrindient_to_order()
        main_page.click_create_order_button()

        order_page.visit(AppRoute.ORDER)
        actual_value = order_page.get_current_count_all_time_orders()
        assert actual_value > current_value
    
    @allure.title('после оформления заказа его номер появляется в разделе «В работе»')
    def test_new_order_number_in_work_list(self, auth_driver):
        main_page = ConstructorPage(auth_driver)
        main_page.add_ingrindient_to_order()
        main_page.click_create_order_button()
        order_number = main_page.get_order_id()
        main_page.visit(AppRoute.ORDER)

        order_page = OrderPage(auth_driver)
        order_number_in_list = order_page.get_user_order(order_number)
        order_in_progress = order_page.get_user_order_in_progress()
        assert order_number_in_list == order_in_progress