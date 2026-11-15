
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import FIRST_NAME, LAST_NAME, POSTAL_CODE, VALID_USERNAME, VALID_PASSWORD

from pages.login_page import LoginPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def prepare_checkout(logged_in_driver):
    cart = CartPage(logged_in_driver)
    cart.add_backpack()
    cart.open_cart()

    checkout = CheckoutPage(logged_in_driver)
    checkout.click_checkout()

    return checkout


def test_checkout_with_valid_information(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.enter_customer_information(
        FIRST_NAME, LAST_NAME, POSTAL_CODE
    )
    checkout.click_continue()

    assert "checkout-step-two.html" in logged_in_driver.current_url


def test_checkout_missing_first_name(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.enter_customer_information(
        "", LAST_NAME, POSTAL_CODE
    )
    checkout.click_continue()

    assert "First Name is required" in checkout.get_error_message()


def test_checkout_missing_last_name(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.enter_customer_information(
        FIRST_NAME, "", POSTAL_CODE
    )
    checkout.click_continue()

    assert "Last Name is required" in checkout.get_error_message()


def test_checkout_missing_postal_code(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.enter_customer_information(
        FIRST_NAME, LAST_NAME, ""
    )
    checkout.click_continue()

    assert "Postal Code is required" in checkout.get_error_message()


def test_order_overview_displays_product_and_prices(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.enter_customer_information(
        FIRST_NAME, LAST_NAME, POSTAL_CODE
    )
    checkout.click_continue()

    assert "Sauce Labs Backpack" in checkout.get_product_names()
    assert "$29.99" in checkout.get_subtotal()
    assert "Tax:" in checkout.get_tax()
    assert "Total:" in checkout.get_total()


def test_complete_order_successfully(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.enter_customer_information(
        FIRST_NAME, LAST_NAME, POSTAL_CODE
    )
    checkout.click_continue()
    checkout.click_finish()

    assert checkout.get_confirmation_message() == "Thank you for your order!"


def test_cancel_checkout_returns_to_cart(logged_in_driver):
    checkout = prepare_checkout(logged_in_driver)

    checkout.click_cancel()

    assert "cart.html" in logged_in_driver.current_url
    assert "Sauce Labs Backpack" in checkout.get_product_names()
