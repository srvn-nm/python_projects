from urllib import response
import telebot
import requests

TOKEN = '5528897472:AAEVbf7Ic7wGOE3sYXd0v0j7cAtSUGByhHU'
URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, I'm Sarvin. What can I do for you?")
 
@bot.message_handler(func=lambda m: True)
def show_message(message):
    symbol = message.text.upper()
    response = requests.get(f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}')
    if response.status_code == 400:
        bot.reply_to(message, "invalid digital symbol")
    elif response.status_code == 200:
        data = response.json()
        bot.reply_to(message, f"Price for {data['symbol']} is {data['price']}.")
    else:
        bot.reply_to(message, "something went wrong.")
 
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, "I don't understand what you are trying to say.")
 
bot.infinity_polling()