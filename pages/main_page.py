from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_register_success_message(self):
        assert self.is_appeared(*MainPageLocators.LOGIN_SUCCESS_MSG, timeout=15), (
            'Impossible to find success message after user registration, maybe registration has failed'
        )
