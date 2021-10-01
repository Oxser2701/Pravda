from conftest import BaseTest
from pages.news_page import NewsPage


class TestPravda(BaseTest):

    def test_open_news(self, start_page):
        start_page.open_news()
        news = NewsPage(start_page.driver)
        news.verify_title()
