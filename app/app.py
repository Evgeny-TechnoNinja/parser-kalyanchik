if __name__ == '__main__':
    from loader import BOT as bot
    from handlers import bot_start, callback_query
    bot.polling()
