import allure
from pages.search_page import SearchPage


@allure.feature("Search")
@allure.story("Positive search")
def test_search_wikipedia(driver):
    search_page = SearchPage(driver)
    search_page.skip_onboarding()

    # 1. Просто вводим текст (теперь метод не ждет результат внутри себя)
    search_page.start_search("Appium")

    # 2. ЖДЕМ появления результата (так как это позитивный тест)
    search_page.find_visible_element(search_page.SEARCH_RESULT)

    # 3. Проверяем текст
    result_text = search_page.get_first_result_text()
    assert "Appium" in result_text