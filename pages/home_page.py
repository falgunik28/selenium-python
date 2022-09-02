from selenium.webdriver.common.by import By


class Homepage:
    logged_in_user = (By.ID, "nameofuser")
    categories = (By.CSS_SELECTOR, "a#itemc")
    add_to_cart_button = (By.CSS_SELECTOR, ".btn.btn-success.btn-lg")
    cart = (By.ID, "cartur")
    log_out = (By.ID, "logout2")
    home_btn = (By.CSS_SELECTOR, ".nav-item.active")
    contact_us = (By.ID, "exampleModalLabel")
    menu_item = (By.CSS_SELECTOR, "#navbarExample .nav-link")
    contact_close = (By.CSS_SELECTOR, "#exampleModal .btn-secondary")
    about_us = (By.ID, "videoModalLabel")
    about_us_close = (By.CSS_SELECTOR, "#videoModal .btn-secondary")
    phones = (By.CLASS_NAME, "hrefch")
