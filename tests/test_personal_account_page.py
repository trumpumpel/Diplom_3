from conftest import web_driver
import allure
from data.url_data import TestUrlData
from pages.personal_account_page import PersonalAccountPage


class TestPersonalAccountPage:
    @allure.title('Тестируем переход по клику на Личный кабинет')
    def test_click_button_personal_account(self, web_driver):
        pa_page = PersonalAccountPage(web_driver)
        pa_page.navigate(TestUrlData.URL)
        pa_page.button_personal_account_click()
        r_url = pa_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_LOG}'

    @allure.title('Тестируем переход по клику на История заказов')
    def test_click_button_order_history(self, web_driver):
        pa_page = PersonalAccountPage(web_driver)
        pa_page.navigate(TestUrlData.URL)
        pa_page.button_personal_account_click()
        pa_page.set_email()
        pa_page.set_pas()
        pa_page.enter_button_click()
        pa_page.button_personal_account_click()
        pa_page.order_history_button_click()
        r_url = pa_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_ORDER_HISTORY}'

    @allure.title('Тестируем переход по клику на Выход')
    def test_click_button_exit(self, web_driver):
        pa_page = PersonalAccountPage(web_driver)
        pa_page.navigate(TestUrlData.URL)
        pa_page.button_personal_account_click()
        pa_page.set_email()
        pa_page.set_pas()
        pa_page.enter_button_click()
        pa_page.button_personal_account_click()
        pa_page.exit_button_click()
        r_url = pa_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_LOG}'
