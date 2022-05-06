from typing import Dict, Any
import ftplib
from settings_ui import DIALOGUE  # noqa
from dateutil import parser
from config import TIME_ZONE  # noqa
from datetime import timedelta, datetime
from pytz import timezone
import os
import os.path


def get_file_server(data_connect: list, folder: str, target: str, result_file: str) -> dict:
    """
    Delivers a file from the server provides the modification time of the file
    :param data_connect: data for connecting to the FTP server
    :param folder: folder where the file will be delivered
    :param target: path on the server to the desired directory
    :param result_file: filename on the FTP server
    :return: An object that contains the success states,
    file modification time, and progress message.
    """
    status: Dict[str, Any] = {
        "success": False,
        "change_time": None,
        "msg": ""
    }
    try:
        ftp_session = ftplib.FTP(*data_connect)
    except Exception as error:
        status["msg"] = DIALOGUE["ftp_fail"]
        return status
    ftp_session.cwd(target)
    server_files: list = ftp_session.nlst()
    if result_file in server_files:
        timestamp: str = ftp_session.voidcmd("MDTM %s" % result_file)[4:].strip()
        # Crutch :(
        time: datetime = parser.parse(timestamp)
        zone: datetime = (datetime.now(timezone(TIME_ZONE["Kiev"])))
        num = int(str(zone).split("+")[-1].replace("0", "")[0])
        status["change_time"] = time + timedelta(hours=num)
        # ===
        output = "./" + folder
        if not os.path.exists(output):
            os.mkdir(output)
        os.chdir(output)
        with open(result_file, "wb") as f:
            ftp_session.retrbinary("RETR %s" % result_file, f.write)
        status["success"] = True
        status["msg"] = DIALOGUE["download_file"]
        os.chdir("..")
    ftp_session.close()
    return status
