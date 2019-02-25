#!/usr/bin/env python
import random

import telebot
from telebot import types
from telebot.types import Message

TOKEN = '646147079:AAGWRRnuLpKqGWu6Uz5KMl_FOWo4L1KRTqk'
bot = telebot.TeleBot (TOKEN)


@bot.message_handler(content_types=["text"])
def any_msg(message):
    keyboard = types.InlineKeyboardMarkup()
    callback_button = types.InlineKeyboardButton(text="Да", callback_data="True")
    callback_button2 = types.InlineKeyboardButton(text="Нет", callback_data="False")
    keyboard.add(callback_button, callback_button2)
    bot.send_message(message.chat.id, "Климатическая техника?", reply_markup=keyboard)


        
@bot.message_handler(func=lambda message: messages.text == u'Нажми меня') #Если была вызвана Button 1
#Тут пишем метод который будет выполнятся, когда нажмём на кнопку
def button(message):
     bot.send_message(message.chat.id, 'Сюда пишем текст типо - Привет')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    if call.message:
        if call.data == "test":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь")    

        elif call.data == "test2":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Пыщь2") 
'''   
@bot.message_handler(content_types=['text'])
def echo_digits(message: Message):
  bot.reply_to(message, str(random.random()))
'''
@bot.message_handler(commands=['calendar'])
def get_calendar(message):
    now = datetime.datetime.now() #Текущая дата
    chat_id = message.chat.id
    date = (now.year,now.month)
    current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
    markup = create_calendar(now.year,now.month)
    bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=markup)
	
bot.polling()

