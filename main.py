import telebot
from telebot import types

from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, f'Привет <b>{msg.from_user.first_name}</b>', parse_mode='html')


@bot.message_handler(commands=['site'])
def get_site(msg):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт университета', url='https://norvuz.ru'))
    bot.send_message(msg.chat.id, 'Перейти на сайт', reply_markup=markup)


bot.polling(none_stop=True)
