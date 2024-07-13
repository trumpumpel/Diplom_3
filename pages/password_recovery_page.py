from locators.base_page_locators import BasePageLocators
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage
from conftest import web_driver
import allure


class PasswordRecoveryPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step('Клик по кнопке Восстановить пароль')
    def btn_recover_password_click(self):
        return self.click_element(BasePageLocators.BTN_RECOVER_PASSWORD, 100)

    @allure.step('Клик по кнопке Восстановить')
    def btn_recover_click(self):
        return self.click_element(PasswordRecoveryPageLocators.BTN_RECOVER, 100)

    @allure.step('Поиск элемента поля Пароль')
    def set_pas_act(self):
        return self.find_element(PasswordRecoveryPageLocators.PAS_ACT, 100)

    @allure.step('Клик по полю Пароль')
    def click_pas(self):
        return self.click_element(PasswordRecoveryPageLocators.PAS, 100)
