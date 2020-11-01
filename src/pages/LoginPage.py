from src.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def auth(self):
        self.browser.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);",
                                           "access_token",
                                           "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjA0MjIwMjQ5LCJleHAiOjE2MDQ4MjUwNDl9.9ordOPNLgWN7IZGdG0jpaun-b2v-vZbFAutTuC8vlcI-UaE2BeAllpVggUssAPgpFBfHXlAf659zYWD7XILhhw")

    def open(self):
        self.browser.open("/login")
        return self

    def login_as(self, username, password):
        self.browser.element("#usernameOrEmail").set_value(username)
        self.browser.element("#password").set_value(password)
        self.browser.element(".btn").click()
