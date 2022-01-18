import telebot
from telebot.types import InlineKeyboardMarkup


def create_inline_keyboard(data: dict) -> InlineKeyboardMarkup:
    """
    Creating an inline keyboard from a dictionary
    :param data: Name of keyboard buttons
    :return: Keyboard object
    """
    inline_keyboard = telebot.types.InlineKeyboardMarkup()
    inline_btn = [telebot.types.InlineKeyboardButton(text=current_value, callback_data=current_key)
                  for current_key, current_value in data.items()]
    inline_keyboard.add(*inline_btn)
    return inline_keyboard
