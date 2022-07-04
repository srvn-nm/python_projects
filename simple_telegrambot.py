import telebot

TOKEN = '5528897472:AAEVbf7Ic7wGOE3sYXd0v0j7cAtSUGByhHU'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, I'm Sarvin. What can I do for you?")
 
bot.infinity_polling()