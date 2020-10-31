from src.pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def brand_element(self):
        return self.browser.element(".navbar-brand")
