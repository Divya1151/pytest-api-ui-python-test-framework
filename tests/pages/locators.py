from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    EMAIL = (By.ID, 'email')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '.submit_btn.ist_button.ist_button_red.sel_login')


class HomePageLocators(object):
    HOME_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Go to Home view"]')
    ADD_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Add Project"]')
    PROJECT_LIST = (By.XPATH, '//ul[@id="projects_list"]/li')
    PROJECT_NAME = (By.ID, 'edit_project_modal_field_name')
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.ist_button.ist_button_red')
    TOP_COMPLETED_HOLDER = (By.ID, 'top_completed_holder')
    VIEW_COMPLETED_TASKS = (By.CSS_SELECTOR, 'a[data-track="karma|view_completed_tasks"]')
    DELETE = (By.ID, 'menu_delete_text')
    DELETE_CONFIRM = (By.XPATH, '//*[@id="reactist-modal-box-8"]/form/footer/button[1]')


class ProjectPageLocators(object):
    ADD_BUTTON = (By.CSS_SELECTOR, '.plus_add_button')
    TASK_CONTENT = (By.CSS_SELECTOR, '.notranslate.public-DraftEditor-content')
    SCHEDULE_BUTTON = (By.CSS_SELECTOR, '.item_due_selector.icon_pill')
    DUE_DATE = (By.CSS_SELECTOR, 'button[data-action-hint="scheduler-suggestion-tomorrow"]')
    CREATE_TASK = (By.XPATH, '//div[@id="editor"]//button[contains(text(),"Add task")]')
    TASKS_LIST = (By.XPATH, '//ul[@class="items"]/li')
    EDIT_TASK = (By.CSS_SELECTOR, 'button[data-action-hint="task-edit"]')
    SAVE_TASK = (By.CSS_SELECTOR, '.ist_button.ist_button_red')
