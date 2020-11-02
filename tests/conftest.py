import configparser
import os
import sys

import pytest
from faker import Faker
from selene import Browser, Config
from selenium import webdriver
from src.app import Application


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
        return read_ini()[env_name]
    except:
        raise KeyError(f"Wrong command {env_name}")


@pytest.fixture(scope="session")
def browser(request):
    config = get_config(request)
    browser = Browser(
        Config(
            driver=webdriver.Chrome(),
            base_url=config['job_url'],
            timeout=4,
            window_width=int(config['window_width']),
            window_height=int(config['window_height'])
        )
    )

    yield browser
    browser.close_current_tab()


@pytest.fixture(scope="session")
def app(browser):
    return Application(browser)


@pytest.fixture(scope="session")
def auth_app(app):
    app \
        .login_page() \
        .open() \
        .auth()
    return app


@pytest.fixture(scope="session")
def faker():
    return Faker()
