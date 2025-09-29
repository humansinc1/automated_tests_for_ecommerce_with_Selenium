import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.cart_page import CartPage
from pages.product_details_page import ProductDetailsPage
from pages.product_listing_page import ProductListingPage


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--unsafely-treat-insecure-origin-as-secure=http://testshop.qa-practice.com/")
    chrome_driver = webdriver.Chrome(options=chrome_options)
    chrome_driver.maximize_window()
    yield chrome_driver


@pytest.fixture()
def cart_page(driver):
    return CartPage(driver)


@pytest.fixture()
def product_details_page(driver):
    return ProductDetailsPage(driver)


@pytest.fixture()
def product_listing_page(driver):
    return ProductListingPage(driver)


@pytest.fixture()
def add_to_cart_pdp(product_details_page):
    product_details_page.open_page()
    product_details_page.add_product_to_cart()
    return product_details_page


@pytest.fixture()
def add_to_cart_plp(product_listing_page):
    product_listing_page.open_page()
    product_listing_page.add_product_to_the_cart_from_plp()
    return product_listing_page
