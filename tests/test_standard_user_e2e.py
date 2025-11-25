import pytest
import random
from playwright.sync_api import expect

# --- Page Object Imports ---
# NOTE: Ensure these class names and file paths match your project structure.
from pages.login_actions import LoginActions
from pages.add_to_cart_actions import AddToCartActions

class TestStandardUserE2E:
    
    # The 'testdata' fixture comes from conftest.py
    # The 'page' fixture comes from pytest-playwright
    
    @pytest.fixture(autouse=True)
    def setup_pages(self, page, testdata):
        """Sets up the page objects and navigates to the base URL before each test."""
        self.login = LoginActions(page)
        self.add_to_cart = AddToCartActions(page)
        self.test_data = testdata
        
        # Navigate to the base URL before every test
        page.goto('https://www.saucedemo.com/')

    def test_standard_user_e2e_purchase(self, page):
        """Standard User should be able to log in and complete a purchase."""
        
        # --- 1. Login and Initial Setup ---
        
        standard_username = self.test_data["username"]["standard"]
        
        self.login.enter_username(standard_username)
        self.login.enter_password(self.test_data["password"])
        
        # Using the method as requested by the user, assuming it exists in LoginActions
        self.login.click_login() 
        
        expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
        print('User is able to login with valid username and password')

        # Reset app state (Good practice before shopping)
        self.add_to_cart.click_hamburger_menu()
        self.add_to_cart.click_reset_app_state()
        print('User is able to reset app state')
        self.add_to_cart.click_close_menu()
        print('User is able to close the menu')

        # --- 2. Select and Store Random Products ---
        
        names_locators = page.locator('.inventory_item_name').all()
        prices_locators = page.locator('.inventory_item_price').all()
        buttons_locators = page.locator('button.btn_inventory').all()
        
        num_products = len(buttons_locators)
        
        # Select 3 random unique indexes
        random_indexes = random.sample(range(num_products), k=3)

        selected_products = []

        # Add random products to cart + store name + price
        for idx in random_indexes:
            product_name = names_locators[idx].inner_text()
            product_price_text = prices_locators[idx].inner_text()
            
            # Convert "$29.99" string to a float number (29.99)
            product_price = float(product_price_text.replace('$', ''))

            print(f'Product name: {product_name} | Price: {product_price}')
            buttons_locators[idx].click()

            selected_products.append({'name': product_name, 'price': product_price})

        # Verify cart badge shows 3
        cart_count = page.locator('.shopping_cart_badge').inner_text()
        
        # Assert on Python primitive (int) using native assert
        assert int(cart_count) == 3
        print('3 random items added to the cart successfully')

        # --- 3. Checkout Steps ---
        
        self.add_to_cart.click_shopping_cart_button()
        expect(page).to_have_url('https://www.saucedemo.com/cart.html')
        print('User is able to navigate to the cart page')
        
        self.add_to_cart.click_checkout_button()
        expect(page).to_have_url('https://www.saucedemo.com/checkout-step-one.html')
        print('User is able to navigate to the checkout page')
        
        # Fill shipping details
        self.add_to_cart.enter_firstname_field(self.test_data["firstname"])
        self.add_to_cart.enter_lastname_field(self.test_data["lastname"])
        self.add_to_cart.enter_zip_code_field(self.test_data["zipcode"])
        self.add_to_cart.click_continue_button()
        
        expect(page).to_have_url('https://www.saucedemo.com/checkout-step-two.html')
        print('User is able to navigate to the checkout overview page')

        # --- 4. Verification (Names and Totals) ---
        
        # Verify selected products at checkout
        checkout_names = page.locator('.inventory_item_name').all_inner_texts()
        selected_names = [p['name'] for p in selected_products]

        # Compare lists ignoring order using native Python 'assert'
        assert sorted(checkout_names) == sorted(selected_names)
        print("Product names verified successfully on the checkout overview page.")

        # Calculate expected item total
        expected_item_total = sum(p['price'] for p in selected_products)

        # Get item total displayed on page
        item_total_text = page.locator('.summary_subtotal_label').inner_text()
        displayed_item_total = float(item_total_text.replace('Item total: $', ''))

        # Verify item total using Python's native 'assert' with tolerance for floats
        assert abs(displayed_item_total - expected_item_total) < 0.01
        print(f"Item total verification successful: Expected ${expected_item_total:.2f}, Found ${displayed_item_total:.2f}")

        # Verify final total (item total + tax)
        tax_text = page.locator('.summary_tax_label').inner_text()
        # Ensure we handle the text format properly
        tax = float(tax_text.replace('Tax: $', ''))

        total_text = page.locator('.summary_total_label').inner_text()
        # Ensure we handle the text format properly
        displayed_final_total = float(total_text.replace('Total: $', ''))

        expected_final_total = expected_item_total + tax
        
        # Verify final total using Python's native 'assert' with tolerance for floats
        assert abs(displayed_final_total - expected_final_total) < 0.01
        print(f"Final total verification successful: Expected ${expected_final_total:.2f}, Found ${displayed_final_total:.2f}")

        # --- 5. Finish and Logout ---
        
        self.add_to_cart.click_finish_button()
        expect(page).to_have_url('https://www.saucedemo.com/checkout-complete.html')
        expect(page.locator('.complete-header')).to_have_text("Thank you for your order!", ignore_case=True)
        print('User is able to complete the purchase process successfully')
        
        self.add_to_cart.click_back_home_button()
        expect(page).to_have_url('https://www.saucedemo.com/inventory.html')
        
        # Final cleanup and logout
        self.add_to_cart.click_hamburger_menu()
        self.add_to_cart.click_reset_app_state()
        self.add_to_cart.click_logout_button()
        expect(page).to_have_url('https://www.saucedemo.com/')
        print('User is able to logout successfully')