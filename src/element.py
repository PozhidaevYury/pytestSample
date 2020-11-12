from selene.support.conditions import have


class PlaywrightElement(object):

    def __init__(self, page, locator):
        self.page = page
        self.locator = locator

    def click(self):
        self.page.click(self.locator)

    def send_keys(self, text):
        self.page.type(selector=self.locator, text=text)

    def should(self, text):
        assert self.page.innerText(self.locator) == text


class SeleneElement(object):

    def __init__(self, element):
        self.element = element

    def click(self):
        self.element.click()

    def should(self, condition):
        self.element.should(have.exact_text(condition.expected_text))
