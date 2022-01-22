from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa
from settings_ui import DIALOGUE, MENU_MAIN_ITEMS  # noqa
from services import parser  # noqa


@bot.callback_query_handler(func=lambda call: True)
def callback_inline_keyboard(call):
    if call.message:
        PARSE, AUTOPARSE, DOWNLOAD, LINK = [item[0] for item in list(MENU_MAIN_ITEMS.items())]
        if call.data == PARSE:
            text = DIALOGUE["parser_notifi"]
            bot.send_message(chat_id=call.message.chat.id, text=text)
            status = parser()
            print(status)
            if not status["success"]:
                text = status["msg"]
                bot.send_message(chat_id=call.message.chat.id, text=text, reply_markup=MAIN_MENU)
                print("branch not proxy work")
            else:
                print("work good")
        elif call.data == AUTOPARSE:
            pass
        elif call.data == DOWNLOAD:
            pass
        elif call.data == LINK:
            pass