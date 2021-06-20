from random import choice
description = "says hello to the user"
@named_static_command
def main(name):
    greetings = ["pleased to meet you", "it's very nice to meet you", "fuck you", "pleased to make your acquaintance"]
    return f"Hello {name}, {choice(greetings)}!"
