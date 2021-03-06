from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_appeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((how, what))
            )
        except TimeoutException:
            return False

        return True

    def is_text_present(self, how, what, timeout=15):
        def get_text(driver):
            result = False
            try:
                elem_text = driver.find_element(how, what).text
                if len(elem_text) > 0:
                    result = True
            except NoSuchElementException:
                pass
            finally:
                return result

        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                get_text
            )
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def view_basket(self):
        button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_LINK)
        button.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), (
            'User icon is not presented, probably unauthorised user'
        )
