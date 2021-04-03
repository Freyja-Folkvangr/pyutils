import re
from os import getenv


def get_configuration(variable_name: str):
    """
    Get an environment variable. If not exists returns None
    :param variable_name:
    :return: value if etxists or None
    """
    return getenv(variable_name, None)

def is_url(url):
    # i hate regex
    # https://ihateregex.io/expr/url/
    x = re.search(r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)", url)
    if x:
        return True
    else:
        return False