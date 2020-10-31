import configparser
import os
import sys

import pytest
from selene import Browser, Config
from selenium import webdriver
from src.app import Application


def get_config():
    config_file_name = os.environ.get("config-file", "project.config.ini")
    root_path = os.path.join(sys.path[0], config_file_name)
    parser = configparser.ConfigParser()
    parser.read(root_path)
    return parser


@pytest.fixture(scope="session")
def browser():
    config = get_config()['local']
    browser = Browser(
        Config(
            driver=webdriver.Chrome(),
            base_url=config['base_url'],
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
