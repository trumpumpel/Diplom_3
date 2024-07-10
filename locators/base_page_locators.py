from selenium.webdriver.common.by import By


class BasePageLocators:
    INGRID_LOC = (By.CSS_SELECTOR,
                  ".BurgerIngredients_ingredients__menuContainer__Xu3Mo > ul:nth-child(2) > a:nth-child(1) > img")
    TEFKI_LOC = (By.XPATH, "//ul[@class='BurgerConstructor_basket__list__l9dp_']")
