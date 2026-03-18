"""
Test 03: Shopping Cart Functionality - SauceDemo
==================================================
This test validates the complete add-to-cart workflow:
adding items, verifying cart count, and checking cart contents.

Website: https://www.saucedemo.com/
Author: [Your Name]
"""

from playwright.sync_api import sync_playwright


def login(page):
    """Helper function to log into SauceDemo."""
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.wait_for_url("**/inventory.html")


def test_add_single_item_to_cart():
    """Test adding a single item to the cart."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Login first
        login(page)

        # Step 1: Add the first product (Sauce Labs Backpack)
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")

        # Step 2: Verify the cart badge shows "1"
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.text_content() == "1", "Cart badge should show 1"

        # Step 3: Verify the button changed to "Remove"
        remove_button = page.locator("[data-test='remove-sauce-labs-backpack']")
        assert remove_button.is_visible(), "Remove button should appear after adding item"

        print("✅ TEST PASSED: Single item added to cart successfully")
        browser.close()


def test_add_multiple_items_to_cart():
    """Test adding multiple items and verifying cart count."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login(page)

        # Add 3 products
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        page.click("[data-test='add-to-cart-sauce-labs-bike-light']")
        page.click("[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")

        # Verify cart shows 3
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.text_content() == "3", "Cart badge should show 3"

        print("✅ TEST PASSED: Multiple items (3) added to cart")
        browser.close()


def test_verify_cart_contents():
    """Test that cart page shows the correct items."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login(page)

        # Add a specific product
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")

        # Navigate to cart
        page.click(".shopping_cart_link")
        page.wait_for_url("**/cart.html")

        # Verify the item is in the cart
        cart_items = page.locator(".cart_item")
        assert cart_items.count() == 1, "Cart should have exactly 1 item"

        item_name = page.locator(".inventory_item_name").text_content()
        assert item_name == "Sauce Labs Backpack", f"Expected 'Sauce Labs Backpack', got '{item_name}'"

        print(f"✅ TEST PASSED: Cart contains correct item: {item_name}")
        browser.close()


def test_remove_item_from_cart():
    """Test removing an item from the cart."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        login(page)

        # Add and then remove a product
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        page.click("[data-test='remove-sauce-labs-backpack']")

        # Verify cart badge is gone (no items)
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.count() == 0, "Cart badge should not be visible after removing item"

        print("✅ TEST PASSED: Item removed from cart successfully")
        browser.close()


if __name__ == "__main__":
    test_add_single_item_to_cart()
    test_add_multiple_items_to_cart()
    test_verify_cart_contents()
    test_remove_item_from_cart()
    print("\n🎉 All shopping cart tests passed!")
