import time

from selenium.webdriver import ActionChains

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from tests.pages.locators import ProjectPageLocators
from tests.pages.home_page import HomePage
from tests.util import util


class ProjectPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def add_task(self):
        add_button = self.driver.find_element(*ProjectPageLocators.ADD_BUTTON)
        add_button.click()

    def add_task_content(self):
        task_content = self.driver.find_element(*ProjectPageLocators.TASK_CONTENT)
        task_content.send_keys("New Task")

    def rename_task_content(self):
        task_content = self.driver.find_element(*ProjectPageLocators.TASK_CONTENT)
        util.clear_text(task_content)
        self.driver.find_element(*ProjectPageLocators.TASK_CONTENT).send_keys("Rename Task")
        WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(ProjectPageLocators.SAVE_TASK)).click()
        # self.driver.find_element(*ProjectPageLocators.SAVE_TASK).click()

    def select_due_date(self):
        schedule = self.driver.find_element(*ProjectPageLocators.SCHEDULE_BUTTON)
        schedule.click()
        due_date = self.driver.find_element(*ProjectPageLocators.DUE_DATE)
        due_date.click()
        time.sleep(2)

    def create_task(self):
        self.add_task()
        self.add_task_content()
        self.select_due_date()
        create_task = self.driver.find_element(*ProjectPageLocators.SAVE_TASK)
        create_task.click()

    def get_task_id(self):
        time.sleep(2)
        tasks_list = WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(ProjectPageLocators.TASKS_LIST))
        for task in tasks_list:
            task_id = task.get_attribute("data-selection-id")
            task_name = self.driver.find_element_by_xpath(f'//*[@id="task-{task_id}-content"]')
            if task_name.text in "New Task":
                return task_id
        else:
            print("Task is not created successfully")

    def get_actual_due_date(self, task_id):
        return self.driver.find_element_by_xpath(f'//*[@id="task-{task_id}"]//button[@class="due_date_controls"]').text

    def complete_task(self, task_id):
        self.driver.find_element_by_css_selector(f'button[aria-describedby="task-{task_id}-content"]').click()

    def is_task_completed(self, task_id):
        time.sleep(1)
        tasks_list = WebDriverWait(self.driver, 10).until(
            ec.presence_of_all_elements_located(ProjectPageLocators.TASKS_LIST))
        for task in tasks_list:
            if "controller actions task_actions full_width_actions" in task.get_attribute("class"):
                return True
            elif task_id in task.get_attribute("data-selection-id"):
                return False

    def rename_task(self, task_id):
        self.action.move_to_element(self.driver.find_element_by_xpath(f'//li[@data-selection-id="{task_id}"]')).perform()
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(ProjectPageLocators.EDIT_TASK)).click()
        self.rename_task_content()

    def is_task_renamed(self, task_id):
        if "Rename Task" in self.driver.find_element_by_xpath(f'//*[@id="task-{task_id}-content"]').text:
            return True
        else:
            return False


