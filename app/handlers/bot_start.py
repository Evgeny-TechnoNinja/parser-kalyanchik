from loader import BOT as bot, KEYBOARD_MAIN_MENU as MAIN_MENU  # noqa
from config import BOT_ADMIN  # noqa
from settings_ui import DIALOGUE  # noqa


@bot.message_handler(commands=["start"])
def bot_start(message):
    if not message.from_user.id == int(BOT_ADMIN):
        bot.reply_to(message, DIALOGUE["warning_not_admin"].format(message.from_user.id))
    else:
        text = DIALOGUE["hello_admin"]
        bot.send_message(message.from_user.id, text)
        text = DIALOGUE["panel"]
        bot.send_message(message.from_user.id, text, reply_markup=MAIN_MENU)
