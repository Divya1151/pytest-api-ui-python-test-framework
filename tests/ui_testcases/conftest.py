import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from tests.pages.home_page import HomePage
from tests.pages.login_page import LoginPage
from tests.pages.project_page import ProjectPage


@pytest.fixture
def chrome_driver(context):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://chrome.todoist.com/app/today")
    yield driver
    # context['home_object'].delete_project(context['project_id'])
    driver.quit()


@pytest.fixture
def context():
    return {}


@pytest.fixture
def setup(chrome_driver, context):
    context['login_object'] = LoginPage(chrome_driver)
    context['login_object'].login_into_todoist("dsingla3103@gmail.com", "Divya123")
    context['home_object'] = HomePage(chrome_driver)
    context['project_object'] = ProjectPage(chrome_driver)
