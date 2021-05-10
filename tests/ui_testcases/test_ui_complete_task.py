
from hamcrest import *


def test_complete_task(setup, context):
    context['project_id'] = context['home_object'].create_project()
    context['home_object'].go_to_project(context['project_id'])
    context['project_object'].create_task()
    task_id = context['project_object'].get_task_id()
    context['project_object'].complete_task(task_id)
    assert_that(context['project_object'].is_task_completed(task_id), equal_to(True))
