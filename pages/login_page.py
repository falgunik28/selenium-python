from selenium.webdriver.common.by import By


class LoginPage:
    # login locators
    login_button = (By.ID, "login2")
    username = (By.ID, "loginusername")
    pwd = (By.ID, "loginpassword")
    sign_in_button = (By.CSS_SELECTOR, "#logInModal .btn-primary")
    login_close = (By.CSS_SELECTOR, "#logInModal .btn-secondary")
    #sign_up locators
    signup_btn = (By.ID, "signin2")
    sign_uname = (By.ID, "sign-username")
    sign_pwd = (By.ID, "sign-password")
    register_button = (By.CSS_SELECTOR, "#signInModal .btn-primary")
    signup_close = (By.CSS_SELECTOR, "#signInModal .btn-secondary")




