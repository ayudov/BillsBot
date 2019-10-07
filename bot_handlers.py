from bot import bot
import config_google_spreadsheet as cgs
from telebot.types import Message
from string_parsing import command, parse_string
from pprint import pprint, pformat


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, 'Hi')


@bot.message_handler(commands=['spent'])
def send_welcome(message):
    bot.send_message(message.chat.id, str(cgs.get_spent_value()))


@bot.message_handler(commands=['link'])
def send_welcome(message):
    bot.send_message(message.chat.id, '<a href="https://docs.google.com/spreadsheets/d/1Rmxzivvr_IrJQArpO6U9wyQDLr7YwVQii_9CXwLZEHM/edit#gid=1339252963url">link</a>',parse_mode='HTML')


@bot.message_handler(content_types=["text"]) #Любой текст
def any_text(message: Message):
    text = parse_string(message.text)
    cgs.write_in_sheet(text)
    # bot.send_message(message.chat.id, str(text))
    bot.send_message(message.chat.id, str(pformat(cgs.get_cells_values())))

    # bot.send_message(message.chat.id, str(cgs.get_number_of_rows()))
    # bot.send_message(message.chat.id, str(cgs.COMMENT_COL))
    #

if __name__ == '__main__':
    bot.polling(none_stop=True)
