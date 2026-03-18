"""
Test 04: Complete Checkout Flow - SauceDemo (End-to-End)
=========================================================
This is a full end-to-end test that simulates a complete user journey:
Login → Browse → Add to Cart → Checkout → Complete Order

Website: https://www.saucedemo.com/
Author: [Your Name]
"""

from playwright.sync_api import sync_playwright


def test_complete_checkout_flow():
    """End-to-end test: Login → Add item → Checkout → Order complete."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # ========== STEP 1: LOGIN ==========
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.wait_for_url("**/inventory.html")
        print("  ✓ Step 1: Logged in successfully")

        # ========== STEP 2: ADD ITEM TO CART ==========
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.text_content() == "1"
        print("  ✓ Step 2: Added 'Sauce Labs Backpack' to cart")

        # ========== STEP 3: GO TO CART ==========
        page.click(".shopping_cart_link")
        page.wait_for_url("**/cart.html")
        item_name = page.locator(".inventory_item_name").text_content()
        assert item_name == "Sauce Labs Backpack"
        print(f"  ✓ Step 3: Cart contains: {item_name}")

        # ========== STEP 4: PROCEED TO CHECKOUT ==========
        page.click("[data-test='checkout']")
        page.wait_for_url("**/checkout-step-one.html")
        print("  ✓ Step 4: Navigated to checkout")

        # ========== STEP 5: FILL CHECKOUT INFO ==========
        page.fill("[data-test='firstName']", "Jane")
        page.fill("[data-test='lastName']", "Smith")
        page.fill("[data-test='postalCode']", "92401")
        page.click("[data-test='continue']")
        page.wait_for_url("**/checkout-step-two.html")
        print("  ✓ Step 5: Filled checkout information")

        # ========== STEP 6: VERIFY ORDER SUMMARY ==========
        summary_item = page.locator(".inventory_item_name").text_content()
        assert summary_item == "Sauce Labs Backpack"

        # Verify price is displayed
        item_price = page.locator(".inventory_item_price").text_content()
        assert "$" in item_price, "Price should be displayed"
        print(f"  ✓ Step 6: Order summary verified - {summary_item} at {item_price}")

        # ========== STEP 7: COMPLETE ORDER ==========
        page.click("[data-test='finish']")
        page.wait_for_url("**/checkout-complete.html")

        # Verify success message
        complete_header = page.locator(".complete-header").text_content()
        assert "Thank you for your order" in complete_header
        print(f"  ✓ Step 7: Order completed - '{complete_header}'")

        print("\n✅ FULL E2E TEST PASSED: Complete checkout flow successful!")
        browser.close()


def test_checkout_missing_info():
    """Test that checkout fails gracefully when info is missing."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Quick login and add item
        page.goto("https://www.saucedemo.com/")
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")
        page.click("[data-test='add-to-cart-sauce-labs-backpack']")
        page.click(".shopping_cart_link")
        page.click("[data-test='checkout']")

        # Try to continue without filling any info
        page.click("[data-test='continue']")

        # Verify error message appears
        error = page.locator("[data-test='error']")
        assert error.is_visible(), "Error message should appear for missing info"
        error_text = error.text_content()
        assert "First Name is required" in error_text

        print("✅ TEST PASSED: Checkout correctly requires customer information")
        browser.close()


if __name__ == "__main__":
    test_complete_checkout_flow()
    test_checkout_missing_info()
    print("\n🎉 All checkout tests passed!")
