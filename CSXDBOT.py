import telebot;
import requests;
import random;
bot = telebot.TeleBot('1300031938:AAFygC8zJMBY6JdE4gM2Vrq12U9Az6qdQQg');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    bot.polling(none_stop=True, interval=0)
    