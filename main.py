# Телеграм бот 2Pizza
import telebot
from telebot import types
bot =  telebot.TeleBot("1677873176:AAECD3nnnsCFLbZyszLC1CzONAwFBGK48r4")
markup = types.ReplyKeyboardMarkup(row_width=2)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я 2pizza бот. Приятно познакомиться, {message.from_user.username}, я помогу тебе с доставкой пиццы! Я могу помочь с доставкой в Гомеле и Миснке, и так в каком городе ты находишься?')

@bot.message_handler(content_types=['text'])
def choose_town(message):
    if message.text.lower() == "гомель" or message.text.lower() == "гомеле":
        itembtn1 = types.KeyboardButton("Papa John's")
        itembtn2 = types.KeyboardButton('Dodo Pizza')
        itembtn3 = types.KeyboardButton('Dominos Pizza')
        markup.add(itembtn1, itembtn2, itembtn3)
        bot.send_message(message.chat.id, "Выбери пиццерию", reply_markup=markup)
    elif message.text.lower() == "минск" or message.text.lower() == "минске":
        bot.send_message(message.chat.id, "Вот список пиццерий в Минске:")
    else:
        bot.send_message(message.chat.id,"Не понял, что ты имел ввиду")





bot.polling()
