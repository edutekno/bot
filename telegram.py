import telebot

bot = telebot.TeleBot("5103019892:AAGAmxFPo_I_Tw0dfFGouY6vTSgk230Afho")

# handle commands, /start
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hello, welcome to Telegram Bot!")
    
# handle all messages, echo response back to users
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
	bot.reply_to(message, "We use Colab. You write "+message.text)

bot.polling()
