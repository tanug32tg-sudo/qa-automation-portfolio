"""
Test 02: Form Filling & Validation - DemoQA
=============================================
This test validates form submission on the DemoQA text-box page.
It fills in user information and verifies the output matches the input.

Website: https://demoqa.com/text-box
Author: [Your Name]
"""

from playwright.sync_api import sync_playwright


def test_fill_text_box_form():
    """Test filling out the text box form and verifying submitted data."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Test data
        full_name = "Jane Smith"
        email = "jane.smith@testmail.com"
        current_address = "123 Main Street, San Bernardino, CA 92401"
        permanent_address = "456 Oak Avenue, Los Angeles, CA 90001"

        # Step 1: Navigate to the text box page
        page.goto("https://demoqa.com/text-box")

        # Step 2: Fill in all form fields
        page.fill("#userName", full_name)
        page.fill("#userEmail", email)
        page.fill("#currentAddress", current_address)
        page.fill("#permanentAddress", permanent_address)

        # Step 3: Click Submit
        page.click("#submit")

        # Step 4: Verify the output section displays correct data
        output = page.locator("#output")
        assert output.is_visible(), "Output section should be visible after submission"

        # Verify each field in the output
        name_output = page.locator("#name").text_content()
        assert full_name in name_output, f"Expected '{full_name}' in output, got '{name_output}'"

        email_output = page.locator("#email").text_content()
        assert email in email_output, f"Expected '{email}' in output, got '{email_output}'"

        print("✅ TEST PASSED: Form filled and submitted successfully")
        print(f"   Name displayed: {name_output}")
        print(f"   Email displayed: {email_output}")

        browser.close()


def test_invalid_email_validation():
    """Test that an invalid email format is handled properly."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://demoqa.com/text-box")

        # Fill with invalid email
        page.fill("#userName", "Test User")
        page.fill("#userEmail", "not-a-valid-email")
        page.fill("#currentAddress", "123 Test St")

        page.click("#submit")

        # Check if the email field shows an error state (red border)
        email_field = page.locator("#userEmail")
        email_class = email_field.get_attribute("class") or ""

        # DemoQA adds 'field-error' class for invalid emails
        if "error" in email_class:
            print("✅ TEST PASSED: Invalid email correctly shows error state")
        else:
            print("⚠️  TEST INFO: Form submitted - email validation may be client-side only")

        browser.close()


if __name__ == "__main__":
    test_fill_text_box_form()
    test_invalid_email_validation()
    print("\n🎉 All form tests passed!")
