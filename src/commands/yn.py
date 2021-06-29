import random
from decorators import reply

description = "answers yes or no"


@reply
def main():
    answers = ["YES", "NO"]
    return random.choice(answers)
