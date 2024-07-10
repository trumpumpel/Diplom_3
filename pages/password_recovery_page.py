from data import TestUrlData
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from conftest import web_driver
import allure


@allure.title('Проверяем функционал восстановления пароля')
class PasswordRecoveryPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step('Клик по кнопке Восстановить пароль')
    def btn_recover_password_click(self):
        return self.click_element(PasswordRecoveryPageLocators.BTN_RECOVER_PASSWORD, 100)

    @allure.step('Вводим email')
    def set_email(self):
        return self.enter_text(PasswordRecoveryPageLocators.SET_EMAIL_LOG, TestUrlData.COR_EMAIL, 100)

    @allure.step('Клик по кнопке Восстановить')
    def btn_recover_click(self):
        return self.click_element(PasswordRecoveryPageLocators.BTN_RECOVER, 100)
