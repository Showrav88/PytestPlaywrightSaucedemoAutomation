
class AddToCartObjects:
  def __init__(self, page):
        self.page = page
        # Menu Elements (XPath used in JS, converted to XPath or best selector)
        self.humburger_menu = page.locator("#react-burger-menu-btn")
        # Locator for "//a[text()='Reset App State']"
        self.reset_app_state = page.locator("text=Reset App State")
        # Locator for "//button[text()='Close Menu']"
        self.close_menu = page.locator("#react-burger-cross-btn")
        
        # Filter Dropdown
        self.filter_dropdown = page.locator("//select[@data-test='product-sort-container']")
        
        # Shopping and Checkout Buttons
        self.shopping_cart = page.locator("//a[@data-test='shopping-cart-link']")
        self.checkout_button = page.locator("text=Checkout")
        
        # Checkout Information Fields
        self.firstname_field = page.locator("//input[@data-test='firstName']")
        self.lastname_field = page.locator("//input[@data-test='lastName']")
        self.zip_code_field = page.locator("//input[@data-test='postalCode']")
        self.continue_button = page.locator("//input[@data-test='continue']")
        
        # Checkout Overview and Complete Page Buttons
        self.finish_button = page.locator("text=Finish")
        self.back_home_button = page.locator("text=Back Home")
        
        # Logout Button
        self.logout_button = page.locator("text=Logout")
        
        # NOTE: The 'finishButton' and 'backHomeButton' were duplicated in the JS. 
        # They are defined only once here for correctness.