from abc import abstractmethod

from playwright import sync_playwright
from selene import Config, Browser
from selene.core.entity import SeleneElement
from selenium import webdriver

from src.element import PlaywrightElement


class Engine(object):

    @abstractmethod
    def open(self, url):
        raise NotImplementedError

    @abstractmethod
    def element(self, locator):
        raise NotImplementedError

    @abstractmethod
    def close(self):
        raise NotImplementedError


class SeleniumEngine(Engine):

    def __init__(self, config):
        if not config:
            pass
        config = Config(
            driver=webdriver.Chrome(),
            base_url=config.base_url,
            timeout=config.timeout,
            window_height=config.window_height,
            window_width=config.window_width
        )
        self.browser = Browser(config)

    def open(self, url):
        self.browser.open(url)

    def element(self, locator):
        return SeleneElement(self.browser.element(locator))

    def close(self):
        return self.browser.close_current_tab()


class PlaywrightEngine(Engine):

    def __init__(self, config):
        self.p = sync_playwright().start()
        self.browser = self.p.chromium.launch(headless=False)

        cfg = {
            "viewport": {"width": config.window_width, "height": config.window_height}
        }

        context = self.browser.newContext(**cfg)
        self.page = context.newPage()
        self.base_url = config.base_url

    def open(self, url):
        self.page.goto(self.base_url + url)

    def element(self, locator):
        return PlaywrightElement(self.page, locator)

    def close(self):
        self.page.close()
        self.browser.close()
        self.p.stop()
