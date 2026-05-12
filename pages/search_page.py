import allure
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement


class SearchPage(BasePage):
    # Локаторы
    SKIP_BUTTON = (AppiumBy.ID, "org.wikipedia:id/fragment_onboarding_skip_button")
    SEARCH_CARD = (AppiumBy.ID, "org.wikipedia:id/search_container")
    SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia:id/search_src_text")
    SEARCH_RESULT = (AppiumBy.ID, "org.wikipedia:id/page_list_item_title")

    @allure.step("Пропуск экрана приветствия")
    def skip_onboarding(self) -> None:
        try:
            # Используем короткое ожидание, чтобы не тратить время, если кнопки нет
            self.click(self.SKIP_BUTTON)
            print("Onboarding skipped.")
        except Exception:
            print("Onboarding not found, continuing...")

    @allure.step("Поиск текста: {text}")
    def start_search(self, text: str) -> None:
        self.click(self.SEARCH_CARD)

        search_field = self.find_visible_element(self.SEARCH_INPUT)
        search_field.clear()
        search_field.send_keys(text)
        # Больше тут ничего не ждем!

    @allure.step("Получение текста первого результата")
    def get_first_result_text(self) -> str:
        element = self.find_visible_element(self.SEARCH_RESULT)
        return element.text
# Локатор сообщения о пустом результате
    EMPTY_SEARCH_MESSAGE = (AppiumBy.ID, "org.wikipedia:id/results_text")

    @allure.step("Проверка, что отображается сообщение 'Результатов не найдено'")
    def get_empty_search_message(self):
        # Ждем появления сообщения и возвращаем его текст
        return self.find_visible_element(self.EMPTY_SEARCH_MESSAGE).text
