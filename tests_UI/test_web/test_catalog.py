import time

import pytest
import allure

from tests_UI.pages.catalog_page import CatalogPage
from tests_UI.pages.item_page import ItemPage
from tests_UI.pages.main_page import MainPage
from tests_UI.pages.cart_page import CartPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


@pytest.fixture(autouse=True)
def cart_page(driver):
    yield CartPage(driver)


class TestAction:
    @allure.title("Buying things online")
    @allure.description("During the test, 1 thing is selected and added to the cart")
    @allure.suite("test_web")
    @allure.feature("Add to cart")
    @pytest.mark.smoke
    @pytest.mark.ui_testing
    def test_action(self, main_page, catalog_page, item_page, cart_page):
        time.sleep(2)
        main_page.click_bn_catalog()
        catalog_page.click_electronika()
        catalog_page.go_to_audio_headphones()
        catalog_page.select_checkbox()

        item_page.click_first_select()
        item_page.add_to_cart()
        time.sleep(2)
        item_page.go_to_cart()
        time.sleep(2)

        cart_page.check_cart_title()
        assert ("Наушники Xiaomi Redmi Buds 4 Active M2232E1 (черный, международная версия)"
                == cart_page.get_selected_hp), \
            (f"Expected header: 'Наушники Xiaomi Redmi Buds 4 Active M2232E1 (черный, международная версия)', "
             f"Actual: {cart_page.get_selected_hp}")


