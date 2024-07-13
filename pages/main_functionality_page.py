from pages.base_page import BasePage
from conftest import web_driver
from locators.main_functionality_page_locators import MainFunctionalityPageLocators
import allure


class MainFunctionalityPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step('Клик по Конструктор')
    def button_constructor_click(self):
        return self.click_element(MainFunctionalityPageLocators.CONSTRUCTOR, 100)

    @allure.step('Поиск закрытого класса всплывающего окна')
    def set_cl_pop_up(self):
        return self.find_element(MainFunctionalityPageLocators.CL_POP_UP, 100)

    @allure.step('Поиск элемента счётчика заказов')
    def set_counter(self):
        return self.find_element(MainFunctionalityPageLocators.COUNTER, 100)

    @allure.step('Получение подтверждения изготовления заказа')
    def set_order_in_progress(self):
        return self.find_element(MainFunctionalityPageLocators.O_I_P, 100)

    @allure.step('Клик по Войти в аккаунт')
    def button_enter_pers_acc_click(self):
        return self.click_element(MainFunctionalityPageLocators.BTN_ENT_PA, 100)
