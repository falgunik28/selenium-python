import json

from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import Homepage
# from pages.login_page import LoginPage
from tests.driver_details import driver
from selenium.webdriver.support import expected_conditions as EC

# read data from json file
with open('../pages/testdata.json') as data_file:
    # dt=data_file.read()
    data = json.load(data_file)

category_lists = driver.find_elements(*Homepage.categories)
for category in category_lists:
    print(category.text)
    if category.text == data["category_phone"]:
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
