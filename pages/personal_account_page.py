from data import TestUrlData
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
import allure


@allure.title('Проверяем функционал личного кабинета')
class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке Личный кабинет')
    def button_personal_account_click(self):
        return self.click_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT, 100)

    @allure.step('Вводим email')
    def set_email(self):
        return self.enter_text(PersonalAccountPageLocators.SET_EMAIL_LOG, TestUrlData.COR_EMAIL, 100)

    @allure.step('Вводим пароль')
    def set_pas(self):
        return self.enter_text(PersonalAccountPageLocators.SET_PAS_LOG, TestUrlData.COR_PASSWORD, 100)

    @allure.step('Клик по кнопке Ввод')
    def enter_button_click(self):
        return self.click_element(PersonalAccountPageLocators.SUB_BTN_CLICK_LOG, 100)

    @allure.step('Клик по кнопке Лента заказов')
    def order_history_button_click(self):
        return self.click_element(PersonalAccountPageLocators.BTN_ORDER_HISTORY, 100)

    @allure.step('Клик по кнопке Выйти')
    def exit_button_click(self):
        return self.click_element(PersonalAccountPageLocators.EXIT_BTN, 100)
