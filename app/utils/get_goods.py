import re
from typing import Dict, Any, Union
from bs4 import BeautifulSoup  # type: ignore
from config import MARKUP_ANALYZER, SLEEP_PARAMETERS  # noqa
from .get_document import get_document
from random import uniform
from time import sleep


def get_goods(data: list) -> list:
    """
    Gets all products by the provided link
    The function is designed to work in parallelism
    :param data: user agent, proxy, list of links where the product is available
    :return: list of dictionaries that contain product
    """
    user_agent, proxy, links = data
    result = []
    sleep(uniform(*SLEEP_PARAMETERS[1]))
    headers = {
        "user-agent": user_agent
    }
    assist: Dict[str, Any] = {
        "word_parasite": "оптом",
        "product_exists": "Есть в наличии",
        "currency": ["грн", "UAH"],
        "word_no_separator": ["Упаковка", "Подсветка"],
        "separator": ":",
        "regex_style_del": "<[^<]+?>",
        "max_chars": 3000,
    }
    for value in links.values():
        blank_category: Dict[str, Any] = {
            "category":  {
                "category_name": "",
                "category_id": 0  # this is a stub for the identifier, it will be made when the document is written
            },
            "goods": []
        }
        for url in value:
            blank_goods: Dict[str, Any] = {
                "product": {
                    "id": "",
                    "available": "false",
                    "url": "",
                    "price": "",
                    "currency": "",
                    "pictures": [],
                    "name": "",
                    "description": "",
                    "param": [],
                    "category": ""
                }
            }
            document = get_document(url, proxy=proxy, headers=headers)
            try:
                soup = BeautifulSoup(document, MARKUP_ANALYZER)
            except Exception as error:  # noqa
                continue
            # TODO: Logical change
            if not blank_category["category"]["category_name"]:
                breadcrumbs = soup.find("ul", {"class": "breadcrumbs"})
                elem_links = breadcrumbs.find_all("a")
                title = elem_links[1].text
                blank_category["category"]["category_name"] = title
                print(blank_category["category"]["category_name"])
            # print(url)
            blank_goods["product"]["url"] = url
            title = soup.find("h1", {"class": "one-card__title"}).text
            blank_goods["product"]["id"] = title.split("-")[-1].strip()
            new_title = title.replace(assist["word_parasite"], "*")
            blank_goods["product"]["name"] = new_title.split("*")[0].strip()
            try:
                available = soup.find("span", {"class": "one-card__available"}).text
            except AttributeError:
                available = soup.find("span", {"class": "one-card__not-available"}).text
            if available == assist["product_exists"]:
                blank_goods["product"]["available"] = "true"
            currency = soup.select("div.one-c_model--wrap > div:nth-child(2) > span:nth-child(2)")[0].text.split()
            blank_goods["product"]["price"] = currency[0]
            if currency[1] == assist["currency"][0]:
                blank_goods["product"]["currency"] = assist["currency"][1]
            slider = soup.select("div.product-image.navigation_show")
            try:
                photos = slider[0].find_all("div", {"class": "big-image"})
                for item in photos:
                    blank_goods["product"]["pictures"].append(item.find("a")["href"])
            except (IndexError, ValueError):
                pass
            characteristic = soup.find("ul", {"class": "one-card__specif"})
            if characteristic:
                for item in characteristic:
                    content = item.text
                    if content != "\n":
                        new_content = []

                        def string_modifier(idx: int):
                            new_content.append(content.replace(assist["word_no_separator"][idx],
                                                               assist["word_no_separator"][idx] + assist[
                                                                   "separator"]))

                        if assist["word_no_separator"][0] in content:
                            string_modifier(0)
                        elif assist["word_no_separator"][1] in content:
                            string_modifier(1)
                        else:
                            new_content.append(content)
                        temporary = "".join(new_content).split(assist["separator"])
                        # print("temporary:", temporary)
                        try:
                            blank_goods["product"]["param"].append(
                                {temporary[0]: temporary[1].strip()})
                        except IndexError:
                            blank_goods["product"]["param"].append(
                                {temporary[0]: ""})
            colors = soup.select("div.one-card__color")
            if colors:
                appearance = []
                key = colors[0].find("span").text
                links = colors[0].find_all("a")
                for link in links:
                    appearance.append(link.attrs["title"])
                blank_goods["product"]["param"].append({key: ", ".join(appearance).lower()})
            # product description
            tab_element = soup.select("div.tabs__items > div > ul > li:nth-child(2) > div")
            if tab_element:
                html_elements = []
                for current_tab_content in tab_element:
                    if len(current_tab_content) > 3:
                        new_string = re.sub(assist["regex_style_del"], "", str(current_tab_content))  # noqa
                        html_elements.append(new_string)
                html_strings = "".join(html_elements)
                if len(html_strings) <= assist["max_chars"]:
                    blank_goods["product"]["description"] = html_strings
                blank_goods["product"]["category"] = blank_category["category"]["category_name"]
            blank_category["goods"].append(blank_goods)
        result.append(blank_category)
        print("blank_category add", blank_category)
    return result
