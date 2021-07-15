import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage


def get_links_to_valid():
    links_to_validate = [
        pytest.param(
            f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}',
            marks=pytest.mark.xfail(reason='will not fix') if offer_num == 7 else ()
        )
        for offer_num in range(0, 10)
    ]
    return links_to_validate


@pytest.mark.need_review
@pytest.mark.parametrize('link', get_links_to_valid())
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    item_to_add_name = page.get_item_name()
    item_to_add_price = page.get_item_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_added_item(item_to_add_name, item_to_add_price)


@pytest.mark.parametrize(
    'link', [
        pytest.param(
            'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207',
            marks=pytest.mark.xfail(reason='expected fail')
        )
    ]
)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_not_be_success_adding_to_basket_message()


@pytest.mark.parametrize('link', [pytest.param('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207')])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_adding_to_basket_message()


@pytest.mark.parametrize(
    'link', [
        pytest.param(
            'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207',
            marks=pytest.mark.xfail(reason='expected fail')
        )
    ]
)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_item_to_basket()
    page.should_disappear_success_adding_to_basket_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_94/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page = LoginPage(browser, link)
    page.should_be_login_url()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_93/"
    page = ProductPage(browser, link)
    page.open()
    page.view_basket()
    page = BasketPage(browser, browser.current_url)
    page.should_be_empty_basket()
    page.should_be_empty_basket_message()


@pytest.mark.parametrize(
    'link', [pytest.param('https://selenium1py.pythonanywhere.com/en-gb/catalogue/stand-on-zanzibar_90/')]
)
class TestUserAddToBasketFromProductPage:

    @pytest.fixture(autouse=True)
    def setup(self, browser, gen_password, gen_email):
        register_link = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
        page = LoginPage(browser, register_link)
        page.open()
        page.should_be_login_link()
        page.should_be_register_form()
        password = gen_password
        email = gen_email
        page.register_new_user(email, password)
        page = MainPage(browser, browser.current_url)
        page.should_be_register_success_message()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_adding_to_basket_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        item_to_add_name = page.get_item_name()
        item_to_add_price = page.get_item_price()
        page.add_item_to_basket()
        page.should_be_correct_added_item(item_to_add_name, item_to_add_price)
