import telebot

from config import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler('/start')
def start(msg):
    pass
