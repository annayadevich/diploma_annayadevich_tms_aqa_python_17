import time

from selenium.webdriver.common.by import By

from tests_UI.locators.main_page_locators import BN_CATALOG
from tests_UI.pages.base_page import BasePage
import allure

class MainPage(BasePage):

    def click_bn_catalog(self):
        self.click(BN_CATALOG)
        with allure.step("Step 1: Click to the 'Catalog' button"):
            time.sleep(1)



