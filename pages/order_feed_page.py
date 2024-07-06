from data import COR_EMAIL, COR_PASSWORD
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from conftest import web_driver
import allure


@allure.title('Проверяем раздел Лента заказов')
class OrderFeedPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def button_constructor_order_feed(self):
        with  allure.step('Нажимаем поле Лента заказов'):
            return self.click_element(OrderFeedPageLocators.ORDER_FEED, 100)

    def order_test_el_click(self):
        with  allure.step('Нажимаем на тестовый элемент'):
            return self.click_element(OrderFeedPageLocators.ORDER_TEST_EL, 100)

    def button_personal_account_click(self):
        with  allure.step('Нажимаем на поле Личный Кабинет'):
            return self.click_element(OrderFeedPageLocators.PERSONAL_ACCOUNT, 100)

    def set_email(self):
        with  allure.step('Вводим email'):
            return self.enter_text(OrderFeedPageLocators.SET_EMAIL_LOG, COR_EMAIL, 100)

    def set_pas(self):
        with  allure.step('Вводим пароль'):
            return self.enter_text(OrderFeedPageLocators.SET_PAS_LOG, COR_PASSWORD, 100)

    def enter_button_click(self):
        with  allure.step('Клик по кнопке Ввод'):
            return self.click_element(OrderFeedPageLocators.SUB_BTN_CLICK_LOG, 100)

    def order_history_button_click(self):
        with  allure.step('Клик по кнопке История заказов'):
            return self.click_element(OrderFeedPageLocators.ORDER_HISTORY_BUTTON, 100)

    def place_order_btn_click(self):
        with  allure.step('Клик по кнопке Оформить заказ'):
            return self.click_element(OrderFeedPageLocators.PLACE_ORDER_BTN, 100)

    def click_cross_pop_up(self):
        with  allure.step('Кликаем крестик всплывающего окна'):
            return self.click_element(OrderFeedPageLocators.CROSS_POP_UP, 100)
