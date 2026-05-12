import allure
from pages.search_page import SearchPage


@allure.feature("Search")
@allure.story("Negative search")
def test_search_with_special_symbols(driver):
    search_page = SearchPage(driver)
    search_page.skip_onboarding()

    # 1. Вводим символы
    search_page.start_search("!!!@@@###")

    # 2. Ждем и проверяем сообщение о пустом результате
    message = search_page.get_empty_search_message()

    assert "No results" in message or "найдено" in message.lower(), \
        f"Ожидали текст об отсутствии результатов, а получили: {message}"
