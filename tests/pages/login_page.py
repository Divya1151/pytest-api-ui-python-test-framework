

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tests.pages.locators import LoginPageLocators


class LoginPage(object):

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        email = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(LoginPageLocators.EMAIL))
        email.send_keys(username)

    def set_password(self, pwd):
        password = WebDriverWait(self.driver, 10).until(ec.presence_of_element_located(LoginPageLocators.PASSWORD))
        password.send_keys(pwd)

    def submit_to_login(self):
        login = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))
        login.submit()

    def login_into_todoist(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.submit_to_login()
