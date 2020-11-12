from src.browser import Browser
from src.pages.CovidPage import CovidPage
from src.pages.LoginPage import LoginPage
from src.pages.MainPage import MainPage


class Application(object):

    def __init__(self, browser: Browser):
        self.browser = browser

    def login_page(self):
        return LoginPage(self.browser)

    def main_page(self):
        return MainPage(self.browser)

    def covid_page(self):
        return CovidPage(self.browser)
