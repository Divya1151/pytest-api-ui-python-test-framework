import requests
from hamcrest import *

from tests.data import payload
from tests.util.util import generate_unique_id
from tests.util.constants import *


def test_rename_task():
    temp_id = generate_unique_id()
    add_response = requests.post(BASE_URL, json=payload.Payload.add_new_task_payload(temp_id))
    task_id = add_response.json()["temp_id_mapping"][temp_id]
    rename_response = requests.post(BASE_URL, json=payload.Payload.rename_task_payload(task_id))
    assert_that(rename_response.status_code, equal_to(200))
    assert_that(rename_response.json()["sync_token"], not_none())
    assert_that(rename_response.json()["full_sync"], equal_to(True))

