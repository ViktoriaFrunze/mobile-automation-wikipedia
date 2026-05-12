from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    # ЭТОТ МЕТОД ОБЯЗАТЕЛЬНО ДОЛЖЕН БЫТЬ ТУТ:
    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Наш новый метод для "тяжелых" случаев:
    def find_visible_element(self, locator, timeout=20):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def type(self, locator, text):
        self.find_element(locator).send_keys(text)