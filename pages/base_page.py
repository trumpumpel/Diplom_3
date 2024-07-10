from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
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

    @allure.step("Добавляю ингридиенты в заказ")
    def adding_ingredients_to_order(self, web_driver):
        WebDriverWait(web_driver, 100).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")))
        INGRID = web_driver.find_element(By.CSS_SELECTOR,
                                         ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")
        TEFKI = web_driver.find_element(By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
        ActionChains(web_driver).move_to_element(INGRID).move_to_element(TEFKI).drag_and_drop(INGRID, TEFKI).perform()
