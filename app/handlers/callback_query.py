from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa
from settings_ui import DIALOGUE, MENU_MAIN_ITEMS  # noqa
from services import parser  # noqa
from utils import create_yml_document, upload  # noqa
from config import CONNECT_DATA, PATH_TARGET  # noqa


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
            pass
        elif call.data == DOWNLOAD:
            pass
        elif call.data == LINK:
            pass