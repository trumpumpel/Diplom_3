from locators.main_functionality_page_locators import MainFunctionalityPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from conftest import web_driver
import allure


class OrderFeedPage(BasePage):

    def __init__(self, web_driver):
        super().__init__(web_driver)

    @allure.step('Клик по кнопке История заказов')
    def order_history_button_click(self):
        return self.click_element(MainFunctionalityPageLocators.BTN_ORDER_HISTORY, 100)

    @allure.step('Кликаем крестик всплывающего окна')
    def click_cross_pop_up(self):
        return self.click_element(BasePageLocators.CROSS_POP_UP, 100)

    @allure.step('Поиск всплывающего окна с деталями заказа')
    def set_pop_up_with_det(self):
        return self.find_element(OrderFeedPageLocators.P_P_O, 100)

    @allure.step('Поиск номера заказа в ленте заказов')
    def find_number_oder(self):
        return self.find_element(OrderFeedPageLocators.NUM_O, 100)

    @allure.step('Поиск элемента счётчика заказов')
    def set_counter_op(self):
        return self.find_element(OrderFeedPageLocators.EL_COUNTER, 100)

    @allure.step('Получение номера заказа из всплывающего окна')
    def find_number_oder_pop_up(self):
        return self.find_element(OrderFeedPageLocators.P_O_NUM,
                                 100)

    @allure.step('Поиск номера заказа в разделе В работе')
    def find_number_oder_in_prog(self):
        return self.find_element(OrderFeedPageLocators.NUM_I_PROG,
                                 100)

    @allure.step('Поиск номера заказа в Истории заказов')
    def find_number_oder_in_hst_ord(self):
        return self.find_element(OrderFeedPageLocators.H_OR,
                                 100)
