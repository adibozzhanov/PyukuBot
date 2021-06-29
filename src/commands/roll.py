import random
from decorators import named_message

description = "rolls a number between 0 and 100"


@named_message
def main(name):
    num = random.randint(0, 100)
    return f"{name} rolled a number: {num}"
