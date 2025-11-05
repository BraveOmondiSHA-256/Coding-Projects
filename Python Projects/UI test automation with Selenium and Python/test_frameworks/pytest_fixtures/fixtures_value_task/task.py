import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

filename = "answer.txt"
link = "http://suninjuly.github.io/math.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# add browser fixture


# add fixture answer_file, returning file object


def test_math(browser, answer_file):
# TODO
