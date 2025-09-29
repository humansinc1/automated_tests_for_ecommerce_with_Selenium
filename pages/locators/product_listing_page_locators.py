from selenium.webdriver.common.by import By


product_card = (By.CLASS_NAME, 'oe_product_cart')
cart_icon = (By.CSS_SELECTOR, 'a[aria-label="Shopping cart"]')
modal_title = (By.CSS_SELECTOR, 'h4.modal-title')
continue_shopping_button = (By.CSS_SELECTOR, '.modal-footer > .btn-secondary')
modal_close_button = (By.CSS_SELECTOR, '.modal-header button')
