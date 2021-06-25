bot = None  # this will get overwritten in the bot class. Very hacky but Idc

# Documentaion for how to use these can be found in the readme

# use this decorator if your command doesn't take any arguments
# perfect for any random generator
def static_command(func):
    def command(update, context):
        chat_id = update.message.chat.id
        text = func()
        bot.send_message(chat_id=chat_id, text=text)

    return command


# use that if you want to include senders name in the reply message
def named_static_command(func):
    def command(update, context):
        chat_id = update.message.chat.id
        name = update.message.from_user.first_name
        text = func(name)
        bot.send_message(chat_id=chat_id, text=text)

    return command
