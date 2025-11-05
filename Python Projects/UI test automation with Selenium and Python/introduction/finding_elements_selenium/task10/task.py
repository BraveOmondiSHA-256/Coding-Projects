from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"


def finding_unique_selectors(browser):
    browser.get(link)
# TODO
    time.sleep(1)
    assert "Congratulations! You have successfully registered!" == browser.find_element(By.TAG_NAME, "h1").text
