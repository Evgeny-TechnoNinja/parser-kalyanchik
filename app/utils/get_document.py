from typing import Optional
from utils.write_logs import write_logs  # noqa
import requests


def get_document(url: str, parameter: dict = None, headers: dict = None, proxy: dict = None) -> Optional[str]:
    """
    Performs Get requests to the desired target.
    If the request failed, it will write the failure to the logs
    :param url: target address
    :param parameter: payloads
    :param headers: required header data, user agent
    :param proxy: ip address in the correct format
    :return: response content on successful request otherwise nothing
    """
    session = requests.Session()
    try:
        response = session.get(url, params=parameter, headers=headers, proxies=proxy)
        try:
            response.raise_for_status()
            return response.text
        except requests.exceptions.HTTPError as error:
            write_logs(str(error))
    except requests.exceptions.ProxyError as error:
        write_logs(str(error))
    return None
