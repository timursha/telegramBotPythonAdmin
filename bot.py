# coding=utf-8
from telegram.ext import Updater, Filters, MessageHandler
import telegram
import sqlite3
import datetime
import requests
import json
from telegram import message

token = "631227260:AAGmtcTJgc25d37m4OGwPVIyImeJeDmbmIU"

cities = [["Москва", "Ростов", "Калининград", "Уфа"]]
bonuses = [["общий", "частный"]]
rec_for_db = {"step": 0, "name": "", "phone_number": "", "city": "", "bonus": "", "msg": "", "surname": ""}

URL = "https://api.telegram.org/bot" + token + "/"


def handle_text(bot, update):
    if rec_for_db["step"] == 0:
        req = "select products_ticket.chat_messages from products_ticket where chat_id=%s;"%(update.message.chat.id)

        # req = "select * from products_ticket;"
        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()
        b = cursor.execute(req)
        b = cursor.fetchall()[0][0]
        print(b)
        b += "user :" + update.message.text + "\n"
        req = "update products_ticket set chat_messages = '%s' where chat_id='%s'"%(b, update.message.chat.id)
        b = cursor.execute(req)
        print(b)
        connection.commit()
        connection.close()


    if rec_for_db["step"] == 1:
        rec_for_db["phone_number"] = update.message.text
        rec_for_db["step"] = rec_for_db["step"] + 1     # переход к следующему шагу
        print(rec_for_db)
        bot.send_message(chat_id=update.message.chat.id, text="введите имя:")
    elif rec_for_db["step"] == 2:
        rec_for_db["name"] = update.message.text
        rec_for_db["step"] = rec_for_db["step"] + 1  # переход к следующему шагу
        print(rec_for_db)
        bot.send_message(chat_id=update.message.chat.id, text="введите фамилию:")
    elif rec_for_db["step"] == 3:
        rec_for_db["surname"] = update.message.text
        rec_for_db["step"] = rec_for_db["step"] + 1  # переход к следующему шагу
        print(rec_for_db)
        bot.send_message(chat_id=update.message.chat.id, text="выберите город:",
                         reply_markup=telegram.ReplyKeyboardMarkup(cities, one_time_keyboard=True,
                                                                   resize_keyboard=True))
    elif rec_for_db["step"] == 4:
        if update.message.text in cities[0]:
            rec_for_db["city"] = update.message.text
            rec_for_db["step"] = rec_for_db["step"] + 1  # переход к следующему шагу
            print(rec_for_db)
            bot.send_message(chat_id=update.message.chat.id, text="выберите бонус:",
                             reply_markup=telegram.ReplyKeyboardMarkup(bonuses, one_time_keyboard=True,
                                                                       resize_keyboard=True))
        else:
            bot.send_message(chat_id=update.message.chat.id, text="There is no your city in list")
    elif rec_for_db["step"] == 5:
        if update.message.text in bonuses[0]:
            rec_for_db["bonus"] = update.message.text
            rec_for_db["step"] = rec_for_db["step"] + 1  # переход к следующему шагу
            print(rec_for_db)
            bot.send_message(chat_id=update.message.chat.id, text="напишите сообщения")
        else:
            bot.send_message(chat_id=update.message.chat.id, text="There is no your bonus in list")
    elif rec_for_db["step"] == 6:
        rec_for_db["msg"] = update.message.text
        rec_for_db["step"] = rec_for_db["step"] + 1  # завершение опроса
        print(rec_for_db)
        bot.send_message(chat_id=update.message.chat.id, text="спасибо. Ожидайте ответа.")\
        
        name = rec_for_db["name"]
        surname = rec_for_db["surname"]
        town = rec_for_db["city"]
        phone = rec_for_db["phone_number"]
        message = rec_for_db["msg"]
        created = datetime.datetime.today()
        print(created)
        updated = datetime.datetime.today()
        print(updated)
        chat_id = update.message.chat.id
        chat_message = "user: " + message + "\n" + "admin: Спасибо! ожидай ответа.\n"

        connection = sqlite3.connect("db.sqlite3")
        cursor = connection.cursor()

        req = "insert into products_ticket (name, surname, town, phone, message, is_active, created, updated, status_id, is_main, chat_id, chat_messages) values ('%s', '%s', '%s', '%s', '%s', 1, '%s', '%s', 1, 1, '%s', '%s');"%(name, surname, town, phone, message, created, updated, chat_id, chat_message)
        b = cursor.execute(req)
        print(b)
        connection.commit()
        connection.close()
        print("added!!!")
        rec_for_db["step"] = 0
    
def handle_command(bot, update):
    if update.message.text == "/start":
        bot.send_message(chat_id=update.message.chat.id, text="Enter phone number:")
        rec_for_db["step"] = rec_for_db["step"] + 1     # переход к следующему шагу

updater = Updater(token=token)

text_handler = MessageHandler(Filters.text, handle_text)
command_handler = MessageHandler(Filters.command, handle_command)

updater.dispatcher.add_handler(text_handler)
updater.dispatcher.add_handler(command_handler)


# dispatcher.run_async(updater.start_polling(poll_interval=2))

updater.start_polling(poll_interval=2)
