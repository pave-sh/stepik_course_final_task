import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage


MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com"


def test_guest_can_go_to_login_page(browser):
    link = MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = MAIN_PAGE_URL
    page = MainPage(browser, link)
    page.open()
    page.view_basket()
    page.should_be_empty_basket()
    page.should_be_empty_basket_message()
