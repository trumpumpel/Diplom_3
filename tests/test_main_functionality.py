from conftest import web_driver
import allure
from data import TestUrlData
from pages.main_functionality_page import MainFunctionalityPage


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
        mf_page.click_on_ingred_in_order_feed()
        elem = mf_page.click_ing_ord_feed()
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == TestUrlData.ACT_WIN

    @allure.title('Проверяем закрывается ли окно кликом по крестику')
    def test_clicking_on_the_cross_closes_the_pop_up_window(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.button_personal_account_click()
        mf_page.set_email()
        mf_page.set_pas()
        mf_page.enter_button_click()
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page.place_order_btn_click()
        mf_page.click_on_ingred_in_order_feed()
        elem = mf_page.set_cl_pop_up()
        mf_page_div_class = elem.get_attribute("class")
        assert mf_page_div_class == TestUrlData.CL_WIN

    #
    @allure.title('Проверяем увеличение значения счётчика при добавлении ингридиента в заказ')
    def test_adding_ingredient_to_order(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page_p_text = mf_page.set_counter()
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
        mf_page_p_text = mf_page.set_order_in_progress()
        assert "Ваш заказ начали готовить" in mf_page_p_text.text

    @allure.title('Проверяем возможность оформить заказ незалогиненным пользователем')
    def test_placing_an_order_not_logged_in_user(self, web_driver):
        mf_page = MainFunctionalityPage(web_driver)
        mf_page.adding_ingredients_to_order(web_driver)
        mf_page.button_enter_pers_acc_click()
        r_url = mf_page.count_url(web_driver)
        assert r_url == f'{TestUrlData.URL}{TestUrlData.URL_LOG}'
