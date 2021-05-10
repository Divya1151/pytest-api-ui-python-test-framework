import json
from enum import Enum

BASE_URL = "https://api.todoist.com/sync/v8/sync"
TOKEN = "461db91702d04169619f2fd82dae148742be6186"


class Type(json.JSONEncoder):
    ITEM_ADD = "item_add"
    ITEM_UPDATE = "item_update"
    ITEM_COMPLETE = "item_complete"
