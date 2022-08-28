from selenium.webdriver.common.by import By


class Checkout:
    place_order_btn = (By.CSS_SELECTOR, ".btn.btn-success")
    products_table = (By.CSS_SELECTOR, "#tbodyid tr")
    purchase_order_btn = (By.CSS_SELECTOR, "#orderModal .btn-primary")
    name_of_purchaser = (By.ID, "name")
    country = (By.ID, "country")
    city = (By.ID, "city")
    card = (By.ID, "card")
    month = (By.ID, "month")
    year = (By.ID, "year")
    purchase_success_msg = (By.CSS_SELECTOR, ".sweet-alert h2")
    order_details = (By.CSS_SELECTOR, "p.lead")
