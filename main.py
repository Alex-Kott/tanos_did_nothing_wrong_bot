import time
from random import randint

import telebot

from config import BOT_API_TOKEN


bot = telebot.TeleBot(BOT_API_TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	if message.from_user.username == "Sapiosexual":
		unrestrict_date = time.time() + randint(31, 60)
		try:
			bot.restrict_chat_member(message.chat.id, message.from_user.id, until_date=unrestrict_date, can_send_messages=False)
		except:
			pass


bot.polling()