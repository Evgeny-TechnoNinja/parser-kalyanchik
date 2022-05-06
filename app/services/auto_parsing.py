import threading
import time
import schedule  # type: ignore
from .parser import parser
from settings_ui import DIALOGUE  # noqa
from utils import create_yml_document, upload  # noqa


def auto_parsing(user_time, message, bot, MAIN_MENU, CONNECT_DATA, PATH_TARGET):
    """
    Implements the launch of the parser on a schedule,
    creates a thread and performs the necessary work in it
    :param user_time: time specified by the user in the desired format
    :param message: information entered by the user, text, etc.
    :param bot: instance TeleBot
    :param MAIN_MENU: control buttons, keyboard
    :param CONNECT_DATA: data for connecting to the FTP server
    :param PATH_TARGET: path on the server to the desired directory
    """
    bot.send_message(message.from_user.id, text=DIALOGUE["autoparse_time_set"])

    def job():
        status: dict = parser()
        if not status["success"]:
            text = status["msg"] + DIALOGUE["autoparse_fail"]
            bot.send_message(message.from_user.id, text, reply_markup=MAIN_MENU)
        else:
            notification_data = create_yml_document(status["data"])
            if not notification_data["filename"]:
                text = DIALOGUE["document_yml_fail"] + DIALOGUE["autoparse_fail"]
                bot.send_message(message.from_user.id, text, reply_markup=MAIN_MENU)
            else:
                status: bool = upload(CONNECT_DATA, PATH_TARGET, notification_data["filename"])
                if not status:
                    text = DIALOGUE["autoparse_fail"] + DIALOGUE["upload_fail"]
                    bot.send_message(message.from_user.id, text=text, reply_markup=MAIN_MENU)
                else:
                    text = DIALOGUE["successful_upload"] + DIALOGUE["autoparse_ready"]
                    bot.send_message(message.from_user.id, text=text, reply_markup=MAIN_MENU)

    def run_threaded(job_func):
        job_thread = threading.Thread(target=job_func)
        job_thread.start()

    def run_schedule():
        schedule.every().day.at(user_time).do(run_threaded, job)
        while True:
            time.sleep(1)
            schedule.run_pending()

    run_schedule()
