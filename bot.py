# !/usr/bin/env python2.7
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

    day_choose_keyboard(message)


@bot.message_handler(commands=['today'])
def get_today_schedule(message):
    pass


def day_choose_keyboard(message):
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
    keyboard_remove(message)
    bot.send_message(message.chat.id, show_day_parser(
        message.text), parse_mode="Markdown")


def show_day_parser(message):
    msg = dbstuff.get_day(day_to_int(message))  # tuple of lists
    res = ''
    for i in msg:
        res += dbstuff.get_starttime(i[1])
        res += ' *'
        res += dbstuff.get_subject_name(i[2])
        res += '* '
        res += str(i[3])
        res += ' '
        res += "\n"
    return res


def keyboard_remove(message):
    """
    Показать расписание на конкретный день,
    если получили в ответе сообщение с днём
    """

    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(
        message.chat.id, "Расписание на этот день: ", reply_markup=markup)


def day_to_int(day):
    day = day.encode('utf-8')
    return {
        'Понедельник': 1,
        'Вторник': 2,
        'Среда': 3,
        'Четверг': 4,
        'Пятница': 5,
        'Суббота': 6,
        'Воскресенье': 7
    }.get(day, 0)


bot.polling(none_stop=True)
