
from hamcrest import *


def test_ui_add_new_task(setup, context):
    context['project_id'] = context['home_object'].create_project()
    context['home_object'].go_to_project(context['project_id'])
    context['project_object'].create_task()
    task_id = context['project_object'].get_task_id()
    assert_that(task_id, not_none(), "Task is not created successfully")
    assert_that(context['project_object'].get_actual_due_date(task_id), equal_to("Tomorrow"))


