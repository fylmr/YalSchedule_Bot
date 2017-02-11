# -*- coding: utf-8 -*-
from telebot import types
import config
import telebot
import dbstuff

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, "Привет. Здесь можно узнать расписание пар.")

    choose_day(message)


def choose_day(message):
    """
    Открыть клавиатуру с выбором
    дня недели
    """

    markup = types.ReplyKeyboardMarkup(row_width=2)

    itembtn1 = types.KeyboardButton('Понедельник')
    itembtn2 = types.KeyboardButton('Вторник')
    itembtn3 = types.KeyboardButton('Среда')
    itembtn4 = types.KeyboardButton('Четверг')
    itembtn5 = types.KeyboardButton('Пятница')
    itembtn6 = types.KeyboardButton('Суббота')

    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)

    bot.send_message(message.chat.id, "Выбери день:",
                     reply_markup=markup)


@bot.message_handler(regexp="(Пон)|(Втор)|(Сред)|(Четв)|(Пят)|(Суб)"
                     .decode('utf-8'))
def show_day(message):
    """
    Показать расписание на конкретный день,
    если получили в ответе сообщение с днём
    """

    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, "Расписание:", reply_markup=markup)


@bot.message_handler(commands=['start', 'help'])
def get_today_schedule(message):
    pass


bot.polling(none_stop=True)
