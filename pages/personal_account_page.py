from data import COR_EMAIL, COR_PASSWORD
from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage
import allure


@allure.title('Проверяем функционал личного кабинета')
class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def button_personal_account_click(self):
        with  allure.step('Клик по кнопке Личный кабинет'):
            return self.click_element(PersonalAccountPageLocators.PERSONAL_ACCOUNT, 100)

    def set_email(self):
        with  allure.step('Вводим email'):
            return self.enter_text(PersonalAccountPageLocators.SET_EMAIL_LOG, COR_EMAIL, 100)

    def set_pas(self):
        with  allure.step('Вводим пароль'):
            return self.enter_text(PersonalAccountPageLocators.SET_PAS_LOG, COR_PASSWORD, 100)

    def enter_button_click(self):
        with  allure.step('Клик по кнопке Ввод'):
            return self.click_element(PersonalAccountPageLocators.SUB_BTN_CLICK_LOG, 100)

    def order_history_button_click(self):
        with  allure.step('Клик по кнопке Лента заказов'):
            return self.click_element(PersonalAccountPageLocators.BTN_ORDER_HISTORY, 100)

    def exit_button_click(self):
        with  allure.step('Клик по кнопке Выйти'):
            return self.click_element(PersonalAccountPageLocators.EXIT_BTN, 100)
