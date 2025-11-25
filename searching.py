from time import time
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.google.com")

        # Type something into Google Search
        page.fill("input[name='q']", "Playwright Python search example")
        page.keyboard.press("Enter")

        time.sleep(3)
        browser.close()

