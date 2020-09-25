from telegram.ext import MessageHandler, Filters


def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand that command.")


unknown_handler = MessageHandler(Filters.command, unknown)
