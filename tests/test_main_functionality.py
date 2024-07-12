from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from conftest import web_driver
from selenium.webdriver.support import expected_conditions as EC
import allure
from data import TestUrlData
from pages.main_functionality_page import MainFunctionalityPage
from locators.main_functionality_page_locators import MainFunctionalityPageLocators


class TestMainFunctionalityPage:

    @allure.title('Проверяем переход по клику на «Конструктор»')
    def test_click_button_constructor(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.navigate(f'{TestUrlData.URL}{TestUrlData.URL_LOG}')
        mf_page.button_constructor_click()
        r_url = mf_page.count_url(web_driver)
        assert r_url == TestUrlData.URL

    @allure.title('Проверяем переход по клику на «Лента заказов»')
    def test_click_button_order_feed(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.button_constructor_order_feed()
        r_url = mf_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_FEED}'

    #
    @allure.title('Проверяем появление всплывающего окна с деталями после клика на ингридиент')
    def test_click_ingredient(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.button_personal_account_click()
        mf_page.set_email()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page.place_order_btn_click()
        mf_page_text = web_driver.find_element(By.XPATH,
                                               "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
        number = mf_page_text.text
        mf_page.click_cross_pop_up()
        mf_page.button_constructor_order_feed()
        mf_page.click_element((By.XPATH, ".//*[contains(text(),'" + number + "')]"), 100)
        elem = web_driver.find_element(By.XPATH,
                                       "//div[contains(@class, 'sCy8X p-10')]")
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == "Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"

    @allure.title('Проверяем закрывается ли окно кликом по крестику')
    def test_clicking_on_the_cross_closes_the_pop_up_window(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.button_personal_account_click()
        mf_page.set_email()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page.place_order_btn_click()
        of_page_text = web_driver.find_element(By.XPATH,
                                               "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8')]")
        number = of_page_text.text
        mf_page.click_cross_pop_up()
        mf_page.button_constructor_order_feed()
        mf_page.click_element((By.XPATH, ".//*[contains(text(),'" + number + "')]"), 100)
        elem = web_driver.find_element(By.XPATH, "//div[contains(@class, 'P3_V5')]")
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == "Modal_modal__P3_V5"

    #
    @allure.title('Проверяем увеличение значения счётчика при добавлении ингридиента в заказ')
    def test_adding_ingredient_to_order(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page_p_text = web_driver.find_element(By.XPATH, "//p[@class='counter_counter__num__3nue1'][text()='2']")
        assert mf_page_p_text.text == "2"

    @allure.title('Проверяем возможность оформить заказ залогиненным пользователем')
    def test_placing_an_order_logged_in_user(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.button_personal_account_click()
        mf_page.set_email()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page.place_order_btn_click()
        mf_page_p_text = web_driver.find_element(By.XPATH, "//div[@class='Modal_modal__contentBox__sCy8X pt-30 pb-30']")
        assert "Ваш заказ начали готовить" in mf_page_p_text.text

    @allure.title('Проверяем возможность оформить заказ незалогиненным пользователем')
    def test_placing_an_order_not_logged_in_user(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.adding_ingredients_to_order(web_driver)
        assert WebDriverWait(web_driver, 10).until(
            EC.invisibility_of_element_located(MainFunctionalityPageLocators.PLACE_ORDER_BTN))
