from selenium.webdriver.common.by import By


class BasePageLocators:
    ELEM = (By.XPATH,
            "//h2[contains(@class, 'text text_type_digits-large mb-8')]")
    ACT_POP_UP = (By.XPATH,
                  "//div[contains(@class, 'Modal_modal__contentBox__sCy8X p-10')]")
    CROSS_POP_UP = (By.XPATH,
                    "//button[contains(@class, 'modified__3V5XS Modal_modal__close__TnseK')]")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    CL_ING = (By.XPATH,
              "//div[contains(@class, 'sCy8X p-10')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='Пароль']")
    SUB_BTN_CLICK_LOG = (By.XPATH, "//button[text()='Войти']")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    ING_LOC = (
        By.CSS_SELECTOR,
        ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")
    TEF_LOC = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
