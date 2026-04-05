from pages.constructor_page import ConstructorPage
from tools.routes import AppRoute

import allure


class TestConstructorPage:
    @allure.title("Переход на страницу конструктор")
    def test_navigate_constructor_button(self, driver):
        main_page = ConstructorPage(driver=driver)
        main_page.visit(AppRoute.ORDER)
        main_page.click_constructor_button()
        main_page.check_current_url(url=AppRoute.BASE)

    @allure.title("Переход на страницу лента заказов")
    def test_navigate_order_button(self, driver):
        main_page = ConstructorPage(driver=driver)
        main_page.visit(url=AppRoute.BASE)
        main_page.click_order_button()
        main_page.check_current_url(url=AppRoute.ORDER)

    @allure.title('При нажатии на ингридиент всплывает окно с информаций')
    def test_popup_of_ingredient(self, driver):
        main_page = ConstructorPage(driver=driver)
        main_page.visit(url=AppRoute.BASE)
        main_page.click_on_ingredient()
        main_page.check_popup_is_visible()

    @allure.title('При нажатии в модальном окне с информацией об ингридиенте крестика , окно закрывается')
    def test_close_ingredient_details_window(self, driver):
        main_page = ConstructorPage(driver=driver)
        main_page.visit(url=AppRoute.BASE)
        main_page.click_on_ingredient()
        main_page.click_cross_popup_button()
        main_page.check_invisibility_ingredient_details()

    @allure.title('При добавлении ингридиента в заказ, счетчик заказа увеличивается')
    def test_ingredient_counter(self, driver):
        main_page = ConstructorPage(driver=driver)
        main_page.visit(url=AppRoute.BASE)
        start_counter_value = main_page.get_count_value()
        main_page.add_ingrindient_to_order()
        actual_value = main_page.get_count_value()
        assert actual_value > start_counter_value

   