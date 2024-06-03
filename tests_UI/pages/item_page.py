from tests_UI.locators.item_page_locators import BN_FIRST_ADD_TO_CART, BN_GO_TO_CART_PRODUCT_REC, SELECTED_PR
from tests_UI.pages.base_page import BasePage
import allure
import time

class ItemPage(BasePage):

    def add_to_cart(self):
        self.click(BN_FIRST_ADD_TO_CART)
        with allure.step("Step 7: Click to the 'Add to cart' buttons"):
            time.sleep(1)

    def go_to_cart(self):
        self.click(BN_GO_TO_CART_PRODUCT_REC)
        with allure.step("Step 8: Click to the 'Go to cart' buttons"):
            time.sleep(1)

    def click_first_select(self):
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.click(SELECTED_PR)
        with allure.step("Step 6: Select first item"):
            time.sleep(1)


