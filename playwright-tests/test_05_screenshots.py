"""
Test 05: Screenshot Capture & Visual Verification
====================================================
This test demonstrates screenshot capabilities for visual QA:
- Full page screenshots
- Element-specific screenshots
- Screenshots on test failure
- Multiple viewport sizes (responsive testing)

Website: https://www.saucedemo.com/
Author: [Your Name]
"""

import os
from playwright.sync_api import sync_playwright


# Create screenshots directory if it doesn't exist
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def test_capture_login_page():
    """Capture a screenshot of the login page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        page.goto("https://www.saucedemo.com/")
        page.screenshot(path=f"{SCREENSHOT_DIR}/01_login_page.png", full_page=True)

        print(f"✅ Screenshot saved: {SCREENSHOT_DIR}/01_login_page.png")
        browser.close()


def test_capture_products_page():
    """Capture a screenshot of the products page after login."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        # Login
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

        # Capture full products page
        page.screenshot(path=f"{SCREENSHOT_DIR}/02_products_page.png", full_page=True)

        print(f"✅ Screenshot saved: {SCREENSHOT_DIR}/02_products_page.png")
        browser.close()


def test_capture_specific_element():
    """Capture a screenshot of a specific product card element."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        # Login
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")

        # Screenshot of just the first product card
        first_product = page.locator(".inventory_item").first
        first_product.screenshot(path=f"{SCREENSHOT_DIR}/03_product_card.png")

        print(f"✅ Element screenshot saved: {SCREENSHOT_DIR}/03_product_card.png")
        browser.close()


def test_capture_error_state():
    """Capture a screenshot when login fails (error state documentation)."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 720})

        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "wrong_user")
        page.fill("#password", "wrong_pass")
        page.click("#login-button")

        # Wait for error to appear, then screenshot
        page.locator("[data-test='error']").wait_for(state="visible")
        page.screenshot(path=f"{SCREENSHOT_DIR}/04_login_error_state.png")

        print(f"✅ Error state screenshot saved: {SCREENSHOT_DIR}/04_login_error_state.png")
        browser.close()


def test_responsive_screenshots():
    """Capture screenshots at different viewport sizes for responsive testing."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)

        viewports = {
            "desktop": {"width": 1920, "height": 1080},
            "tablet": {"width": 768, "height": 1024},
            "mobile": {"width": 375, "height": 812},
        }

        for device_name, viewport_size in viewports.items():
            page = browser.new_page(viewport=viewport_size)

            page.goto("https://www.saucedemo.com/")
            page.fill("#user-name", "standard_user")
            page.fill("#password", "secret_sauce")
            page.click("#login-button")
            page.wait_for_url("**/inventory.html")

            filename = f"{SCREENSHOT_DIR}/05_responsive_{device_name}.png"
            page.screenshot(path=filename, full_page=True)
            print(f"✅ {device_name.capitalize()} screenshot ({viewport_size['width']}x{viewport_size['height']}): {filename}")

            page.close()

        browser.close()

    print("\n✅ TEST PASSED: All responsive screenshots captured")


if __name__ == "__main__":
    test_capture_login_page()
    test_capture_products_page()
    test_capture_specific_element()
    test_capture_error_state()
    test_responsive_screenshots()
    print(f"\n🎉 All screenshots saved to '{SCREENSHOT_DIR}/' folder!")
