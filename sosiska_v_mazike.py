import telebot
from telebot import types
import random
import os

TOKEN='790712070:AAF_VOm2TBZUIZfD1awmAPB1bBeIp7ddVuc'
bot = telebot.TeleBot(TOKEN)

b = 0

@bot.message_handler(commands=["start"])
def handle_message(message):
    n = message.chat.id
    if os.path.isfile(f'./{n}') == False:
        n = message.chat.id
        f = open(f'Users/{n}', "w+")
        f.write('0')
        f.close()

    f = open(f'Users/{n}', "r")
    x = f.read(1)
    vat = types.ReplyKeyboardMarkup(True, False)
    vat.row('Начать игру')
    bot.send_message(message.chat.id, f'Привет.У тебя {x} баллов. Чтобы начать игру нажми "Начать игру"', reply_markup=vat)


@bot.message_handler(regexp="Начать игру")
def keyboard(message):
    global b
    b = random.randint(1, 50)
    key = types.ReplyKeyboardMarkup(True, True)
    key.row("Больше", "Меньше")
    bot.send_message(message.chat.id, "Мое число будет больше или меньше " + str(b) + "?", reply_markup=key)


@bot.message_handler(content_types=["text"])
def main(message):
    vot = types.ReplyKeyboardMarkup(True, True)
    vot.row('Начать игру')
    a = random.randint(1, 50)
    n = message.chat.id
    f = open(f'Users/{n}', "r")
    x = f.read(1)
    y = int(x)
    if message.text == "Больше":
        if a > b:
            f = open(f'Users/{n}', "w")
            y = y + 1
            f.write(str(y))
            f.close()
            bot.send_message(message.chat.id, 'Как ты угадал ?! Твой счет: "' +str(y) +'"  Было загаданно число  ' + str(a)+ ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)
        elif a < b:
            bot.send_message(message.chat.id, 'Хахахаха.... не угадал ! Моё число ' + str(a) + ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)
    elif message.text == "Меньше":
        if a > b:
            bot.send_message(message.chat.id, 'Фууу не угадал ! Моё число ' + str(a) + ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)
        elif a < b:
            f = open(f'Users/{n}', "w")
            y = y + 1
            f.write(str(y))
            f.close()
            bot.send_message(message.chat.id, 'Ого!! Придеться дать тебе балл. Твой счет: "' + str(y) +  '"  Я загадал число  ' + str(a)+ ". Чтобы Попробовать еще нажми 'Начать игру' ?", reply_markup=vot)

if __name__ == "__main__":
    bot.polling(none_stop=True)
