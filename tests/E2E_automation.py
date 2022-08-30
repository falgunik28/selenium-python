import datetime
import re
import time
import json
from pages.login_page import LoginPage
from pages.home_page import Homepage
from pages.cart_page import Checkout
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# read data from json file
with open('../pages/testdata.json') as data_file:
    # dt=data_file.read()
    data = json.load(data_file)


# added to git
def open_browser():
    if data['browser'] == 'chrome':
        service = Service(executable_path=data["chrome_driver_path"])
        driver = webdriver.Chrome(service=service)
    elif data['browser'] == 'firefox':
        service = Service(executable_path=data["ff_driver_path"])
        driver = webdriver.Firefox(service=service)
    else:
        driver = ""
    driver.get(data["website_link"])

    # signin

    print(data["exec_start"] + str(datetime.datetime.now()))
    driver.find_element(*LoginPage.login_button).click()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LoginPage.sign_in_button))

    driver.find_element(*LoginPage.username).send_keys(data["username"])
    driver.find_element(*LoginPage.pwd).send_keys(data["password"])
    driver.find_element(*LoginPage.sign_in_button).click()

    # homepage

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Homepage.logged_in_user))
    message = driver.find_element(*Homepage.logged_in_user)
    print(message.text)

    assert (message.text == data["msg_text"])

    # category_list=driver.find_element(By.CSS_SELECTOR, value ="a#itemc")
    category_lists = driver.find_elements(*Homepage.categories)
    for category in category_lists:
        print(category.text)
        if category.text == data["category_text"]:
            category.click()
            break
    phone_list = driver.find_elements(*Homepage.category_phones)
    for phn in phone_list:

        if phn.text == data["phn_text"]:
            phn.click()
            break
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Homepage.add_to_cart_button))
    driver.find_element(*Homepage.add_to_cart_button).click()

    driver.find_element(*Homepage.cart).click()
    # Cart_page
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Checkout.place_order_btn))

    time.sleep(1)

    cart_list = driver.find_elements(*Checkout.products_table)
    assert (len(cart_list) != 0)

    driver.find_element(*Checkout.place_order_btn).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Checkout.purchase_order_btn))

    driver.find_element(*Checkout.name_of_purchaser).send_keys(data["purchaser"])
    driver.find_element(*Checkout.country).send_keys(data["country"])
    driver.find_element(*Checkout.city).send_keys(data["city"])
    driver.find_element(*Checkout.card).send_keys(data["card_details"])
    driver.find_element(*Checkout.month).send_keys(data["validity_month"])
    driver.find_element(*Checkout.year).send_keys(data["valid_year"])

    driver.find_element(*Checkout.purchase_order_btn).click()

    confirmation_header = driver.find_element(*Checkout.purchase_success_msg).text
    assert (confirmation_header == data["confirmation_msg"])

    confirmation_msg = driver.find_element(*Checkout.order_details).text

    assert (bool(re.search("Id: [0-9]{7}", confirmation_msg)) == True)

    # message = driver.find_element(by=By.CSS_SELECTOR, value=".lead.text-muted").text
    print("Purchase successful")
    print(data["exec_end"] + str(datetime.datetime.now()))


open_browser()
