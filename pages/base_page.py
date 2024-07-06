from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import web_driver
import allure


class BasePage:
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    def navigate(self, url: str):
        with allure.step("Открываем страницу"):
            self.web_driver.get(url)

    def find_element(self, locator: tuple, timeout: 15) -> object:
        with allure.step("Ищем элемент на странице"):
            return WebDriverWait(self.web_driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator: tuple, timeout: 15):
        with allure.step("Ищем и кликаем по найденому элементу"):
            element = self.find_element(locator, timeout)
            element.click()

    def click_el(self, element):
        with allure.step("Кликаем по элементу"):
            self.scroll(element)
            element.click()

    def enter_text(self, locator: tuple, text: str, timeout: 15):
        with allure.step("Вводим текст"):
            element = self.find_element(locator, timeout)
            element.click()
            element.send_keys(text)
