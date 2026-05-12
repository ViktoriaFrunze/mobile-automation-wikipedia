import allure
from pages.search_page import SearchPage


@allure.feature("Search")
@allure.story("Positive search")
def test_search_wikipedia(driver):
    search_page = SearchPage(driver)
    search_page.skip_onboarding()

    # 1. Enter search text (the method performs the input without internal waiting)
    search_page.start_search("Appium")

    # 2. WAIT for the search result to appear (crucial for a positive test case)
    search_page.find_visible_element(search_page.SEARCH_RESULT)

    # 3. Verify the result text
    result_text = search_page.get_first_result_text()
    assert "Appium" in result_text, \
        f"Expected 'Appium' to be in the result, but got: {result_text}"