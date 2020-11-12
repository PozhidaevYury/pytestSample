import configparser
import os
import sys

import pytest
from faker import Faker
from selenium import webdriver
from src.app import Application
from src.browser import Browser
from src.configuration import Configuration
from src.engine import PlaywrightEngine, SeleniumEngine


def pytest_addoption(parser):
    parser.addoption(
        "--env", action="store", default="local", help="env variable name"
    )


def read_ini():
    config_file_name = os.environ.get("config-file", "project.config.ini")
    root_path = os.path.join(sys.path[0], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


def get_config(request):
    env_name = request.config.getoption("--env")
    try:
        config = read_ini()[env_name]
        return Configuration(
            base_url=config['base_url'],
            timeout=4,
            window_width=int(config['window_width']),
            window_height=int(config['window_height'])
        )
    except:
        raise KeyError(f"Wrong command {env_name}")


def get_driver(env):
    if env == "local":
        return webdriver.Chrome()
    else:
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "86.0",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }
        return webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub",
                                desired_capabilities=capabilities)


@pytest.fixture(scope="session")
def browser(request):
    config = get_config(request)

    browser = Browser(
        #   Config(
        #      driver=get_driver(env_name),
        #        base_url=config['base_url'],
        #        timeout=4,
        #        window_width=int(config['window_width']),
        #        window_height=int(config['window_height'])
        #    )
        # )

        # SeleniumEngine(config)
        PlaywrightEngine(config)
    )

    yield browser
    browser.close()


@pytest.fixture(scope="session")
def app(browser):
    yield Application(browser)


@pytest.fixture(scope="session")
def auth_app(app):
    app \
        .login_page() \
        .open() \
        .auth_playwrigth()
    return app


@pytest.fixture(scope="session")
def faker():
    return Faker()
