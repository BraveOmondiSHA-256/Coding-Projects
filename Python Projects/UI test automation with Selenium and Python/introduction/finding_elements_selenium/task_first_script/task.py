from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"


def fill_form(browser):
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "# TODO")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "# TODO")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "# TODO")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "# TODO")
    button.click()

