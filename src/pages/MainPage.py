import allure

from src.pages.BasePage import BasePage


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("open main page")
    def open(self):
        self.browser.open("/list")
        return self

    @allure.step("check navbar")
    def brand_element(self):
        return self.browser.element(".navbar-brand")

    @allure.step("return created episode")
    def episode_name(self):
        return self.browser.element("div > ul > li > span")
