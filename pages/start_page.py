import logging

from constant.start_page import StartPageConstants
from helpers.base import BaseHelpers


class StartPage(BaseHelpers):
    """Start Page"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = logging.getLogger(__name__)
        self.constant = StartPageConstants

    def open_news(self):
        self.driver.find_element_by_xpath(self.constant.SIDE_MENU_XPATH).click()
        self.driver.find_element_by_xpath(self.constant.SECTIONS_XPATH).click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.driver.find_element_by_xpath(self.constant.NEWS_XPATH).click()
        self.log.info("News is opened")
