from typing import Callable
from utils.write_logs import logs_init  # noqa
from utils import get_proxies, get_suitable_proxy, get_user_agents, get_category_name, get_pagination_data  # noqa
from utils import get_links_products, weed_out_links, get_goods  # noqa
from settings_ui import DIALOGUE  # noqa
from random import choice
from config import DONOR_URL  # noqa
import multiprocessing
import pickle


def parser():
    def multiprocessing_run(func: Callable[[list], list], amount: int, serial_data: list) -> list:
        with multiprocessing.Pool(amount) as p:
            result_data: list = []
            for result in p.imap_unordered(func, iterable=serial_data):
                result_data.append(*result)
        return result_data

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
    if not isinstance(PROXY, dict):
        status["msg"] = PROXY + DIALOGUE["parsing_not_possible"]
        return status
    USER_AGENTS = get_user_agents(10, PROXY)
    category_names = get_category_name(DONOR_URL, PROXY, choice(USER_AGENTS))
    AMOUNT_CATEGORY = len(category_names)
    selected_user_agents = [choice(USER_AGENTS) for _ in range(AMOUNT_CATEGORY)]
    selected_proxies = [get_suitable_proxy(PROXIES_DATA) for _ in range(AMOUNT_CATEGORY)]
    target_url = [DONOR_URL for _ in range(len(DONOR_URL))]
    iterable = [*zip(selected_user_agents, selected_proxies, category_names, target_url)]
    pagination_data = multiprocessing_run(get_pagination_data, AMOUNT_CATEGORY, iterable)
    iterable = [*zip(selected_user_agents, selected_proxies, pagination_data)]
    links_products = multiprocessing_run(get_links_products, AMOUNT_CATEGORY, iterable)
    links_products[:] = weed_out_links(links_products)
    # === for dev
    pickle.dump(links_products, open("links", "wb"))
    # links = pickle.load(open("links", "rb"))
    # ===
    iterable = [*zip(selected_user_agents, selected_proxies, links_products)]  # links_products
    goods = multiprocessing_run(get_goods, AMOUNT_CATEGORY, iterable)
    # # == for dev
    pickle.dump(goods, open("goods", "wb"))
    # goods = pickle.load(open("goods", "rb"))
    # ===
    if goods:
        status["data"], status["msg"], status["success"] = goods, DIALOGUE["data_received"], True
        return status
    else:
        status["msg"] = DIALOGUE["data_not_received"]
        return status
