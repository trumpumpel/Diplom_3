from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import web_driver
import allure

from data import TestUrlData
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    @allure.step("Открываем страницу")
    def navigate(self, url: str):
        self.web_driver.get(url)

    @allure.step("Ищем элемент на странице")
    def find_element(self, locator: tuple, timeout: 15) -> object:
        return WebDriverWait(self.web_driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.step("Ищем и кликаем по найденому элементу")
    def click_element(self, locator: tuple, timeout: 15):
        element = self.find_element(locator, timeout)
        element.click()

    @allure.step("Вводим текст")
    def enter_text(self, locator: tuple, text: str, timeout: 15):
        element = self.find_element(locator, timeout)
        element.click()
        element.send_keys(text)

    @allure.step("Добавляю ингридиенты в заказ")
    def adding_ingredients_to_order(self, web_driver):
        WebDriverWait(web_driver, 100).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR,
                ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")))
        INGRID = web_driver.find_element(
            By.CSS_SELECTOR,
            ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")
        TEFKI = web_driver.find_element(By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
        ActionChains(web_driver).move_to_element(INGRID).move_to_element(TEFKI).drag_and_drop(INGRID, TEFKI).perform()

    @allure.step('Получаю текущий урл')
    def count_url(self, web_driver):
        return web_driver.current_url

    @allure.step('Клик по заказанному ингридиенту в Ленте заказов')
    def click_on_ingred_in_order_feed(self):
        element = self.find_element(BasePageLocators.ELEM,
                                    10)
        number = element.text
        self.click_element(BasePageLocators.CROSS_POP_UP, 100)
        self.click_element(BasePageLocators.ORDER_FEED, 100)
        return self.click_element((By.XPATH, ".//*[contains(text(),'" + number + "')]"), 100)

    @allure.step('Клик по ингридиенту в Ленте заказов')
    def click_ing_ord_feed(self):
        self.click_element(BasePageLocators.CL_ING, 100)
        return self.find_element(BasePageLocators.ACT_POP_UP, 100)

    @allure.step('Клик по Лента заказов')
    def button_constructor_order_feed(self):
        return self.click_element(BasePageLocators.ORDER_FEED, 100)

    @allure.step('Нажимаем поле Личный кабинет')
    def button_personal_account_click(self):
        return self.click_element(BasePageLocators.PERSONAL_ACCOUNT, 100)

    @allure.step('Вводим email')
    def set_email(self):
        return self.enter_text(BasePageLocators.SET_EMAIL_LOG, TestUrlData.COR_EMAIL, 100)

    @allure.step('Вводим пароль')
    def set_pas(self):
        return self.enter_text(BasePageLocators.SET_PAS_LOG, TestUrlData.COR_PASSWORD, 100)

    @allure.step('Клик по кнопке Ввод')
    def enter_button_click(self):
        return self.click_element(BasePageLocators.SUB_BTN_CLICK_LOG, 100)

    @allure.step('Клик по кнопке Оформить заказ')
    def place_order_btn_click(self):
        return self.click_element(BasePageLocators.PLACE_ORDER_BTN, 100)
