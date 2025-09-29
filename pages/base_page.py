from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.locators import header_locators


class BasePage:
    base_url = 'http://testshop.qa-practice.com/shop'
    page_url = None


    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened')

    def find(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_all(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def wait(self):
        wait = WebDriverWait(self.driver, 5)
        return wait

    def action(self):
        action = ActionChains(self.driver)
        return action

    def was_product_added_to_the_cart(self):
        self.wait().until(
            EC.text_to_be_present_in_element(header_locators.cart_qty_badge, '1')
        )
        assert self.find(header_locators.cart_qty_badge).text == '1'
