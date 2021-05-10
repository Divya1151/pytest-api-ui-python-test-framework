import uuid

from selenium.webdriver.common.keys import Keys


def generate_unique_id():
    return str(uuid.uuid4())


def clear_text(element):
    element.send_keys(Keys.COMMAND + 'a')
    element.send_keys(Keys.DELETE)
