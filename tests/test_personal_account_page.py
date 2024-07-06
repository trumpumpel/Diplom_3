from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from conftest import web_driver
import allure
from data import URL, URL_ORDER_HISTORY, URL_LOG, URL_PROFILE
from pages.personal_account_page import PersonalAccountPage


@allure.title('Тестируем функционал личного кабинета')
class TestPersonalAccountPage:
    @allure.title('Тестируем переход по клику на Личный кабинет')
    def test_click_button_personal_account(self, web_driver):
        pa_page = PersonalAccountPage(web_driver)
        pa_page.navigate(URL)
        pa_page.button_personal_account_click()
        assert web_driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    @allure.title('Тестируем переход по клику на История заказов')
    def test_click_button_order_history(self, web_driver):
        pa_page = PersonalAccountPage(web_driver)
        pa_page.navigate(URL)
        pa_page.button_personal_account_click()
        pa_page.set_email()
        pa_page.set_pas()
        pa_page.enter_button_click()
        pa_page.button_personal_account_click()
        pa_page.order_history_button_click()
        assert web_driver.current_url == URL_ORDER_HISTORY

    @allure.title('Тестируем переход по клику на Выход')
    def test_click_button_exit(self, web_driver):
        pa_page = PersonalAccountPage(web_driver)
        pa_page.navigate(URL)
        pa_page.button_personal_account_click()
        pa_page.set_email()
        pa_page.set_pas()
        pa_page.enter_button_click()
        pa_page.button_personal_account_click()
        pa_page.exit_button_click()
        WebDriverWait(web_driver, 15).until(expected_conditions.url_changes(URL_PROFILE))
        assert web_driver.current_url == URL_LOG
