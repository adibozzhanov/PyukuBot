bot = None  # this will get overwritten in the bot class. Very hacky but Idc

# Documentaion for how to use these can be found in the readme


# a normal message without any arguments
def message(func):
    def command(update, context):
        text = func()
        update.message.reply_text(text)

    return command


# message that has the name of the person who triggered the command in it
def named_message(func):
    def command(update, context):
        name = update.message.from_user.first_name
        text = func(name)
        update.message.reply_text(text)

    return command


# a reply to the message containing the command
def reply(func):
    def command(update, context):
        chat_id = update.message.chat.id
        text = func()
        update.message.reply_text(text, quote=True)

    return command
