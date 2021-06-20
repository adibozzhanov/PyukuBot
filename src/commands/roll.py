import random
from decorators import named_static_command

description = "rolls a number between 0 and 100"

@named_static_command
def main(name):
    num = random.randint(0,100)
    return f"{name} rolled a number: {num}"
