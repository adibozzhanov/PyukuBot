from random import choice
from decorators import named_message

description = "says hello to the user"


@named_message
def main(name):
    greetings = [
        "pleased to meet you",
        "it's very nice to meet you",
        "fuck you",
        "pleased to make your acquaintance",
    ]
    return f"Hello {name}, {choice(greetings)}!"
