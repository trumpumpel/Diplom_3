from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from conftest import web_driver
import allure


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
