from data import COR_EMAIL, COR_PASSWORD
from pages.base_page import BasePage
from conftest import web_driver
from locators.main_functionality_page_locators import MainFunctionalityPageLocators
import allure


@allure.title('Проверяем основной функционал')
class MainFunctionalityPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def button_constructor_click(self):
        with  allure.step('Нажимаем поле Конструктор'):
            return self.click_element(MainFunctionalityPageLocators.CONSTRUCTOR, 100)

    def button_constructor_order_feed(self):
        with  allure.step('Нажимаем поле Лента заказов'):
            return self.click_element(MainFunctionalityPageLocators.ORDER_FEED, 100)

    def button_personal_account_click(self):
        with  allure.step('Нажимаем поле Личный кабинет'):
            return self.click_element(MainFunctionalityPageLocators.PERSONAL_ACCOUNT, 100)

    def click_test_ing(self):
        with  allure.step('Кликаем тестируемый ингридиент'):
            return self.click_element(MainFunctionalityPageLocators.TEST_ING, 100)

    def click_test_elem(self):
        with  allure.step('Кликаем тестируемый элемент'):
            return self.click_element(MainFunctionalityPageLocators.TEST_ELEM, 100)

    def click_cross_pop_up(self):
        with  allure.step('Кликаем крестик всплывающего окна'):
            return self.click_element(MainFunctionalityPageLocators.CROSS_POP_UP, 100)

    def set_email(self):
        with  allure.step('Вводим email'):
            return self.enter_text(MainFunctionalityPageLocators.SET_EMAIL_LOG, COR_EMAIL, 100)

    def set_pas(self):
        with  allure.step('Вводим пароль'):
            return self.enter_text(MainFunctionalityPageLocators.SET_PAS_LOG, COR_PASSWORD, 100)

    def enter_button_click(self):
        with  allure.step('Клик по кнопке Ввод'):
            return self.click_element(MainFunctionalityPageLocators.SUB_BTN_CLICK_LOG, 100)

    def place_order_btn_click(self):
        with  allure.step('Клик по кнопке Оформить заказ'):
            return self.click_element(MainFunctionalityPageLocators.PLACE_ORDER_BTN, 100)
