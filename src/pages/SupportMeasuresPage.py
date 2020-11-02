from src.pages.BasePage import BasePage


class SupportMeasuresPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def switch_to_page(self):
        self.browser.switch_to_next_tab()
        return self

    def show_support_measures(self):
        self.browser \
            .element("#t11 > div.info-block__title.js-info-button > h5") \
            .click()
        return self

    def info_block(self):
        return self.browser.element("#t11 > div.info-block__hidden.js-info-block > p > b")
