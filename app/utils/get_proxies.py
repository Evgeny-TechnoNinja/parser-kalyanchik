from typing import Union, List
from config import PROXIES, PROXY_LOGIN, PROXY_PASSWORD  # noqa
from settings_ui import DIALOGUE  # noqa


def get_proxies() -> Union[str, List[str]]:
    """
    Gets the proxy, login and passwords from the configuration file,
    if the data is not received, it will return a notification string about the lack of data.
    If the data is all obtained from a configuration file,
    collects a list of required configuration strings to use the proxy
    :return: Warning string or list of proxy strings
    """

    def notice(name_key: str) -> str:
        return DIALOGUE["proxy_data"]["sentence"].format(DIALOGUE["proxy_data"][name_key])

    if len(PROXIES[0]) == 0:
        return notice("proxy")
    if not PROXY_LOGIN:
        return notice("login")
    if not PROXY_PASSWORD:
        return notice("password")
    else:
        return [f"{PROXY_LOGIN}:{PROXY_PASSWORD}@{proxy}" for proxy in PROXIES]
