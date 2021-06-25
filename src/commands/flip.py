import random
from decorators import static_command

description = "flips a coin"


@static_command
def main():
    choices = ["HEADS", "TAILS"]
    return f"The coin landed on: {random.choice(choices)}"
