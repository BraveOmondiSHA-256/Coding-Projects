import math
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def execute_script(browser):
# TODO