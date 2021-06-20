

bot = None

# use this decorator if your command doesn't take any arguments
# perfect for any random generator
def static_command(func):
    def command(update, context):
        chat_id = update.message.chat.id
        text = func()
        print(bot)
        bot.send_message(chat_id = chat_id, text = text)
    return command


def named_static_command(func):
    def command(update, context):
        chat_id = update.message.chat.id
        name = update.message.from_user.first_name
        text = func(name)

        bot.send_message(chat_id = chat_id, text = text)

    return command
        
        
    
    
