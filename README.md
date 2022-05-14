# puzzle_project
import telebot
from time import sleep
bot = telebot.TeleBot('5221488288:AAHR4_qqgKWrWkDgbagc03HJ34HkzFLBPks')
#@bot.message_handler(content_types= 'text')

@bot.message_handler(commands=['start'])


def but(message):
    bot.send_message(message.chat.id, 'здарова мамонт')
    bot.send_message(message.chat.id, '/key проверка ключа')
    bot.send_message(message.chat.id, 'https://t.me/Igorpq, поддержка')
    bot.send_message(message.chat.id, 't.me/fellkings, поддержка')


bot.polling(non_stop=True, interval=0)
