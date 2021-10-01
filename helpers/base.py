import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseHelpers:
    """Store base helpers for Web testing"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=5)

    def wait_until_element_find(self, locator_type, locator):
        """Wait until element find and return it"""
        self.wait.until(EC.presence_of_element_located((locator_type, locator)))
        return self.driver.find_element(by=locator_type, value=locator)

    def find_by_contains_text(self, text, element_tag="*"):
        """Find element using XPATH contains function by text"""
        return self.wait_until_element_find(By.XPATH, f".//{element_tag}[contains(text(), '{text}')]")
