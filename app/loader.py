import telebot
from config import TELEGRAM_TOKEN
from settings_ui import MENU_MAIN_ITEMS
from keyboard import create_inline_keyboard as keyboard

BOT = telebot.TeleBot(TELEGRAM_TOKEN)
KEYBOARD_MAIN_MENU = keyboard(MENU_MAIN_ITEMS)
