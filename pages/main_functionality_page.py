from data import TestUrlData
from pages.base_page import BasePage
from conftest import web_driver
from locators.main_functionality_page_locators import MainFunctionalityPageLocators
import allure


class MainFunctionalityPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step('Нажимаем поле Конструктор')
    def button_constructor_click(self):
        return self.click_element(MainFunctionalityPageLocators.CONSTRUCTOR, 100)

    @allure.step('Нажимаем поле Лента заказов')
    def button_constructor_order_feed(self):
        return self.click_element(MainFunctionalityPageLocators.ORDER_FEED, 100)

    @allure.step('Нажимаем поле Личный кабинет')
    def button_personal_account_click(self):
        return self.click_element(MainFunctionalityPageLocators.PERSONAL_ACCOUNT, 100)

    @allure.step('Кликаем тестируемый ингридиент')
    def click_test_ing(self):
        return self.click_element(MainFunctionalityPageLocators.TEST_ING, 100)

    @allure.step('Кликаем тестируемый элемент')
    def click_test_elem(self):
        return self.click_element(MainFunctionalityPageLocators.TEST_ELEM, 100)

    @allure.step('Кликаем крестик всплывающего окна')
    def click_cross_pop_up(self):
        return self.click_element(MainFunctionalityPageLocators.CROSS_POP_UP, 100)

    @allure.step('Вводим email')
    def set_email(self):
        return self.enter_text(MainFunctionalityPageLocators.SET_EMAIL_LOG, TestUrlData.COR_EMAIL, 100)

    @allure.step('Вводим пароль')
    def set_pas(self):
        return self.enter_text(MainFunctionalityPageLocators.SET_PAS_LOG, TestUrlData.COR_PASSWORD, 100)

    @allure.step('Клик по кнопке Ввод')
    def enter_button_click(self):
        return self.click_element(MainFunctionalityPageLocators.SUB_BTN_CLICK_LOG, 100)

    @allure.step('Клик по кнопке Оформить заказ')
    def place_order_btn_click(self):
        return self.click_element(MainFunctionalityPageLocators.PLACE_ORDER_BTN, 100)
