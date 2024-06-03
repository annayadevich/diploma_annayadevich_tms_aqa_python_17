from testing_UI.locators.catalog_page_locators import BN_ONLINER_PRIME, BN_ZOO, BN_ZOO_COSMETICS
from testing_UI.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains


class CatalogPage(BasePage):

    @property
    def zoo(self):
        return self.wait_for(BN_ZOO)

    @property
    def zoo_cosmetics(self):
        return self.wait_for(BN_ZOO_COSMETICS)

    def click_onliner_prime(self):
        self.click(BN_ONLINER_PRIME)

    def go_to_pet_cosmetics(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.zoo).perform()
        action.move_to_element(self.zoo_cosmetics).perform()
        action.click().perform()