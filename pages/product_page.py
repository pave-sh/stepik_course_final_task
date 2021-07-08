import math

from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), (
            'Impossible to find button which add item to basket'
        )

    def get_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        return item_name.text

    def get_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        return item_price.text

    def should_be_correct_added_item(self, item_name, item_price):
        self.is_text_present(*ProductPageLocators.ADDED_TO_BASKET_MSG, timeout=15)  # special case for firefox
        added_item_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_BASKET_MSG)
        added_item_name = added_item_name.text
        added_item_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE_MSG)
        added_item_price = added_item_price.text
        assert item_name == added_item_name, (
            f'Added item name {added_item_name!r} is not equal to expected {item_name!r}'
        )
        assert item_price == added_item_price, (
            f'Busket price {added_item_price!r} is not equal to expected {item_price!r}'
        )

    def should_be_success_adding_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MSG), (
            'Impossible to find success message after adding item to basket'
        )

    def should_not_be_success_adding_to_basket_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MSG), (
            'Success message is present but it should not'
        )

    def should_disappear_success_adding_to_basket_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_ADD_TO_BASKET_MSG), (
            'Success message should disappear but it should not'
        )

    def add_item_to_basket(self):
        self.should_be_add_to_basket_button()
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
