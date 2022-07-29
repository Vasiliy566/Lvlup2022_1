import telebot

from register import is_user_exists, create_user
from utils import is_email_valid

bot = telebot.TeleBot('5599836785:AAFx9GuAzlGQsfLu8RDw5ezbdYL3akFJzSQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я умею /register')


@bot.message_handler(commands=['register'])
def register(message):
    user_id = message.chat.id
    if is_user_exists(user_id):
        bot.send_message(user_id, 'Ты уже регистрировался!')
    else:
        bot.send_message(message.chat.id, 'Введи пожалуйста свое имя и фамилию')
        bot.register_next_step_handler(message, read_name)


def read_name(message):
    name = message.text
    bot.send_message(message.chat.id, f"Введи пожалуйста свою почту")
    bot.register_next_step_handler(message, read_email, name)


def read_email(message, name):
    email = message.text
    if is_email_valid(email):
        bot.send_message(message.chat.id, f"Спасибо за регистрацию")
        create_user(message.chat.id, name, email)
    else:
        bot.send_message(message.chat.id, f"Некорректная почта")


bot.infinity_polling()
