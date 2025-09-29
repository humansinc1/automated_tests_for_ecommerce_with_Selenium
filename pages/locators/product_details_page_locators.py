from selenium.webdriver.common.by import By


add_to_cart_button = (By.ID, 'add_to_cart')

product_name = (By.TAG_NAME, 'h1')
product_price = (By.CLASS_NAME, 'oe_price')
product_qty = (By.CSS_SELECTOR, 'input.quantity')
breadcrumb_1 = (By.CSS_SELECTOR, '.breadcrumb-item > [href="/shop/category/multimedia-9"]')
breadcrumb_2 = (By.CSS_SELECTOR, '.breadcrumb-item > [href="/shop"]')
page_body = (By.TAG_NAME, 'body')