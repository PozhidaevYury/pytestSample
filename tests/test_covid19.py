import pytest
from selene import Browser, Config, command
from selene.support.conditions import have
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    browser = Browser(
        Config(
            driver=webdriver.Chrome(),
            timeout=4,
            window_width=1920,
            window_height=1080
        )
    )

    yield browser
    browser.close_current_tab()


def test_covid19(browser):
    browser.open("https://service.nalog.ru/covid19/")
    [browser.element("#query").send_keys(x) for x in "773466902356"]
    browser.element(".nu-button").click()

    browser.element("div.covid-result:nth-child(1) > a:nth-child(1)").click()

    browser.switch_to_next_tab()
    browser \
        .element("#t1") \
        .should(have.exact_text("МЕРЫ ПОДДЕРЖКИ ДЛЯ ОРГАНИЗАЦИЙ И ИНДИВИДУАЛЬНЫХ ПРЕДПРИНИМАТЕЛЕЙ"))

    browser.driver.execute_script("window.scrollTo(0, Y)")
    
    browser \
        .element("#t11 > div.info-block__title.js-info-button") \
        .click() \
        .should(have.exact_text("До 30 июня включительно:"))

    browser.driver.back()
    browser.switch_to_previous_tab()

    browser \
        .element("div.covid-result:nth-child(2) > a:nth-child(1)") \
        .should(have.exact_text("Продлены сроки сдачи отчетности"))
