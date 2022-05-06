from datetime import datetime
from settings_ui import DIALOGUE  # noqa
from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa
from services import auto_parsing  # noqa
from config import CONNECT_DATA, PATH_TARGET  # noqa


def set_time(message):
    """
    Is a handler, accepts, processes the time entered by the user
    :param message: information entered by the user, text, etc.
    """
    time_user = message.text
    try:
        datetime.strptime(time_user, "%H:%M")
        auto_parsing(time_user, message, bot, MAIN_MENU, CONNECT_DATA, PATH_TARGET)
    except ValueError:
        text = DIALOGUE["wrong_time_format"]
        bot.send_message(message.from_user.id, text, reply_markup=MAIN_MENU)
