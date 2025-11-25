class LoginObjects:

    def __init__(self, page):
        self.page = page
        self.username_field = page.locator('//input[@name="user-name"]')
        self.password_field = page.locator('//input[@name="password"]')
        self.login_button = page.locator('//input[@id="login-button"]')
