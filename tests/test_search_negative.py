import allure
from pages.search_page import SearchPage

@allure.feature("Search")
@allure.story("Negative search")
def test_search_with_special_symbols(driver):
    search_page = SearchPage(driver)
    search_page.skip_onboarding()

    # 1. Input special characters
    search_page.start_search("!!!@@@###")

    # 2. Wait for and verify the empty search result message
    message = search_page.get_empty_search_message()

    # Updated assertion to be purely in English
    assert "No results" in message, \
        f"Expected 'No results' message, but got: {message}"
