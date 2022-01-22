from utils.write_logs import logs_init  # noqa
from utils import get_proxies, get_suitable_proxy, get_user_agents  # noqa
from settings_ui import DIALOGUE  # noqa


def parser():
    status = {
        "success": False,
        "msg": "",
        "data": None
    }
    logs_init()
    PROXIES_DATA = get_proxies()
    if not isinstance(PROXIES_DATA, list):
        status["msg"] = PROXIES_DATA + DIALOGUE["parsing_not_possible"]
        return status
    PROXY = get_suitable_proxy(PROXIES_DATA)
    print("PROXY", PROXY)
    if not isinstance(PROXY, dict):
        status["msg"] = PROXY + DIALOGUE["parsing_not_possible"]
        return status
    USER_AGENTS = get_user_agents(10)
    status["success"] = True
    return status
