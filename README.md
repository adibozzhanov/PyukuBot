# PyukuBot
A telegram bot that can do stuff...

It can do all sorts of random things. 

Add it to your telegram group chat and some of the features will definitely brighten up your group chat.

# Contributing
You can contribute to the pyuku bot in multiple ways. Generally, any sort of feature supported by a new command is very much pleased. 


## Adding a new command

Adding a new command is made very simple. Only very basic python knowledge is required.

All you need to do is to create a file with the `main` function in there that returns a string and that's it.
The decorators will take care of all the bot logic and you won't need to ever touch these.


If you want to add a new command for the bot to support, add a new `nameofyourcommand.py` file in `/src/commands` directory.

The format of the command file.

 - The file MUST contain a `main` function that takes in parameters depending on the chosen decorator, and returns a `string`
 
 - The `main` function MUST use one of the predefined decorators. See next section on what decorators are available.
 
 - The file MUST contain a `description` variable declared at the outer most scope, that has a short description of the command. 
 
An example of the command file:

```python
# hello.py
from decorators import static_command

description = "replies with a hello message."

@static_command
def main():
    return "Hi! I'm Pyuku!"

```
 
 - `description` is needed for the command to be added into the `/help` command.
 - `main` is where you code goes. You are free to create other methods and classes in the file if so needed.
