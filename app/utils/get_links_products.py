from bs4 import BeautifulSoup  # type: ignore
from .get_document import get_document
from config import MARKUP_ANALYZER, NAVIGATION_NAME, SLEEP_PARAMETERS # noqa
from random import uniform
from time import sleep


def get_links_products(data: list) -> list:
    """
    Gets links to each product
    The function is designed to work in parallelism
    :param data: packed arguments, user agent, proxy, pagination information
    :return: a list of dictionaries, where the key is the name of the category
    and the value is a list of links to the product of this category
    """
    user_agent, proxy, pagination_information = data
    sleep(uniform(*SLEEP_PARAMETERS[0]))
    links_products = []
    headers = {
        "user-agent": user_agent
    }
    for path, num in pagination_information.items():
        category_name = str(path).split("/")[-2]
        blank: dict = {category_name: []}
        for current_num in range(1, num + 1):
            payload = {NAVIGATION_NAME: str(current_num)}
            document = get_document(path, parameter=payload, proxy=proxy, headers=headers)
            soup = BeautifulSoup(document, MARKUP_ANALYZER)
            cards = soup.find_all("div", {"class": "productions-slider__card"})
            for card in cards:
                product_box = card.find_all("div", {"class": "prod-opt--padding"})
                for item in product_box:
                    blank[category_name].append(item.find("a")["href"])
        links_products.append(blank)
    return links_products
