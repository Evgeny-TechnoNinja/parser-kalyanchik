from utils.write_logs import logs_init  # noqa
from utils import get_proxies  # noqa
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
    else:
        status["success"] = True
        return status
