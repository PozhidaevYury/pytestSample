from selene.core.entity import SeleneElement

from src.pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.open("/list")
        return self

    def brand_element(self):
        return self.browser.element(".navbar-brand")

    def episode_name(self) -> SeleneElement:
        return self.browser.element("div > ul > li > span")
