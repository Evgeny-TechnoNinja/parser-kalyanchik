from bs4 import BeautifulSoup  # type: ignore
from config import MARKUP_ANALYZER # noqa
from .get_document import get_document


def get_category_name(url: str, proxy: dict, user_agent: str) -> list:
    """
    Gets the category name
    :param url: resource donor
    :param proxy: ip proxy
    :param user_agent: random user agent
    :return: list of category names
    """
    result = []
    headers = {
        "user-agent": user_agent
    }
    document = get_document(url, proxy=proxy, headers=headers)
    soup = BeautifulSoup(document, MARKUP_ANALYZER)
    links = soup.select("div.container > div.center-menu")[0].find_all("a")
    for link in links:
        result.append(str(link["href"]).strip("/"))
    return result[:-2]