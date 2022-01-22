from config import USER_AGENT_DATA  # noqa
from .get_document import get_document  # noqa


def get_user_agents(num_ua):
    user_agents = []
    headers = {
        "user-agent": USER_AGENT_DATA["default"]
    }
    document = get_document(USER_AGENT_DATA["url"], headers=headers)
    # soup = BeautifulSoup(document, config.MARKUP_ANALYZER)
    # cells = soup.find_all('td')
    # for cell in cells:
    #     if re.match(config.REGEX["user_agent"], cell.get_text()):
    #         user_agents.append("".join(cell.get_text().split('\n')).strip())
    # try:
    #     return sample(user_agents, num_ua)
    # except ValueError as error:
    #     return config.DEFAULT_USER_AGENT