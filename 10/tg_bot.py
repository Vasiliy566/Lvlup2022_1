import telebot

bot = telebot.TeleBot('5599836785:AAFx9GuAzlGQsfLu8RDw5ezbdYL3akFJzSQ')


@bot.message_handler(commands=['start'])
def start_message(message):
    print(message)
    # bot.send_message(message.chat.id, 'Привет')


bot.infinity_polling()
