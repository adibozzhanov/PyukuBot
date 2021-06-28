import random
from bottoken import TOKEN
from telegram import Bot

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters


class Pyukumuku(Bot):
    def __init__(self):
        super().__init__(TOKEN)
        self.coin = ["HEADS", "TAILS"]
        self.yesno = ["YES", "NO"]

        
        updater = Updater(TOKEN, use_context = True)

        dp = updater.dispatcher

        dp.add_handler(CommandHandler("flip", self.flip))
        dp.add_handler(CommandHandler("yn", self.yn))
        dp.add_handler(CommandHandler("roll", self.roll))
        dp.add_handler(CommandHandler("help", self.help))
        dp.add_error_handler(self.error)

        updater.start_polling()
        print("Pyukumuku is running")
        updater.idle()


    def help(self, update, context):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        self.sendMessage(chat_id = chat_id, text = f"Commands:\n/flip - flips a coin\n/yn - yes/no answer\n/roll <n1> <n2> - a random number between n1 and n2")


    def flip(self,update, context):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        c = random.choice(self.coin)
        self.sendMessage(chat_id = chat_id, text = f"The coin landed on {c}")

    def yn(self, update, context):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id

        c = random.choice(self.yesno)
        self.sendMessage(chat_id = chat_id, text = f"I am confident that the answer is {c}")

    def roll(self, update, context):
        chat_id = update.message.chat.id
        msg_id = update.message.message_id
        name = update.message.from_user.first_name

        try:
            val1, val2 = context.args[0], context.args[1]
            ret = random.randint(int(val1), int(val2))
            self.sendMessage(chat_id = chat_id, text = f"Here is a numebr for you: {ret}")
        except:
            self.sendMessage(chat_id = chat_id, text = f"I'm sorry {name}, but it seems like your brain is too small to use roll.\n\nHint: roll n1 n2. (n1 < n2)")
            
        
        

    def error(self,update, context):
        print(f"Update {update} caused an error {context.error}")
        
        
        



if __name__ == "__main__":
    Pyukumuku()

