import time

import pytest

from testing_UI.pages.catalog_page import CatalogPage
from testing_UI.pages.item_page import ItemPage
from testing_UI.pages.main_page import MainPage


@pytest.fixture(autouse=True)
def main_page(driver):
    yield MainPage(driver)


@pytest.fixture(autouse=True)
def catalog_page(driver):
    yield CatalogPage(driver)


@pytest.fixture(autouse=True)
def item_page(driver):
    yield ItemPage(driver)


class TestAction:

    def test_action(self, main_page, catalog_page, item_page):
        time.sleep(2)
        main_page.click_bn_catalog()
        catalog_page.click_electronika()
        time.sleep(2)
        catalog_page.go_to_audio_headphones()
        time.sleep(2)
        catalog_page.select_checkbox()
        time.sleep(2)
        item_page.click_first_select()
        time.sleep(2)

        # item_page.click_yo()
        # item_page.check_yo_clicked()
        # time.sleep(10)
