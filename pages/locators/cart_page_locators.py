from selenium.webdriver.common.by import By


page_title = (By.TAG_NAME, 'h3')
empty_cart_text = (By.CLASS_NAME, 'alert')
product_title = (By.TAG_NAME, 'h6')
product_price = (By.CSS_SELECTOR, '[data-oe-expression="product_price"]')
product_qty = (By.CSS_SELECTOR, 'input.quantity')
checkout_button = (By.CSS_SELECTOR, '[name="website_sale_main_button"]')
checkout_title = (By.TAG_NAME, 'h3')
