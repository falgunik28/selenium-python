import json
import time

from selenium.webdriver.support.wait import WebDriverWait
from pages.cart_page import Checkout
from pages.login_page import LoginPage
from tests.driver_details import OpenBrowser
from pages.home_page import Homepage
from selenium.webdriver.support import expected_conditions as EC

with open('../pages/testdata.json') as data_file:
    # dt=data_file.read()
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
    message = d.driver.find_element(*Homepage.logged_in_user)
    # uname = get_name()
    assert (message.text == data["msg_text"])
    print(message.text)


def test_add_to_cart():
    # category_list=driver.find_element(By.CSS_SELECTOR, value ="a#itemc")
    category_lists = d.driver.find_elements(*Homepage.categories)
    for category in category_lists:
        print(category.text)
        if category.text == data["category_text"]:
            category.click()
            break
    phone_list = d.driver.find_elements(*Homepage.category_phones)
    for phn in phone_list:

        if phn.text == data["phn_text"]:
            phn.click()
            break
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.add_to_cart_button))
    d.driver.find_element(*Homepage.add_to_cart_button).click()

    d.driver.find_element(*Homepage.cart).click()
    # Cart_page
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Checkout.place_order_btn))

    WebDriverWait(d.driver, 10).until(EC.visibility_of_all_elements_located(Checkout.products_table))

    cart_list = d.driver.find_elements(*Checkout.products_table)
    assert (len(cart_list) != 0)


def test_add_to_cart_thrice():
    login()
    category_lists = d.driver.find_elements(*Homepage.categories)
    for category in category_lists:
        print(category.text)
        if category.text == data["category_text"]:
            category.click()
            break
    phone_list = d.driver.find_elements(*Homepage.category_phones)
    for phn in phone_list:

        if phn.text == data["phn_text"]:
            phn.click()
            break
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.add_to_cart_button))

    d.driver.find_element(*Homepage.add_to_cart_button).click()
    time.sleep(1)
    d.driver.switch_to.alert.accept()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.add_to_cart_button))
    d.driver.find_element(*Homepage.add_to_cart_button).click()
    time.sleep(1)
    d.driver.switch_to.alert.accept()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.add_to_cart_button))
    d.driver.find_element(*Homepage.add_to_cart_button).click()
    time.sleep(1)
    d.driver.switch_to.alert.accept()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(Homepage.cart))
    d.driver.find_element(*Homepage.cart).click()
    WebDriverWait(d.driver, 10).until(EC.visibility_of_all_elements_located(Checkout.products_table))
    cart = d.driver.find_elements(*Checkout.products_table)
    print(f"Items in the cart: {len(cart)}")
    assert (len(cart) == 3)
    for i in range(3):
        test_delete_cart()

    logout()


def logout():
    d.driver.find_element(*Homepage.log_out).click()


def test_delete_cart():
    cart_list = d.driver.find_elements(*Checkout.products_table)
    # print(len(cart_list))
    d.driver.find_element(*Checkout.delete_button).click()
    # WebDriverWait(d.driver, 20).until(EC.visibility_of_all_elements_located(Checkout.product_body_class))
    time.sleep(2)
    new_list = d.driver.find_elements(*Checkout.product_body_class)
    # print(len(new_list))

    assert (len(new_list) == (len(cart_list)-1))
    print("Item deleted")
    # logout()


# Check the add to cart, add multiple items in the cart and delete cart functionality
login()
test_add_to_cart()
test_delete_cart()
logout()
test_add_to_cart_thrice()
d.driver
