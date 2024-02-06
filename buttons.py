from telebot.types import InlineKeyboardMarkup,InlineKeyboardButton,ReplyKeyboardMarkup,KeyboardButton
def number_buttons():
    buttons = ReplyKeyboardMarkup(resize_keyboard=True)
    num_buttons = KeyboardButton('поделится контактом', request_contact=True)

    buttons.add(num_buttons)
    return buttons
