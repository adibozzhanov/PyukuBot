import random
from decorators import static_command

description = "answers yes or no"

@static_command
def main():
    answers = ["YES", "NO"]
    return random.choice(answers)
    

    
