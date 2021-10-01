from PageObjects.page_objects import StartPages, NewsPages


def test_pravda(start_page):
    StartPages(start_page).open_news()
    NewsPages(start_page.driver).verify_title()
