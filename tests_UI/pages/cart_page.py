from tests_UI.locators.cart_locators import SELECTED_HEADPHONES
from tests_UI.pages.base_page import BasePage


class CartPage(BasePage):


    def check_cart_title(self):
        page_title = self.driver.title
        assert page_title == "Корзина заказов onliner.by", (f"Navigation wrong. {page_title=} "
                                                            f"!= 'Корзина заказов onliner.by'")

    @property
    def get_selected_hp(self):
        self.wait_for(SELECTED_HEADPHONES)
        title = self.driver.find_element(*SELECTED_HEADPHONES)
        return title.text


