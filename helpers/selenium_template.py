# movies/utils/selenium_template

from selenium import webdriver
from fake_useragent import UserAgent
from bs4 import BeautifulSoup as bs
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from time import sleep
from pathlib import Path
import pandas as pd
from selenium.webdriver.common.by import By
from helpers.helpers import save_text


def get_soup(url: str, save_: bool, filename: str) -> bs:
    path = Path(filename)
    if path.exists():
        soup = use_file(path)
    else:
        soup = use_selenium(url, save_)
    return soup


def use_file(path: str) -> bs:
    with open(path, 'r') as f:
        text_ = f.read()
        soup = bs(text_, 'html.parser')
        print('run from file')
    return soup

def use_selenium(url_, save_):
    options = Options()
    options.add_argument('--headless')
    ua = UserAgent()
    user_agent = ua.random
    options.add_argument(f'user-agent:{user_agent}')
    with webdriver.Firefox(service=Service('/Users/geckodriver'), options=options) as driver:
        driver.get(url_)
        sleep(2)
        driver.maximize_window()
        driver.save_screenshot("data/homepage.png")
        soup = bs(driver.page_source, 'html.parser')
        if save_:
            save_text(driver.page_source)
        print("run using selenium")
    
    return soup