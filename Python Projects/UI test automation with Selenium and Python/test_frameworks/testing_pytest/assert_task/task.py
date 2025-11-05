import math
import pytest
from selenium.webdriver.common.by import By
from selenium.common import NoAlertPresentException

link = "https://suninjuly.github.io/divide.html"


def test_valid_input(browser, input):
    browser.get(link)
# TODO
def test_invalid_input(browser, input):
    browser.get(link)
# TODO