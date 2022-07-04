import telebot

TOKEN = '5528897472:AAEVbf7Ic7wGOE3sYXd0v0j7cAtSUGByhHU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, I'm Sarvin. What can I do for you?")
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "I don't understand what you are trying to say.")
 
bot.infinity_polling()