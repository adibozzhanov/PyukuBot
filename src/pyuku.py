from commands import commands
import decorators

from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# This is the main bot class
class Pyuku(Bot):
    def __init__(self, token):
        super().__init__(token)

        updater = Updater(token, use_context=True)

        self.dp = updater.dispatcher

        decorators.bot = self

        # add handlers
        self.initHandlers()

        updater.start_polling()
        print("Pyuku is running!")
        updater.idle()

    # initialise all command handlers
    def initHandlers(self):
        for command in commands:
            self.dp.add_handler(CommandHandler(command, commands[command][0]))

    # Help is a special command handler that contains info about each command
    # Thus we create it automatically after all handlers are initialised
