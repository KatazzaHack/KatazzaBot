from katazza_bot.handlers.start import start_handler
from katazza_bot.handlers.keyboard_callback import keyboard_callback_handler
from katazza_bot.handlers.unknown import unknown_handler


def init_handlers(dispatcher):
    dispatcher.add_handler(start_handler)
    # dispatcher.add_handler(set_length_handler)
    # dispatcher.add_handler(set_theme_handler)
    # dispatcher.add_handler(choose_theme_handler)
    dispatcher.add_handler(keyboard_callback_handler)
    dispatcher.add_handler(unknown_handler)
