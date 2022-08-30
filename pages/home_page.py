from selenium.webdriver.common.by import By


class Homepage:
    logged_in_user = (By.ID, "nameofuser")
    categories = (By.CSS_SELECTOR, "a#itemc")
    category_phones = (By.CLASS_NAME, "hrefch")
    add_to_cart_button = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    cart = (By.ID, "cartur")
    log_out = (By.ID, "logout2")
