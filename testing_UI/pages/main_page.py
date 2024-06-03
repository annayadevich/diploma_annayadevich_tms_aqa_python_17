from selenium.webdriver.common.by import By

from testing_UI.locators.main_page_locators import BN_CATALOG
from testing_UI.pages.base_page import BasePage


class MainPage(BasePage):


    def click_bn_catalog(self):
        self.click(BN_CATALOG)
