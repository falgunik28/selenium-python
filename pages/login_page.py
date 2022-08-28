from selenium.webdriver.common.by import By


class LoginPage:
    login_button = (By.ID, "login2")
    username = (By.ID, "loginusername")
    pwd = (By.ID, "loginpassword")
    sign_in_button=(By.CSS_SELECTOR,"#logInModal .btn-primary")
