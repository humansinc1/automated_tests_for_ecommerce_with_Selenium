from pages.base_page import BasePage
from pages.locators import cart_page_locators
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    page_url = '/cart'


    def is_cart_title_correct(self):
        title = self.find(cart_page_locators.page_title)
        assert title.text == 'Order overview'

    def is_empty_cart_text_correct(self):
        text = self.find(cart_page_locators.empty_cart_text)
        assert text.text == 'Your cart is empty!'

    def is_product_title_correct(self, product_name):
        self.wait().until(
            EC.visibility_of_element_located(cart_page_locators.product_title)
        )
        cart_product_title = self.find(cart_page_locators.product_title)
        assert cart_product_title.text == product_name

    def is_product_price_correct(self, product_price):
        self.wait().until(
            EC.visibility_of_element_located(cart_page_locators.product_title)
        )
        cart_product_price = self.find(cart_page_locators.product_price)
        assert cart_product_price.text == product_price

    def is_product_qty_correct(self, product_qty):
        self.wait().until(
            EC.visibility_of_element_located(cart_page_locators.product_title)
        )
        cart_product_qty = self.find(cart_page_locators.product_qty)
        assert cart_product_qty.value_of_css_property('value') == product_qty

    def is_checkout_button_clickable(self):
        self.wait().until(
            EC.element_to_be_clickable(cart_page_locators.checkout_button)
        )
        checkout_button = self.find(cart_page_locators.checkout_button)
        checkout_button.click()
        checkout_title = self.find(cart_page_locators.checkout_title)
        assert checkout_title.text == 'Fill in your address or Sign in'
