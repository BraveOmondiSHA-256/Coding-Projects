from selenium.webdriver.common.by import By

lesson_link = "https://stepik.org/lesson/236895/step/1"


def test_authorisation(browser):
    browser.get(lesson_link)
# TODO