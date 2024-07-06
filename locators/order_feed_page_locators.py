from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    ORDER_FEED = (By.XPATH, "//p[text()='Лента Заказов']")
    ORDER_TEST_EL = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem__2x95r mb-6')][1]")
    SET_EMAIL_LOG = (By.XPATH, "//label[text()='Email']/../input")
    SET_PAS_LOG = (By.CSS_SELECTOR, "input[name='Пароль']")
    SUB_BTN_CLICK_LOG = (By.XPATH, "//button[text()='Войти']")
    PERSONAL_ACCOUNT = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    ORDER_HISTORY_BUTTON = (By.XPATH, "//a[text()='История заказов']")
    PLACE_ORDER_BTN = (By.XPATH, "//button[text()='Оформить заказ']")
    CROSS_POP_UP = (
        By.XPATH, "//button[contains(@class, 'modified__3V5XS Modal_modal__close__TnseK')]")
