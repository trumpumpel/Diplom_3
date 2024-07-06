from selenium.webdriver.common.by import By
from conftest import web_driver
import allure
from data import URL_LOG, URL_FORGOT_PASSWORD
from pages.password_recovery_page import PasswordRecoveryPage


@allure.title('Тестируем функционал восстановления пароля')
class TestPasswordRecoveryPage:
    @allure.title('Проверяем переход на страницу восстановления пароля по кнопке Восстановить пароль')
    def test_click_button_password_recovery(self, web_driver):
        pr_page = PasswordRecoveryPage(web_driver)
        pr_page.navigate(URL_LOG)
        pr_page.btn_recover_password_click()
        assert web_driver.current_url == URL_FORGOT_PASSWORD

    @allure.title('Проверяем ввод почты и клик по кнопке Восстановить')
    def test_set_email_click_button_recovery(self, web_driver):
        pr_page = PasswordRecoveryPage(web_driver)
        pr_page.navigate(URL_LOG)
        pr_page.btn_recover_password_click()
        pr_page.set_email()
        pr_page.btn_recover_click()
        assert web_driver.current_url == URL_FORGOT_PASSWORD

    @allure.title('Проверяем клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_to_button_show_hide_password(self, web_driver):
        pr_page = PasswordRecoveryPage(web_driver)
        pr_page.navigate(URL_LOG)
        pr_page.btn_recover_password_click()
        pr_page.set_email()
        pr_page.btn_recover_click()
        pr_page.click_element((By.CSS_SELECTOR, ".input__icon.input__icon-action"), 100)
        pr_page = web_driver.find_element(By.CSS_SELECTOR,
                                          "#root > div > main > div > form > fieldset:nth-child(1) > div > div")
        pr_page_div_class = pr_page.get_attribute("class")
        assert pr_page_div_class == "input pr-6 pl-6 input_type_text input_size_default input_status_active"
