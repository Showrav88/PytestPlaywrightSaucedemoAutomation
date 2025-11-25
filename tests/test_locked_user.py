# tests/test_locked_user.py
import pytest
from playwright.sync_api import expect # Note: You'll switch to the sync expect, but this import is fine for type hinting
from pages.login_actions import LoginActions

# REMOVE @pytest.mark.asyncio and async
def test_locked_out_user_login_error(page, testdata):
    # 'page' is now the synchronous Playwright Page object provided by the plugin
    login = LoginActions(page)
    
    # You MUST also switch your LoginActions methods to be synchronous
    login.navigate()
    login.enter_username(testdata["username"]["locked"])
    login.enter_password(testdata["password"])
    login.click_login()

    error_message = page.locator('[data-test="error"]')
    
    # Use the synchronous version of expect (it handles the await internally)
    expect(error_message).to_be_visible()
    print(error_message.text_content()) # Text content should also be called synchronously