from selenium.webdriver.common.by import By


class MainFunctionalityPageLocators:
    BTN_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='Пароль']")
    SUB_BTN_CLICK_LOG = (By.XPATH, "//button[text()='Войти']")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    TEST_ING = (By.XPATH, ".// *[ @ id = 'root'] / div / main / div / div / ul / li[1]")
    TEST_ELEM = (By.XPATH, ".// *[ @ id = 'root'] / div / main / div / div / ul / li[1]")
    CROSS_POP_UP = (By.XPATH,
                    "//*[@id='root']/div/section[2]/div[1]/button")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    INGRID_LOC = (By.CSS_SELECTOR,
                  ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
