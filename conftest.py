import logging

import pytest as pytest
from selenium import webdriver

from constant.base import BaseConstants
from pages.start_page import StartPage


class BaseTest:
    log = logging.getLogger(__name__)


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope="function")
def start_page(driver):
    driver.get(BaseConstants.START_PAGE)
    return StartPage(driver)
