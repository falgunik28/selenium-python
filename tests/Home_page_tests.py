import json
import time

from selenium.webdriver.support.wait import WebDriverWait
from pages.cart_page import Checkout
from pages.login_page import LoginPage
from tests.driver_details import OpenBrowser
from pages.home_page import Homepage
from selenium.webdriver.support import expected_conditions as EC

with open('../pages/testdata.json') as data_file:
    data = json.load(data_file)

d = OpenBrowser()


def login():
    d.driver.find_element(*LoginPage.login_button).click()
    # wait for element loading
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(LoginPage.sign_in_button))
    # entering username and password for login

    d.driver.find_element(*LoginPage.username).send_keys(data["username"])
    d.driver.find_element(*LoginPage.pwd).send_keys(data["password"])
    d.driver.find_element(*LoginPage.sign_in_button).click()
    # fetching the logged-in username from wep page
    WebDriverWait(d.driver, 10).until(EC.visibility_of_element_located(Homepage.logged_in_user))


def logout():
    d.driver.find_element(*Homepage.log_out).click()


def test_home_btn():
    login()
    message = d.driver.find_element(*Homepage.logged_in_user)
    assert (message.text == data["msg_text"])
    d.driver.find_element(*Homepage.home_btn)
    logout()


def test_contact_us_btn():
    login()
    items = d.driver.find_elements(*Homepage.menu_item)
    for item in items:
        if item.text == data["contact"]:
            # print(item.text)
            item.click()
            break
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.contact_close))
    msg = d.driver.find_element(*Homepage.contact_us).text
    assert (msg == data["contact_pg_header"])
    print(f"Contact-us tab is working fine!")
    d.driver.find_element(*Homepage.contact_close).click()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.log_out))
    logout()


def test_about_us_btn():
    login()
    items = d.driver.find_elements(*Homepage.menu_item)
    for item in items:
        if item.text == data["about_us"]:
            # print(item.text)
            item.click()
            break
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.about_us_close))
    msg = d.driver.find_element(*Homepage.about_us).text
    assert (msg == data["about_us_header"])
    print(f"About-us tab is working fine!")
    d.driver.find_element(*Homepage.about_us_close).click()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.log_out))
    logout()


def test_cart_btn():
    login()
    d.driver.find_element(*Homepage.cart).click()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.home_btn))
    msg = d.driver.find_element(*Checkout.place_order_btn).text
    assert (msg == data["place_order"])
    print(f"Cart tab is working fine!")
    d.driver.find_element(*Homepage.home_btn).click()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.log_out))
    logout()


def test_phone_categories():
    my_list = []
    login()
    category_lists = d.driver.find_elements(*Homepage.categories)
    for category in category_lists:
        print(category.text)
        if category.text == data["category_phone"]:
            category.click()
            break
    time.sleep(1)
    list_of_phones = d.driver.find_elements(*Homepage.phones)
    for phone in list_of_phones:
        my_list.append(phone.text)
    print(my_list)
    print(data["all_phones"])
    assert (my_list == data["all_phones"])
    print("category phone is fetching all phones only.It is working fine!")
    logout()


test_home_btn()
test_contact_us_btn()
test_about_us_btn()
test_cart_btn()
test_phone_categories()
d.driver.quit()
