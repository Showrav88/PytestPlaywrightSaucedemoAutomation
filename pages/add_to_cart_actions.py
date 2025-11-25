from page_objects.add_to_cart_objects import AddToCartObjects
from playwright.sync_api import Page

class AddToCartActions:
    """
    Action class for AddToCart and Checkout functionality.
    Converts JavaScript asynchronous logic to Python synchronous Playwright logic.
    """
    def __init__(self, page: Page):
        self.page = page
        # Locate uses the synchronous objects file
        self.locate = AddToCartObjects(page)

    # --- Menu Actions ---
    def click_hamburger_menu(self):
        self.locate.humburger_menu.click()

    def click_reset_app_state(self):
        self.locate.reset_app_state.click()

    def click_close_menu(self):
        self.locate.close_menu.click()
        
    def click_logout_button(self):
        self.locate.logout_button.click()

    # --- Shopping/Cart Actions ---
    def click_shopping_cart_button(self):
        self.locate.shopping_cart.click()

    # --- Checkout Actions (Step 1) ---
    def click_checkout_button(self):
        self.locate.checkout_button.click()

    def enter_firstname_field(self, firstname: str):
        # Note: Renamed from enterFirstnameField to snake_case in Python
        self.locate.firstname_field.fill(firstname)

    def enter_lastname_field(self, lastname: str):
        # Note: Renamed from enterLastnameField to snake_case in Python
        self.locate.lastname_field.fill(lastname)

    def enter_zip_code_field(self, zipcode: str):
        # Note: Renamed from enterZipCodeField to snake_case in Python
        self.locate.zip_code_field.fill(zipcode)

    def click_continue_button(self):
        self.locate.continue_button.click()

    # --- Checkout Actions (Step 2/Complete) ---
    def click_finish_button(self):
        self.locate.finish_button.click()

    def click_back_home_button(self):
        self.locate.back_home_button.click()

    # --- Filter Actions ---
    def select_filter_option(self):
        self.locate.filter_dropdown.click()
        # Converted await this.page.waitForTimeout(3000)
        self.page.wait_for_timeout(3000)

    def select_filter_option_za(self, option: str):
        # Note: Renamed from selectFilterOptionZA to snake_case in Python
        self.locate.filter_dropdown.select_option(option)