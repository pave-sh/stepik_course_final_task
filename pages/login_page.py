from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        cur_url = self.browser.current_url
        assert LoginPageLocators.LOGIN_LINK_SUBSTRING in cur_url, (
            f'Login url {cur_url!r} does not contain expected word {LoginPageLocators.LOGIN_LINK_SUBSTRING!r}'
        )

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), (
            f'Impossible to find login form at login page {self.url}'
        )

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), (
            f'Impossible to find register form at login page {self.url}'
        )
