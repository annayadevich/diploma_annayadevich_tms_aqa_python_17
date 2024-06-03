from selenium.webdriver.common.by import By


BN_FIRST_ADD_TO_CART = By.XPATH, '(//a[contains(@class, "product-aside__button_cart")])[1]'
BN_GO_TO_CART_PRODUCT_REC = By.XPATH, '//div[@class="product-recommended__sidebar"]//a[@href="https://cart.onliner.by"]'

TXT_FIRST_PRICE = By.XPATH, '//div[@class="offers-description__price offers-description__price_primary"]'

BOX_YO = By.XPATH, '//div[@class="dropdown-style__checkbox-sign"][contains(text(), "ЙО!")]'

SEL_MANUF = By.XPATH, '//*[contains(text(), "Наушники Xiaomi Redmi Buds 4 Active M2232E1 ")]'

