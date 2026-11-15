
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.test_data import VALID_USERNAME, VALID_PASSWORD

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_inventory_page_loads(logged_in_driver):
    assert "inventory.html" in logged_in_driver.current_url


def test_all_products_are_displayed(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    products = inventory.get_product_names()

    assert len(products) > 0


def test_product_names_are_not_empty(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    products = inventory.get_product_names()

    assert all(name.strip() for name in products)


def test_product_prices_are_valid(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    prices = inventory.get_product_prices()

    assert len(prices) > 0
    assert all(price > 0 for price in prices)


def test_sort_products_name_a_to_z(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.sort_by_name_a_to_z()

    names = inventory.get_product_names()

    assert names == sorted(names)


def test_sort_products_price_low_to_high(logged_in_driver):
    inventory = InventoryPage(logged_in_driver)
    inventory.sort_by_price_low_to_high()

    prices = inventory.get_product_prices()

    assert prices == sorted(prices)
