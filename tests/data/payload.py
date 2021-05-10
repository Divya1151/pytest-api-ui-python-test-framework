from tests.util.util import generate_unique_id
from tests.util.constants import *


class Payload:

    @staticmethod
    def add_new_task_payload(temp_id):
        return {
            "token": TOKEN,
            "commands": [
                {
                    "type": Type.ITEM_ADD,
                    "temp_id": temp_id,
                    "uuid": generate_unique_id(),
                    "args": {
                        "content": "TaskNewDivya5",
                        "due": {
                            "date": "2021-03-22"}
                    }
                }
            ]
        }

    @staticmethod
    def rename_task_payload(task_id):
        return {
            "token": TOKEN,
            "commands": [
                {
                    "type": Type.ITEM_UPDATE,
                    "uuid": generate_unique_id(),
                    "args": {
                        "id": task_id,
                        "content": "RenameTask"
                    }
                }
            ]
        }

    @staticmethod
    def complete_task(task_id):
        return {
            "token": TOKEN,
            "type": Type.ITEM_COMPLETE,
            "uuid": generate_unique_id(),
            "args": {
                "id": task_id
            }
        }
