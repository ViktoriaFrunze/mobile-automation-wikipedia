import pytest
import allure
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver():
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'apps', 'wikipedia.apk'))

    options = UiAutomator2Options()
    options.platform_name = 'Android'
    options.automation_name = 'UiAutomator2'
    options.device_name = 'AndroidEmulator'
    options.app = app_path
    options.app_wait_activity = "org.wikipedia.*"
    options.no_reset = False

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver_instance = item.funcargs.get('driver')
        if driver_instance:
            try:
                allure.attach(
                    driver_instance.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Failed to take screenshot: {e}")