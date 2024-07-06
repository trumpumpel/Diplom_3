from data import COR_EMAIL
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from conftest import web_driver
import allure


@allure.title('Проверяем функционал восстановления пароля')
class PasswordRecoveryPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    def btn_recover_password_click(self):
        with  allure.step('Клик по кнопке Восстановить пароль'):
            return self.click_element(PasswordRecoveryPageLocators.BTN_RECOVER_PASSWORD, 100)

    def set_email(self):
        with  allure.step('Вводим email'):
            return self.enter_text(PasswordRecoveryPageLocators.SET_EMAIL_LOG, COR_EMAIL, 100)

    def btn_recover_click(self):
        with  allure.step('Клик по кнопке Восстановить'):
            return self.click_element(PasswordRecoveryPageLocators.BTN_RECOVER, 100)
