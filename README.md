from telebot import types
import telebot

bot = telebot.TeleBot('5221488288:AAHR4_qqgKWrWkDgbagc03HJ34HkzFLBPks')

keyword_ = '2541-986-37'

@bot.message_handler(commands=['start'])
def but(message):
    bot.send_message(message.chat.id, 'https://t.me/Igorpq, поддержка')
    bot.send_message(message.chat.id, 'https://t.me/fellkings, поддержка')
    bot.send_message(message.chat.id, 'https://t.me/voxy9132, поддержка')
    mess = f"Привет, <b>{message.from_user.first_name}</b>, я FellygaBot,  проверяю ключи. Введите ключ для проверки."
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(commands= 'text')
def key1(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.from_user.id, 'Пришли ключ на проверку', reply_markup = keyboard)

@bot.message_handler(content_types = 'text')
def key(message):
    keyboard = types.InlineKeyboardMarkup()
    if message.text == keyword_:
        bot.send_message(message.from_user.id, 'Ключ действителен!', reply_markup = keyboard)
    if message.text != keyword_:
        bot.send_message(message.from_user.id, 'Ключ не рабочий или был использован повторно', reply_markup = keyboard)

bot.polling(non_stop=True)
