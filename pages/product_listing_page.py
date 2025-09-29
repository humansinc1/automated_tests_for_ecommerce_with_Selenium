from pages.base_page import BasePage
from pages.locators import product_listing_page_locators, header_locators
from selenium.webdriver.support import expected_conditions as EC


class ProductListingPage(BasePage):
    page_url = '/category/desks-1'


    def add_product_to_the_cart_from_plp(self):
        self.wait().until(EC.presence_of_element_located(product_listing_page_locators.cart_icon))
        product_card = self.find(product_listing_page_locators.product_card)
        add_to_cart_icon = self.find(product_listing_page_locators.cart_icon)
        self.action().move_to_element(product_card).move_to_element(add_to_cart_icon).click().perform()

    def click_continue_shopping_in_modal(self):
        self.wait().until(EC.presence_of_element_located(product_listing_page_locators.modal_title))
        continue_shopping = self.find(product_listing_page_locators.continue_shopping_button)
        continue_shopping.click()

    def is_popup_opened(self):
        self.wait().until(EC.presence_of_element_located(product_listing_page_locators.modal_title))
        popup = self.find(product_listing_page_locators.modal_title)
        assert popup.text == 'Add to cart'

    def is_product_not_added_to_cart(self):
        self.wait().until(EC.presence_of_element_located(product_listing_page_locators.modal_title))
        self.find(product_listing_page_locators.modal_close_button).click()
        assert self.find(header_locators.cart_qty_badge).value_of_css_property('display') == 'none'
