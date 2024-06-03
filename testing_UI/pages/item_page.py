from testing_UI.locators.item_page_locators import BN_FIRST_ADD_TO_CART, BN_GO_TO_CART_PRODUCT_REC, \
    TXT_FIRST_PRICE, BOX_YO, SEL_MANUF
from testing_UI.pages.base_page import BasePage


class ItemPage(BasePage):

    def add_to_cart(self):
        self.click(BN_FIRST_ADD_TO_CART)

    def go_to_cart(self):
        self.click(BN_GO_TO_CART_PRODUCT_REC)

    def get_first_price(self):
        return self.text(TXT_FIRST_PRICE)

    def click_first_select(self):
        self.driver.execute_script("window.scrollTo(0, 200);")
        self.click(SEL_MANUF)

    def click_yo(self):
        self.click(BOX_YO)

    def check_yo_clicked(self):
        self.wait_for(BOX_YO).is_selected()
