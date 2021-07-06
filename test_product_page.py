from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    item_to_add_name = page.get_item_name()
    item_to_add_price = page.get_item_price()
    page.add_item_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_added_item(item_to_add_name, item_to_add_price)
