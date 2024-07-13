from conftest import web_driver
import allure
from data.auth_data import TestAuthData
from pages.order_feed_page import OrderFeedPage


class TestOrderFeedPage:

    @allure.title('Тестируем появление всплывающего окна с деталями после клика на заказ')
    def test_click_order_pop_up_window_will_open(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page.click_on_ingrid_in_order_feed()
        elem = of_page.set_pop_up_with_det()
        of_page_div_class = elem.get_attribute("class")
        assert of_page_div_class == TestAuthData.POP_UP_DET

    @allure.title('Тестируем появление заказа из истории заказов в Ленте заказов')
    @allure.title('Тестируем появление заказа после создания в Ленте заказов')
    def test_orders_from_history_in_order_feed_page(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page_text = of_page.find_number_oder_pop_up()
        number = of_page_text.text
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = of_page.find_number_oder()
        num = of_page_text.text
        assert f"{num}" == f"#0{number}"

    @allure.title('Тестируем появление заказа из истории заказов в Ленте заказов')
    @allure.title('Тестируем появление заказа после создания в Истории заказов')
    def test_orders_from_history_in_order_feed_page(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page_text = of_page.find_number_oder_pop_up()
        number = of_page_text.text
        of_page.click_cross_pop_up()
        of_page.button_personal_account_click()
        of_page.order_history_button_click()
        of_page_text = of_page.find_number_oder_in_hst_ord()
        num = of_page_text.text
        assert f"{number}" in f"{num}"


    @allure.title('Тестируем увелечение значения счётчика за всё время при создании нового заказа')
    def test_all_counter_when_creating_an_order(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_constructor_order_feed()
        of_page_text = of_page.set_counter_op()
        number = of_page_text.text
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = of_page.set_counter_op()
        num = of_page_text.text
        assert f"{num}" > f"{number}"

    @allure.title('Тестируем увелечение значения счётчика Выполнено за сегодня при создании нового заказа')
    def test_day_counter_when_creating_an_order(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_constructor_order_feed()
        of_page_text = of_page.set_counter_op()
        number = of_page_text.text
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = of_page.set_counter_op()
        num = of_page_text.text
        assert f"{num}" > f"{number}"

    @allure.title('Тестируем появление номера закaза в разделе В работе после его создания')
    def test_availability_number_in_section_in_progress(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page_text = of_page.find_number_oder_pop_up()
        number = of_page_text.text
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = of_page.find_number_oder_in_prog()
        num = of_page_text.text
        assert f"{num}" == f"0{number}"
