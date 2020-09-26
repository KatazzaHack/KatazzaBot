from telegram.ext import CommandHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from katazza_bot.video_storage import VideoStorage


def choose_theme(update, context):
    random_themes = sorted(VideoStorage.instance().get_random_themes())
    keyboard = [[InlineKeyboardButton(random_themes[0], callback_data=random_themes[0]),
                 InlineKeyboardButton(random_themes[1], callback_data=random_themes[1])],
                [InlineKeyboardButton(random_themes[2], callback_data=random_themes[2])]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose the theme:', reply_markup=reply_markup)

def start(update, context):
    choose_theme(update, context)



start_handler = CommandHandler('start', start)
