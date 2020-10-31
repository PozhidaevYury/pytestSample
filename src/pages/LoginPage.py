from src.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.open("/login")
        return self

    def login_as(self, username, password):
        self.browser.element("#usernameOrEmail").set_value(username)
        self.browser.element("#password").set_value(password)
        self.browser.element(".btn").click()
