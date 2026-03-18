"""
Test 01: Login Functionality - SauceDemo
==========================================
This test validates the login functionality of the SauceDemo e-commerce site.
It covers both successful login and invalid login scenarios.

Website: https://www.saucedemo.com/
Author: [Your Name]
"""

from playwright.sync_api import sync_playwright, expect


def test_successful_login():
    """Test that a valid user can log in and reach the products page."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Step 1: Navigate to SauceDemo
        page.goto("https://www.saucedemo.com/")
        assert "Swag Labs" in page.title()

        # Step 2: Enter valid credentials
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # Step 3: Click the Login button
        page.click("#login-button")

        # Step 4: Verify we landed on the products page
        page.wait_for_url("**/inventory.html")
        header = page.locator(".title")
        assert header.text_content() == "Products"

        print("✅ TEST PASSED: Successful login - user reached Products page")
        browser.close()


def test_invalid_login():
    """Test that an invalid user sees an error message."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Step 1: Navigate to SauceDemo
        page.goto("https://www.saucedemo.com/")

        # Step 2: Enter invalid credentials
        page.fill("#user-name", "invalid_user")
        page.fill("#password", "wrong_password")

        # Step 3: Click the Login button
        page.click("#login-button")

        # Step 4: Verify error message is displayed
        error_message = page.locator("[data-test='error']")
        assert error_message.is_visible()
        assert "do not match" in error_message.text_content()

        print("✅ TEST PASSED: Invalid login - error message displayed correctly")
        browser.close()


def test_locked_out_user():
    """Test that a locked out user sees an appropriate error."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "locked_out_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        error_message = page.locator("[data-test='error']")
        assert error_message.is_visible()
        assert "locked out" in error_message.text_content()

        print("✅ TEST PASSED: Locked out user - appropriate error shown")
        browser.close()


if __name__ == "__main__":
    test_successful_login()
    test_invalid_login()
    test_locked_out_user()
    print("\n🎉 All login tests passed!")
