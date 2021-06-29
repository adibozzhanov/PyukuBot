import random
from decorators import message

description = "flips a coin"


@message
def main():
    choices = ["HEADS", "TAILS"]
    return f"The coin landed on: {random.choice(choices)}"
