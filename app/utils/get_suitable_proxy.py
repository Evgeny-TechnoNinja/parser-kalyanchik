from typing import Union, Dict
from config import PROXIES_TEST_OPTIONS  # noqa
from random import choice
from settings_ui import DIALOGUE  # noqa
import requests


def get_suitable_proxy(proxies) -> Union[str, Dict[str, str]]:
    """
    Takes a list of proxies prepared for work and checks them for suitability.
    From the list of proxies is taken randomly. If the proxy is valid,
    then the function will return it as a dictionary. If all proxies are unusable,
    a warning line will be returned
    :param proxies: List of previously prepared proxies in the required format
    :return: When working, the proxy will return a dictionary with the proxy ready to work in requests,
    otherwise it will return a string with a warning
    """
    connection_attempts: int = len(proxies) * PROXIES_TEST_OPTIONS["multiplication_attempts"]
    random_proxy: str = choice(proxies)
    blank_proxies = {
        "http": "http://{}".format(random_proxy),
        "https": "http://{}".format(random_proxy)
    }

    def check() -> bool:
        try:
            requests.get(PROXIES_TEST_OPTIONS["url"], proxies=blank_proxies, timeout=PROXIES_TEST_OPTIONS["timeout"])
            return True
        except Exception as error:
            return False

    while True:
        if not check():
            random_proxy: str = choice(proxies)
            blank_proxies['http'] = 'http://{}'.format(random_proxy)
            blank_proxies['https'] = 'http://{}'.format(random_proxy)
            connection_attempts -= 1
        else:
            break

        if connection_attempts == 0:
            return DIALOGUE['bad_connect']
    return blank_proxies
