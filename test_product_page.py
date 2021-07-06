import pytest
from .pages.product_page import ProductPage


def get_links_to_valid():
    links_to_validate = [
        pytest.param(
            f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer_num}',
            marks=pytest.mark.xfail(reason='will not fix') if offer_num == 7 else ()
        )
        for offer_num in range(0, 10)
    ]
    return links_to_validate


@pytest.mark.parametrize('link', get_links_to_valid())
@pytest.mark.skip
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
