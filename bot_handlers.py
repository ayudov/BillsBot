from bot import bot


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi')

if __name__ == '__main__':
    bot.polling(none_stop=True)
