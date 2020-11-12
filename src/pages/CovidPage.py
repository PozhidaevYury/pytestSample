from src.pages.BasePage import BasePage


class CovidPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.open("https://service.nalog.ru/covid19/")
        return self

    def search_by_inn(self, inn):
        [self.browser.element("#query").send_keys(x) for x in inn]
        self.browser.element(".nu-button").click()
        self.browser.element("div.covid-result:nth-child(1) > a:nth-child(1)").click()
