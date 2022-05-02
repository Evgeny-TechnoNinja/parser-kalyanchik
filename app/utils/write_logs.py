import logging
from config import HTTP_ERROR_FILE  # noqa


def logs_init() -> None:
    """
    Initializes logging
    """
    logging.basicConfig(filename=HTTP_ERROR_FILE, level=logging.INFO, filemode="w")


def write_logs(txt) -> None:
    """
    Writes the text of the error to the file
    :param txt: error text
    """
    print("[!]log: ", txt)
    logging.warning(txt)
