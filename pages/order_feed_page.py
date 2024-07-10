from data import TestUrlData
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage
from conftest import web_driver
import allure


class OrderFeedPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step('Нажимаем поле Лента заказов')
    def button_constructor_order_feed(self):
        return self.click_element(OrderFeedPageLocators.ORDER_FEED, 100)

    @allure.step('Нажимаем на тестовый элемент')
    def order_test_el_click(self):
        return self.click_element(OrderFeedPageLocators.ORDER_TEST_EL, 100)

    @allure.step('Нажимаем на поле Личный Кабинет')
    def button_personal_account_click(self):
        return self.click_element(OrderFeedPageLocators.PERSONAL_ACCOUNT, 100)

    @allure.step('Вводим email')
    def set_email(self):
        return self.enter_text(OrderFeedPageLocators.SET_EMAIL_LOG, TestUrlData.COR_EMAIL, 100)

    @allure.step('Вводим пароль')
    def set_pas(self):
        return self.enter_text(OrderFeedPageLocators.SET_PAS_LOG, TestUrlData.COR_PASSWORD, 100)

    @allure.step('Клик по кнопке Ввод')
    def enter_button_click(self):
        return self.click_element(OrderFeedPageLocators.SUB_BTN_CLICK_LOG, 100)

    @allure.step('Клик по кнопке История заказов')
    def order_history_button_click(self):
        return self.click_element(OrderFeedPageLocators.ORDER_HISTORY_BUTTON, 100)

    @allure.step('Клик по кнопке Оформить заказ')
    def place_order_btn_click(self):
        return self.click_element(OrderFeedPageLocators.PLACE_ORDER_BTN, 100)

    @allure.step('Кликаем крестик всплывающего окна')
    def click_cross_pop_up(self):
        return self.click_element(OrderFeedPageLocators.CROSS_POP_UP, 100)
