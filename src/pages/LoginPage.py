import allure

from src.pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    @allure.step("authorization with cookie")
    def auth(self):
        self.browser.driver.execute_script("window.localStorage.setItem(arguments[0], arguments[1]);",
                                           "access_token",
                                           "eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwiaXNBZG1pbiI6dHJ1ZSwibmFtZSI6ImFkbWluIiwiaWF0IjoxNjA0OTQxNjEzLCJleHAiOjE2MDU1NDY0MTN9.OLFlhIsTjKA4ogkG1-VytK9fdwU41zn1BXnpXcwKggUCm13ivOcQanGb3Z2irHFmqmCQugj3FMrUWr6yr5SEQg")

    @allure.step("open login page")
    def open(self):
        self.browser.open("/login")
        return self

    @allure.step("enter username and password")
    def login_as(self, username, password):
        self.browser.element("#usernameOrEmail").set_value(username)
        self.browser.element("#password").set_value(password)
        self.browser.element(".btn").click()
