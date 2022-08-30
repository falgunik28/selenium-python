import json
import time
import random
import string

from selenium.webdriver.support.wait import WebDriverWait
from tests.driver_details import OpenBrowser
from pages.home_page import Homepage
from pages.login_page import LoginPage
from selenium.webdriver.support import expected_conditions as EC

# read data from json file
with open('../pages/testdata.json') as data_file:
    # dt=data_file.read()
    data = json.load(data_file)
#
#
# class OpenBrowser:
#     service = Service(executable_path=data["chrome_driver_path"])
#     driver = webdriver.Chrome(service=service)
#     driver.get(data["website_link"])

d = OpenBrowser()


def test_login():
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
    logout()


def logout():
    d.driver.find_element(*Homepage.log_out).click()


def get_name():
    name = string.ascii_lowercase
    usr_name = (''.join(random.choice(name) for i in range(5)))
    return usr_name


def test_sign_up():
    d.driver.find_element(*LoginPage.signup_btn).click()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(LoginPage.register_button))
    new_name = get_name()
    d.driver.find_element(*LoginPage.sign_uname).send_keys(new_name)
    d.driver.find_element(*LoginPage.sign_pwd).send_keys(data["new_pwd"])
    d.driver.find_element(*LoginPage.register_button).click()
    time.sleep(1)
    alert_msg = d.driver.switch_to.alert.text
    # print(alert_msg)

    assert (alert_msg == data["alert_msg_02"])

    d.driver.switch_to.alert.accept()
    d.driver.find_element(*LoginPage.login_button).click()
    # wait for element loading
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(LoginPage.sign_in_button))
    # entering username and password for login

    d.driver.find_element(*LoginPage.username).send_keys(new_name)
    d.driver.find_element(*LoginPage.pwd).send_keys(data["new_pwd"])
    d.driver.find_element(*LoginPage.sign_in_button).click()
    # fetching the logged-in username from wep page
    WebDriverWait(d.driver, 10).until(EC.visibility_of_element_located(Homepage.logged_in_user))
    message = d.driver.find_element(*Homepage.logged_in_user)
    # uname = get_name()
    assert (message.text == ("Welcome "+new_name))

    print(message.text)
    logout()


def test_signin_error():
    d.driver.find_element(*LoginPage.login_button).click()
    # wait for element loading
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(LoginPage.sign_in_button))
    # entering username and password for login

    d.driver.find_element(*LoginPage.username).send_keys(data["username"])
    d.driver.find_element(*LoginPage.sign_in_button).click()
    msg = d.driver.switch_to.alert.text
    d.driver.switch_to.alert.accept()
    assert (msg == data["alert_msg_04"])
    print(msg)
    d.driver.find_element(*LoginPage.login_close).click()


def test_signup_error():
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(LoginPage.signup_btn))
    d.driver.find_element(*LoginPage.signup_btn).click()
    WebDriverWait(d.driver, 10).until(EC.element_to_be_clickable(LoginPage.register_button))
    new_name = get_name()
    d.driver.find_element(*LoginPage.sign_uname).send_keys(new_name)
    d.driver.find_element(*LoginPage.register_button).click()
    msg = d.driver.switch_to.alert.text
    d.driver.switch_to.alert.dismiss()
    assert (msg == data["alert_msg_04"])
    print(msg)
    d.driver.find_element(*LoginPage.signup_close).click()


# run test scenarios for login, signup and errors caught
test_sign_up()
test_login()
test_signin_error()
test_signup_error()
# Close browser session
d.driver.quit()
