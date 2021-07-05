from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
	LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
	REGISTR_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
	CART_BUTTON = (By.CSS_SELECTOR, "form#add_to_basket_form button[type='submit']")
	CART_MESSAGE = (By.CSS_SELECTOR, "div#messages strong")
	BOOK_TITLE = (By.CSS_SELECTOR, "div.content h1")
	CART_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")
	BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")

