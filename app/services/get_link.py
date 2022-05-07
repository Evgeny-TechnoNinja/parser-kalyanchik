from config import PATH_TARGET, FILE_TARGET  # noqa


def get_link():
    """
    Provides a link to a file
    :return: link
    """
    return f"http://{PATH_TARGET.split('/')[-1]}/{FILE_TARGET}"

