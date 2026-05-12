import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class SearchPage(BasePage):
    # Locators
    SKIP_BUTTON = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    SEARCH_CARD = (AppiumBy.ID, "org.wikipedia:id/search_container")
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    SEARCH_RESULT = (AppiumBy.ID, "org.wikipedia:id/page_list_item_title")
    # Empty search message locator
    EMPTY_SEARCH_MESSAGE = (AppiumBy.ID, "org.wikipedia:id/results_text")

    @allure.step("Skip onboarding screen")
    def skip_onboarding(self) -> None:
        try:
            # Use a short wait to avoid wasting time if the button is not present
            self.click(self.SKIP_BUTTON)
            print("Onboarding skipped.")
        except Exception:
            print("Onboarding not found, continuing...")

    @allure.step("Start search for text: {text}")
    def start_search(self, text: str) -> None:
        self.click(self.SEARCH_CARD)

        search_field = self.find_visible_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        # No more waiting required here!

    @allure.step("Get the text of the first search result")
    def get_first_result_text(self) -> str:
        element = self.find_visible_element(self.SEARCH_RESULT)
        return element.text

    @allure.step("Verify 'No results found' message is displayed")
    def get_empty_search_message(self) -> str:
        # Wait for the message to appear and return its text
        return self.find_visible_element(self.EMPTY_SEARCH_MESSAGE).text
