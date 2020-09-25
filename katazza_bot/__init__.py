from telegram.ext import Updater
import logging
from katazza_bot.handlers import init_handlers
from katazza_bot.config import TELEGRAM_BOT_TOKEN

# Create katazza_bot/config.py that contains the following line:
# TELEGRAM_BOT_TOKEN = 'ADD YOUR TOKEN HERE'
def run(telegram_bot_token=TELEGRAM_BOT_TOKEN):
    updater = Updater(token=TELEGRAM_BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    logging.basicConfig(filename="logs.txt", format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    init_handlers(dispatcher)

    updater.start_polling()
