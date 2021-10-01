import logging

from selenium.webdriver.common.by import By

from helpers.base import BaseHelpers


class PravdaLocators:
    SIDE_MENU_XPATH = ".//div[@class='top_all_sections']"
    SECTIONS_XPATH = ".//a[@href='/reports/']"
    NEWS_XPATH = ".//div[@class='article_header']"
    NEWS_TEXT_XPATH = f'{""}'
    POST_TITLE_XPATH = ".//h1[@class='post_title']"
    POST_TITLE_TEXT = f'{""}'


class StartPages(BaseHelpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)

    def open_news(self):
        self.driver.wait_and_click(By.XPATH, PravdaLocators.SIDE_MENU_XPATH)
        self.driver.wait_and_click(By.XPATH, PravdaLocators.SECTIONS_XPATH)
        self.driver.wait_and_click(By.XPATH, PravdaLocators.NEWS_XPATH)
        self.log.info("News is Opened")


class NewsPages(BaseHelpers):

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)

    def verify_title(self):
        self.wait_until_element_find(By.XPATH, PravdaLocators.POST_TITLE_XPATH)
        self.log.info("Verified Post Title")
        title = self.find_by_contains_text(PravdaLocators.POST_TITLE_TEXT)
        news_title = self.find_by_contains_text(PravdaLocators.NEWS_TEXT_XPATH)
        assert title.text == news_title.text
        self.log.info("Titles are equal")
