from tests_UI.locators.catalog_page_locators import BN_ELECTRONIKA, BN_AUDIO, BN_HEADPHONES, CHECKBOX_GENERAL_PRIME
from tests_UI.pages.base_page import BasePage
from selenium.webdriver.common.action_chains import ActionChains
import allure
import time

class CatalogPage(BasePage):

    @property
    def audio(self):
        return self.wait_for(BN_AUDIO)

    @property
    def audio_headphones(self):
        return self.wait_for(BN_HEADPHONES)

    @property
    def checkbox_general(self):
        return self.wait_for(CHECKBOX_GENERAL_PRIME)

    def click_electronika(self):
        self.click(BN_ELECTRONIKA)

    @property
    def checkbox_general_1(self):
        return self.wait_for(CHECKBOX_GENERAL_PRIME)

    def select_checkbox(self):
        self.click(CHECKBOX_GENERAL_PRIME)

    def go_to_audio_headphones(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.audio).perform()
        action.move_to_element(self.audio_headphones).perform()
        action.click().perform()
        with allure.step("Step 2: Select 'Electronika' section"):
            time.sleep(1)
        with allure.step("Step 3: Select 'Audio' line"):
            time.sleep(1)
        with allure.step("Step 4: Click to the 'HEADPHONES' buttons"):
            time.sleep(1)
        with allure.step("Step 5: Select checkbox 'GENERAL_PRIME'"):
            time.sleep(1)


