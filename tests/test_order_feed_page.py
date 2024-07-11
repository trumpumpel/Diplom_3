from selenium.webdriver.common.by import By
from conftest import web_driver
from selenium.webdriver.support import expected_conditions as EC
import allure
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
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
        number = of_page_text.text
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page.click_element((By.XPATH, ".//*[contains(text(),'" + number + "')]"), 10)
        of_page = web_driver.find_element(By.XPATH,
                                          "//div[contains(@class, 'Modal_modal__container__Wo2l_')]")
        of_page_div_class = of_page.get_attribute("class")
        assert of_page_div_class == "Modal_modal__container__Wo2l_"

    @allure.title('Тестируем появление заказа из истории заказов в Ленте заказов')
    def test_orders_from_history_in_order_feed_page(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.button_personal_account_click()
        of_page.order_history_button_click()
        of_page_text = web_driver.find_element(By.XPATH, "//p[@class='text text_type_digits-default']")
        number = of_page_text.text
        of_page.button_constructor_order_feed()
        assert EC.presence_of_element_located((By.XPATH, ".//*[contains(text(),'" + number + "')]")) is not True

    @allure.title('Тестируем увелечение значения счётчика за всё время при создании нового заказа')
    def test_all_counter_when_creating_an_order(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_constructor_order_feed()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
        number = of_page_text.text
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
        num = of_page_text.text
        assert f"{num}" > f"{number}"

    @allure.title('Тестируем увелечение значения счётчика Выполнено за сегодня при создании нового заказа')
    def test_day_counter_when_creating_an_order(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_constructor_order_feed()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
        number = of_page_text.text
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
        num = of_page_text.text
        assert f"{num}" > f"{number}"

    @allure.title('Тестируем появление номера закза в разделе В работе после его создания')
    def test_availability_number_in_section_in_progress(self, web_driver):
        of_page = OrderFeedPage(web_driver)
        of_page.button_personal_account_click()
        of_page.set_email()
        of_page.set_pas()
        of_page.enter_button_click()
        of_page.adding_ingredients_to_order(web_driver)
        of_page.place_order_btn_click()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
        number = of_page_text.text
        of_page.click_cross_pop_up()
        of_page.button_constructor_order_feed()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//ul[contains(@class, 'OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi')]")
        num = of_page_text.text
        assert f"{num}" == f"0{number}"
