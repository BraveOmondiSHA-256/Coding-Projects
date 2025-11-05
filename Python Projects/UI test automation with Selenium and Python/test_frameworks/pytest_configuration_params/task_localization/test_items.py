import pytest
from selenium.webdriver.common.by import By

@pytest.fixture
def link():
    return "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_is_have_button_add_to_basket(browser, link):
# TODO
