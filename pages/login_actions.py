# pages/login_actions.py

from page_objects.login_objects import LoginObjects
from playwright.sync_api import Page

class LoginActions:
    def __init__(self, page: Page):
        self.page = page
        self.locate = LoginObjects(page)

    # 1. REMOVE 'async' and 'await'
    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    # 2. REMOVE 'async' and 'await'
    def enter_username(self, username):
        # Using the locator directly from the page object for clarity
        self.locate.username_field.fill(username) 
        # OR using the direct string locator:
        # self.page.fill('input[data-test="username"]', username)

    # 3. REMOVE 'async' and 'await'
    def enter_password(self, password):
        self.locate.password_field.fill(password)
        # OR using the direct string locator:
        # self.page.fill('input[data-test="password"]', password)

    # 4. REMOVE 'async' and 'await'
    def click_login(self):
        self.locate.login_button.click()
        # OR using the direct string locator:
        # self.page.click('input[data-test="login-button"]')