import time

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from tests.pages.locators import HomePageLocators
from selenium.webdriver import ActionChains

class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)


    def go_to_home_view(self):
        home_button = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(HomePageLocators.HOME_BUTTON))
        home_button.click()

    def add_project(self):
        add_project = self.driver.find_element(*HomePageLocators.ADD_BUTTON)
        add_project.click()

    def get_project_id(self):
        project_list = self.driver.find_elements(*HomePageLocators.PROJECT_LIST)
        for project in project_list:
            project_id = project.get_attribute('data-id')
            if project_id in self.driver.current_url:
                return project_id
        else:
            print("Project is not created successfully")

    def create_project(self):
        self.add_project()
        project_name = self.driver.find_element(*HomePageLocators.PROJECT_NAME)
        project_name.send_keys("Divya_Project")
        submit_project = self.driver.find_element(*HomePageLocators.SUBMIT_BUTTON)
        submit_project.click()
        time.sleep(3)
        return self.get_project_id()

    def go_to_project(self, project_id):
        self.go_to_home_view()
        project = self.driver.find_element_by_css_selector(f'li[data-id="{project_id}"]')
        project.click()

    def navigate_to_view_all_completed_tasks(self):
        self.driver.find_element(*HomePageLocators.TOP_COMPLETED_HOLDER).click()
        self.driver.find_element(*HomePageLocators.VIEW_COMPLETED_TASKS).click()

    def delete_project(self, project_id):
        self.go_to_home_view()
        time.sleep(1)
        self.action.context_click(self.driver.find_element_by_css_selector(f'li[data-id="{project_id}"]')).perform()
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(HomePageLocators.DELETE)).click()
        time.sleep(1)
        delete_confirm = self.driver.find_element(*HomePageLocators.DELETE_CONFIRM)
        time.sleep(100)
        delete_confirm.submit()

