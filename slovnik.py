#!/usr/bin/python3
from telegram import Updater, ChatAction, ParseMode
import logging
from parser import Parser
#from parser import MAX_LENGTH

#Here insert your Telegram bot HTTP API
TOKEN = ''

# Enable Logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def log_params(method_name, update):
    logger.debug("Method: %s\nFrom: %s\nchat_id: %d\nText: %s" %
                (method_name,
                 update.message.from_user,
                 update.message.chat_id,
                 update.message.text))

def start(bot, update):
    log_params('start', update)
    bot.sendMessage(update.message.chat_id
        , text="""Tento bot prekladá slová z ruštiny do slovenčiny a zo slovenčiny do ruštiny.
Этот бот переводит слова с русского на словацкий и со словацкого на русский.""")

def translate(bot, update, count=500):
    log_params('translate', update)
    bot.sendChatAction(chat_id=update.message.chat_id, action=ChatAction.TYPING)
    parser = Parser(update.message.text)
    translated_text = parser.get_translated_text(length=count)
    return bot.sendMessage(chat_id=update.message.chat_id, text=translated_text, parse_mode=ParseMode.HTML)

def unknown(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Извините, я не понимаю данную команду.")

'''
def complete(bot, update):
    translate(bot, update, count=MAX_LENGTH)
'''

def main():
    updater = Updater(TOKEN)
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Add handlers for Telegram messages
    dp.addTelegramCommandHandler("start", start)
    dp.addTelegramMessageHandler(translate)
    #dp.addTelegramCommandHandler("Complete", complete)
    dp.addUnknownTelegramCommandHandler(unknown)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()