from conftest import web_driver
import allure

from data.auth_data import TestAuthData
from data.url_data import TestUrlData
from locators.password_recovery_page_locators import PasswordRecoveryPageLocators
from pages.password_recovery_page import PasswordRecoveryPage


class TestPasswordRecoveryPage:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_click_button_password_recovery(self, web_driver):
        pr_page = PasswordRecoveryPage(web_driver)
        pr_page.navigate(f'{TestUrlData.URL}{TestUrlData.URL_LOG}')
        pr_page.btn_recover_password_click()
        r_url = pr_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_FORGOT_PASSWORD}'

    @allure.title('Проверяем ввод почты и клик по кнопке Восстановить')
    def test_set_email_click_button_recovery(self, web_driver):
        pr_page = PasswordRecoveryPage(web_driver)
        pr_page.navigate(f'{TestUrlData.URL}{TestUrlData.URL_LOG}')
        pr_page.btn_recover_password_click()
        pr_page.set_email()
        pr_page.btn_recover_click()
        r_url = pr_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_FORGOT_PASSWORD}'

    @allure.title('Проверяем клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_button_show_hide_password(self, web_driver):
        pr_page = PasswordRecoveryPage(web_driver)
        pr_page.navigate(f'{TestUrlData.URL}{TestUrlData.URL_LOG}')
        pr_page.btn_recover_password_click()
        pr_page.set_email()
        pr_page.btn_recover_click()
        pr_page.click_element(PasswordRecoveryPageLocators.PAS, 100)
        elem = pr_page.set_pas_act()
        pr_page_div_class = elem.get_attribute("class")
        assert pr_page_div_class == TestAuthData.PAS_ACT_CL
