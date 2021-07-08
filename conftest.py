import pytest
import random
import string

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--browser_name', action='store', default="chrome",
        help="Choose browser: chrome or firefox, chrome is default"
    )
    parser.addoption(
        '--language', action='store', default='en',
        help="Choose localization: en is default"
    )


@pytest.fixture
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'firefox':
        firefox_profile = webdriver.FirefoxProfile()
        firefox_profile.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=firefox_profile)
    else:
        raise pytest.UsageError(f"Invalid --browser_name value, expect chrome or firefox, get {browser_name!r}")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def gen_password():
    chars = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(10))


@pytest.fixture
def gen_email():
    chars = string.ascii_lowercase + string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(10)) + '@fakemail.org'
