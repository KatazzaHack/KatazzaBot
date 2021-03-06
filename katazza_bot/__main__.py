from telegram.ext import Updater
import logging
from katazza_bot.handlers import init_handlers
from katazza_bot.config import TELEGRAM_BOT_TOKEN

def run(telegram_bot_token=TELEGRAM_BOT_TOKEN):
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.DEBUG, filename="logs.txt")

    init_handlers(dispatcher)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    run()