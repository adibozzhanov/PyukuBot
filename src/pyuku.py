from os import walk

from telegram import Bot

from commands import *

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

class Pyuku(Bot):

    def __init__(self, token):
        super().__init__(token)

        updater = Updater(token, use_context = True)

        dp = updater.dispatcher

        # add handlers
        self.initHandlers()


        updater.start_polling()
        print("Pyuku is running!")
        updater.idle()

    def initHandlers(self):
        f = []
        
        for (dirpath, dirnames, filenames) in walk("commands"):
            f.extend(filenames)

        for command in f:
            exec("import command.{}")
        
        
        
