from data import TestUrlData
from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.main_functionality_page_locators import MainFunctionalityPageLocators
from pages.base_page import BasePage
import allure


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке Личный кабинет')
    def button_personal_account_click(self):
        return self.click_element(MainFunctionalityPageLocators.PERSONAL_ACCOUNT, 100)

    @allure.step('Вводим email')
    def set_email(self):
        return self.enter_text(MainFunctionalityPageLocators.SET_EMAIL_LOG, TestUrlData.COR_EMAIL, 100)

    @allure.step('Вводим пароль')
    def set_pas(self):
        return self.enter_text(MainFunctionalityPageLocators.SET_PAS_LOG, TestUrlData.COR_PASSWORD, 100)

    @allure.step('Клик по кнопке Ввод')
    def enter_button_click(self):
        return self.click_element(MainFunctionalityPageLocators.SUB_BTN_CLICK_LOG, 100)

    @allure.step('Клик по кнопке Лента заказов')
    def order_history_button_click(self):
        return self.click_element(MainFunctionalityPageLocators.BTN_ORDER_HISTORY, 100)

    @allure.step('Клик по кнопке Выйти')
    def exit_button_click(self):
        return self.click_element(PersonalAccountPageLocators.EXIT_BTN, 100)
