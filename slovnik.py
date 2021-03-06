#!/usr/bin/python3
from telegram import ChatAction, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Handler, Filters
import logging
import os
from parser import Parser
#from parser import MAX_LENGTH

env = './.env'
with open(env) as f:
    os.environ.update(
        line.strip().split('=', 1) for line in f
    )
#Here insert your Telegram bot HTTP API TOKEN
TOKEN = os.environ['TOKEN']
#Trim output result to OUTPUT_LIMIT
OUTPUT_LIMIT = int(os.environ['OUTPUT_LIMIT'])

# Enable Logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fileHandler = logging.FileHandler("{0}/{1}.log".format("log","slovnik"))
logger.addHandler(fileHandler)



def log_params(method_name, update):
    logger.info("\nFrom: %s - %s %s \ndate: %s\nText: %s" %
                (update.message.from_user.username,
                 update.message.from_user.first_name,
                 update.message.from_user.last_name,
                 update.message.date,
                 update.message.text))

def start(bot, update):
    log_params('start', update)
    bot.sendMessage(update.message.chat_id, 
        text="""Tento bot prekladá slová z ruštiny do slovenčiny a zo slovenčiny do ruštiny. Этот бот переводит слова с русского на словацкий и со словацкого на русский. """)

def translate(bot, update, count=OUTPUT_LIMIT):
    log_params('translate', update)
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    parser = Parser(update.message.text)
    translated_text = parser.get_translated_text(length=count)
    return bot.sendMessage(chat_id=update.message.chat_id, text=translated_text, parse_mode=ParseMode.HTML)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Неизвестная команда. Neznáma inštrukcia.")

'''
def complete(bot, update):
    translate(bot, update, count=MAX_LENGTH)
'''
def error_handler(bot, update, error):
    print("error")
    try:
        raise error
    except Exception as e:
        client.captureException()



def main():
    updater = Updater(TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dp.add_handler(start_handler)
    translate_handler = MessageHandler(Filters.text, translate)
    dp.add_handler(translate_handler)
    unknown_handler = MessageHandler(Filters.command, unknown)
    dp.add_handler(unknown_handler)
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()