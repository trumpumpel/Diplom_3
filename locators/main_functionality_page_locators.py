from selenium.webdriver.common.by import By


class MainFunctionalityPageLocators:
    BTN_RECOVER_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='Пароль']")
    SUB_BTN_CLICK_LOG = (By.XPATH, "//button[text()='Войти']")
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    CROSS_POP_UP = (By.XPATH,
                    "//button[contains(@class, 'modified__3V5XS Modal_modal__close__TnseK')]")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    BTN_ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
