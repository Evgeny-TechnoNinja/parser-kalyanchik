from config import USER_AGENT_DATA, MARKUP_ANALYZER  # noqa
from .get_document import get_document  # noqa
from bs4 import BeautifulSoup  # type: ignore
from random import sample
import re


def get_user_agents(num_ua: int, proxy: dict) -> list:
    """
    Gets a document from the network, extracts lines with a user agent from it,
    then randomly extracts the specified number of user agents, in case it doesn’t,
    it will return the user agent that is assigned by default
    :param proxy: ip proxy
    :param num_ua: number of user agents
    :return: a list of user agents or one that is the default
    """
    user_agents = []
    headers = {
        "user-agent": USER_AGENT_DATA["default"]
    }
    document = get_document(USER_AGENT_DATA["url"], proxy=proxy, headers=headers)
    if document:
        soup = BeautifulSoup(document, MARKUP_ANALYZER)
        cells = soup.find_all('td')
        for cell in cells:
            if re.match(USER_AGENT_DATA["regex"]["user_agent"], cell.get_text()):
                user_agents.append("".join(cell.get_text().split('\n')).strip())
    try:
        return sample(user_agents, num_ua)
    except ValueError as error:
        return [USER_AGENT_DATA["default"]]
