import requests
from hamcrest import *

from tests.util.util import generate_unique_id
from tests.data import payload
from tests.util.constants import *


def test_add_new_task():
    temp_id = generate_unique_id()
    response = requests.post(BASE_URL, json=payload.Payload.add_new_task_payload(temp_id))
    assert_that(response.json()["full_sync"], equal_to(True))
    assert_that(response.json()["sync_token"], not_none())
    assert_that(list(response.json()["temp_id_mapping"].keys())[0], equal_to(temp_id))
    assert_that(response.status_code, equal_to(200), "Task is not created successfully")
    assert_that(response.json()["temp_id_mapping"][temp_id], not_none())




