import telebot
import buttons
import wikipedia

wikipedia.set_lang('ru')
bot = telebot.TeleBot('6830144675:AAGlL5KQ_zNLiXQioh_PUTAcz00-fpy_MoU')


@bot.message_handler(command=['start'])
def start(message):
    user_id = message.from_user.id
    bot.message_handler(user_id, 'привет ты в тестовом боте \n для начала пройди регистрацию')
    bot.register_next_step_handler(message, registration)


def registration(message):
    user_id = message.from_user.id
    bot.message_handler(user_id, 'отправьте свое имя')
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    user_id = message.from_user.id

    username = message.text

    bot.send_message(user_id, 'отправте номер телефона', reply_markup=buttons.number_buttons())
    bot.register_next_step_handler(message, next, username)


def next(message):
    user_id = message.from_user.id
    bot.message_handler(user_id, 'поздравляю вы успешно зарегались')
    bot.register_next_step_handler(message, next2)


def next2(message):
    user_id = message.from_user.id

    bot.message_handler(user_id, 'ну что поехали(это бот нужен для того что-бы \n не заходить в википедию а задавать '
                                 'вопрос отсюда ')
    bot.register_next_step_handler(message, next3)


def next3(message):
    user_id = message.from_user.id

    question = message.text
    page = wikipedia.page(question)

    bot.send_message(user_id, message.chat.id, page.summary)

    bot.infinity_polling()
