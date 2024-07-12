from locators.personal_account_page_locators import PersonalAccountPageLocators
from locators.main_functionality_page_locators import MainFunctionalityPageLocators
from pages.base_page import BasePage
import allure


class PersonalAccountPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке История заказов')
    def order_history_button_click(self):
        return self.click_element(MainFunctionalityPageLocators.BTN_ORDER_HISTORY, 100)

    @allure.step('Клик по кнопке Выйти')
    def exit_button_click(self):
        return self.click_element(PersonalAccountPageLocators.EXIT_BTN, 100)
