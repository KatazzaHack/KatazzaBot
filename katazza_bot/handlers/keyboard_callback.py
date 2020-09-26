from telegram.ext import CommandHandler, MessageHandler, Filters,  CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from katazza_bot.video_storage import VideoStorage

def callback_theme(update, context):
    query = update.callback_query
    context.user_data["theme"] = query.data
    times = VideoStorage.instance().get_times()

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    keyboard = [[InlineKeyboardButton(str(time), callback_data=time) for time in times]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    query.edit_message_text(text="Good choice! {} was selected\n".format(query.data)
                                 + "Please select the video length:", reply_markup=reply_markup)


def callback_length(update, context):
    query = update.callback_query
    context.user_data["length"] = query.data

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    random_themes = sorted(VideoStorage.instance().get_random_themes(), key=lambda x: len(x))
    keyboard = [[InlineKeyboardButton(random_themes[0], callback_data=random_themes[0]),
                 InlineKeyboardButton(random_themes[1], callback_data=random_themes[1])],
                [InlineKeyboardButton(random_themes[2], callback_data=random_themes[2])]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text=VideoStorage.instance().get_video(int(context.user_data["length"]), context.user_data["theme"]),
        reply_markup=reply_markup)


def callback_inline(update, context):
    query = update.callback_query
    if query.data in VideoStorage.instance().get_themes():
        callback_theme(update, context)
    elif query.data in VideoStorage.instance().get_times():
        callback_length(update, context)
    else:
        query.answer()
        query.edit_message_text(text="Error has occured: no such button "
                                     + str(type(query.data)) + str(query.data))


keyboard_callback_handler = CallbackQueryHandler(callback_inline)