from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa
from settings_ui import DIALOGUE, MENU_MAIN_ITEMS  # noqa
from services.parser import parser  # noqa
from services import get_file_server, get_link  # noqa
from utils import create_yml_document, upload  # noqa
from config import CONNECT_DATA, PATH_TARGET, FOLDER_RESULT, FILE_TARGET  # noqa
from .set_time import set_time


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_keyboard(call):
    if call.message:
        PARSE, AUTOPARSE, DOWNLOAD, LINK = [item[0] for item in list(MENU_MAIN_ITEMS.items())]
        if call.data == PARSE:
            text = DIALOGUE["parser_notifi"]
            bot.send_message(chat_id=call.message.chat.id, text=text)
            status = parser()
            if not status["success"]:
                text = status["msg"]
                bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
            else:
                text = status["msg"] + DIALOGUE["creation_yml"]
                bot.send_message(chat_id=call.message.chat.id, text=text)
                notification_data = create_yml_document(status["data"])
                if notification_data["filename"]:
                    text = notification_data["msg"] + DIALOGUE["written_file"].format(
                        notification_data["total_products"])
                    bot.send_message(chat_id=call.message.chat.id, text=text)
                    status = upload(CONNECT_DATA, PATH_TARGET, notification_data["filename"])
                    if not status:
                        text = DIALOGUE["upload_fail"]
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
                    else:
                        text = DIALOGUE["successful_upload"] + DIALOGUE["successful_parsing"]
                        bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
        elif call.data == AUTOPARSE:
            text = DIALOGUE["time_notifi"].format(DIALOGUE["time_example"])
            bot.send_message(chat_id=call.message.chat.id, text=text)
            bot.register_next_step_handler(call.message, set_time)
        elif call.data == DOWNLOAD:
            status = get_file_server(CONNECT_DATA, FOLDER_RESULT, PATH_TARGET, FILE_TARGET)
            if not status["success"]:
                if status["msg"]:
                    text = status["msg"]
                    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
                else:
                    text = DIALOGUE["download_fail"]
                    bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
            else:
                text = status["msg"]
                bot.send_message(chat_id=call.message.chat.id, text=text)
                bot.send_document(call.message.chat.id, open(f"{FOLDER_RESULT}/{FILE_TARGET}", "rb"))
                text = DIALOGUE["file_info"].format(status["change_time"])
                bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
        elif call.data == LINK:
            text = DIALOGUE["hot_link"].format(get_link())
            bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)