import ftplib


def upload(data_connect: list, target: str, filename: str) -> bool:
    """
    Connection to the FTP server, delivers a file to the server
    :param data_connect: authorization on the server, host, user, password
    :param target: path to put the file
    :param filename: name of the file of interest
    (it must be in the root of the program)
    :return: boolean value, success is True, otherwise False if the connection fails
    """
    try:
        ftp_session = ftplib.FTP(*data_connect)
    except Exception as error:
        return False
    ftp_session.cwd(target)
    new_filename = filename
    with open(filename, "rb") as f:
        ftp_session.storbinary("STOR %s" % new_filename, f)
    ftp_session.close()
    return True

