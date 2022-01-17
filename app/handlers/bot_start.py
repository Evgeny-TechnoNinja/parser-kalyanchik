from loader import BOT as bot  # noqa
from config import BOT_ADMIN  # noqa
from settings_ui import DIALOGUE  # noqa


@bot.message_handler(commands=["start"])
def bot_start(message):
    if message.from_user.id == int(BOT_ADMIN):
        text = DIALOGUE["hello_admin"]
        bot.send_message(message.from_user.id, text)
