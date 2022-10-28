from telegram.ext.updater import Updater
import os
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup
from collections import OrderedDict
import requests

import json
import f
# Content of f.py
# # Module: f.py
# from telegram.ext.updater import Updater
# updater = Updater("Token", use_context=True)

t1 = "/Tickets"
t2 = "/Help"

def start(update: Update, context: CallbackContext):
    buttons = [[KeyboardButton(t1)], [KeyboardButton(t2)]]
    context.bot.send_message(chat_id=update.effective_chat.id, text="Bot made to get notified when tickets are available for sale.", reply_markup=ReplyKeyboardMarkup(buttons))

def help(update: Update, context: CallbackContext):
    update.message.reply_text("""Available Commands :
    /Tickets  - Tickets""")


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

def Tickets_function(update: Update, context: CallbackContext):
    i = 0
    n = 0
    while i == 0: 
        if n > 0:
            os.sleep(1000*30)
            # os.sleep(1000*60*60)
        n = n + 1
        scrape()
        ret = open_file()
        if (ret == ""):
            ret = "You will receive a notification when a new game tickets will be available for sale!"
        else: i = 1
    update.message.reply_text(ret)
    
def scrape():
    os.system("snscrape --jsonl --progress --max-results 50 twitter-search \"from:JuventusFCWomen\" > tweets.json && cat tweets.json | jq '.content' > data.txt")
    
def open_file():
    with open('data.txt','r') as file:
        for line in file:
            for word in line.split():
                if(word == "ticket" or word == "tickets" or word == "ticket." or word == "tickets." or word == "tickets." or word == "tickets." or word == "ticket," or word == "tickets," or word == "ticket!" or word == "tickets!" or word == "ticket?" or word == "tickets?"):
                    Line = line
                    return Line
        Line = ""
        return Line

    
f.updater.dispatcher.add_handler(CommandHandler('start', start))
f.updater.dispatcher.add_handler(CommandHandler('help', help))
f.updater.dispatcher.add_handler(CommandHandler('Tickets', Tickets_function))
f.updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
f.updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
f.updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))
f.updater.start_polling()
