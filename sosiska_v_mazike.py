import telebot
from telebot import types
import random

TOKEN='790712070:AAF_VOm2TBZUIZfD1awmAPB1bBeIp7ddVuc'
bot = telebot.TeleBot(TOKEN)

b = 0

@bot.message_handler(commands=["start"])
def handle_message(message):
    vat = types.ReplyKeyboardMarkup(True, False)
    vat.row('Начать игру')
    bot.send_message(message.chat.id, 'Привет. Чтобы начать игру нажми "Начать игру"', reply_markup=vat)


@bot.message_handler(regexp="Начать игру")
def keyboard(message):
    global b
    b = random.randint(1, 100)
    key = types.ReplyKeyboardMarkup(True, True)
    key.row("Выше", "Ниже")
    bot.send_message(message.chat.id, "Мое чило будет выше или ниже " + str(b) + "?", reply_markup=key)


@bot.message_handler(content_types=["text"])
def main(message):
    vot = types.ReplyKeyboardMarkup(True, True)
    vot.row('Начать игру')
    a = random.randint(1, 100)
    if message.text == "Выше":
        if a > b:
            bot.send_message(message.chat.id, 'Правильно ! Моё число ' + str(a)+ ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)
        elif a < b:
            bot.send_message(message.chat.id, 'Не правильно ! Моё число ' + str(a) + ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)
    elif message.text == "Ниже":
        if a > b:
            bot.send_message(message.chat.id, 'Не правильно ! Моё число ' + str(a) + ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)
        elif a < b:
            bot.send_message(message.chat.id, 'Правильно ! Моё число ' + str(a)+ ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)


if __name__ == "__main__":
    bot.polling(none_stop=True)
