from pages.base_page import BasePage
from pages.locators import product_details_page_locators, header_locators
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsPage(BasePage):
    page_url = '/furn-9999-office-design-software-7?category=9'
    product_name = None
    product_price = None
    product_qty = None


    def add_product_to_cart(self):
        self.product_name = self.find(product_details_page_locators.product_name).text
        self.product_price = self.find(product_details_page_locators.product_price).text
        self.product_qty = self.find(product_details_page_locators.product_qty).value_of_css_property('value')
        add_to_cart_button = self.find(product_details_page_locators.add_to_cart_button)
        add_to_cart_button.click()
        self.wait().until(EC.text_to_be_present_in_element(header_locators.cart_qty_badge, '1'))

    def is_add_to_cart_button_color_correct(self):
        add_to_cart_button = self.find(product_details_page_locators.add_to_cart_button)
        assert add_to_cart_button.value_of_css_property('background-color') == 'rgba(17, 100, 102, 1)'

    def is_add_to_cart_button_hover_color_correct(self):
        add_to_cart_button = self.find(product_details_page_locators.add_to_cart_button)
        self.action().move_to_element(add_to_cart_button).perform()
        assert add_to_cart_button.value_of_css_property('background-color') == 'rgba(14, 85, 87, 1)'

    def are_breadcrumbs_clickable(self):
        self.wait().until(EC.element_to_be_clickable(product_details_page_locators.breadcrumb_1))
        breadcrumb_1 = self.find(product_details_page_locators.breadcrumb_1)
        breadcrumb_1.click()
        self.wait().until(EC.visibility_of_element_located(product_details_page_locators.page_body))
        assert self.driver.current_url == 'http://testshop.qa-practice.com/shop/category/multimedia-9'
        self.driver.back()
        breadcrumb_2 = self.find(product_details_page_locators.breadcrumb_2)
        self.wait().until(EC.element_to_be_clickable(product_details_page_locators.breadcrumb_1))
        breadcrumb_2.click()
        assert self.driver.current_url == 'http://testshop.qa-practice.com/shop'
