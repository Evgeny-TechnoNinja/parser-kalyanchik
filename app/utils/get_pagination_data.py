from bs4 import BeautifulSoup  # type: ignore
from .get_document import get_document
from config import MARKUP_ANALYZER, SLEEP_PARAMETERS  # noqa
from random import uniform
from time import sleep


def get_pagination_data(data: list) -> list:
    """
    Parses pagination
    The function is designed to work in parallelism
    :param data: packed arguments, consist of user agent, proxy, category name, donor url
    :return: List with dictionaries that contain as a key the path of the category
    and the value of the number of pages of the category
    """
    user_agent, proxy, categories, target_url = data
    sleep(uniform(*SLEEP_PARAMETERS[0]))
    headers = {
        "user-agent": user_agent
    }
    result = []
    amount_pagination = []
    url = f"{target_url}{categories}/"
    document = get_document(url, proxy=proxy, headers=headers)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    pagination_elements = soup.select("#pagination > ul")[0].find_all("a")
    for element in pagination_elements:
        amount_pagination.append(int(str(element["href"]).split("=")[-1]))
    result.append({url: max(amount_pagination)})
    return result
