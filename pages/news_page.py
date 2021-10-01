import logging

from constant.news_page import NewsPageConstants
from constant.start_page import StartPageConstants
from helpers.base import BaseHelpers


class NewsPage(BaseHelpers):
    """"News Page"""

    def __init__(self, driver):
        super(NewsPage, self).__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constant = NewsPageConstants

    def verify_title(self):
        self.driver.find_element_by_xpath(self.constant.POST_TITLE_XPATH)
        self.log.info("Verified Post Title")
        title = self.find_by_contains_text(self.constant.POST_TITLE_TEXT)
        news_title = self.find_by_contains_text(StartPageConstants.NEWS_TEXT_XPATH)
        assert title.text == news_title.text
        self.log.info("Titles are equal")
