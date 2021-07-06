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
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    item_to_add_name = page.get_item_name()
    item_to_add_price = page.get_item_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_added_item(item_to_add_name, item_to_add_price)
