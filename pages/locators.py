from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    VIEW_BASKET = (By.XPATH, '//div[contains(@class, "basket-mini")]/span/a')
    BASKET_ITEMS = (By.XPATH, '//div[@id="content_inner"]//div[@class="basket-items"]')
    EMPTY_BASKET_MSG = (By.XPATH, '//div[@id="content_inner"]/p')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK_SUBSTRING = 'login'
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    LOGIN_EMAIL = (By.XPATH, '//form[@id="login_form"]//input[@name="login-username"]')
    LOGIN_PASSWORD = (By.XPATH, '//form[@id="login_form"]//input[@name="login-password"]')

    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')
    REGISTER_EMAIL = (By.XPATH, '//form[@id="register_form"]//input[@name="registration-email"]')
    REGISTER_PASSWORD = (By.XPATH, '//form[@id="register_form"]//input[@name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD = (By.XPATH, '//form[@id="register_form"]//input[@name="registration-password2"]')


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, '//form[@id="add_to_basket_form"]/button[contains(@class, "btn-add-to-basket")]')

    ITEM_NAME = (By.XPATH, '//div[contains(@class, "product_main")]/h1')
    ITEM_PRICE = (By.XPATH, '//div[contains(@class, "product_main")]/p[@class="price_color"]')

    ADDED_TO_BASKET_MSG = (By.XPATH, '//div[@id="messages"]/div[1]//strong')
    BASKET_PRICE_MSG = (By.XPATH, '//div[@id="messages"]/div[3]//strong')

    SUCCESS_ADD_TO_BASKET_MSG = (By.XPATH, '//div[@id="messages"]/div[contains(@class, "alert-success")]/div')
